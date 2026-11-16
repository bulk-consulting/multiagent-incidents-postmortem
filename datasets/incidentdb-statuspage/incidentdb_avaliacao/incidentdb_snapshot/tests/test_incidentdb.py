import unittest
import json
import tempfile
from pathlib import Path
import argparse

from src.schema import IncidentRecord
from src.validator import IncidentValidator, ValidationError
from src.search import IncidentSearchEngine
from src.cli import load_records, cmd_export_rag


class TestIncidentDBSchema(unittest.TestCase):
    def setUp(self):
        self.sample_valid_data = {
            "incident_id": "INC-2026-TEST-01",
            "company": "Acme Cloud",
            "date": "2026-03-15",
            "title": "Kernel Lock Contention Outage Under Synthetic High-Throughput Ingestion",
            "severity": "CRITICAL",
            "service_stack": ["Linux Kernel", "eBPF", "Kafka", "Rust"],
            "categories": ["KERNEL_PANIC", "LOCK_CONTENTION", "HIGH_THROUGHPUT"],
            "symptom_logs": (
                "[10492.102] kernel: watchdog: BUG: soft lockup - CPU#4 stuck for 26s! [worker:8291]\n"
                "[10492.103] Call Trace:\n"
                "[10492.104]  <IRQ>\n"
                "[10492.105]  __bpf_prog_run22+0x4c/0x90\n"
                "[10492.106]  sch_handle_ingress+0x14f/0x2f0\n"
                "[10492.107]  __netif_receive_skb_core+0x4a2/0xce0"
            ),
            "root_cause_analysis": (
                "An unoptimized eBPF TC filter attached to ingress virtual network interfaces "
                "acquired a global spinlock on per-packet ring buffer updates during traffic spikes, "
                "resulting in soft lockups across all packet processing CPU cores."
            ),
            "breaking_config_code": (
                "# Unbounded spinlock acquisition in eBPF program\n"
                "static __always_inline int process_packet(struct __sk_buff *skb) {\n"
                "    bpf_spin_lock(&global_state_lock);\n"
                "    global_packet_counter++;\n"
                "    bpf_spin_unlock(&global_state_lock);\n"
                "    return TC_ACT_OK;\n"
                "}"
            ),
            "remediation_patch": (
                "# Lock-free per-CPU array map replacement\n"
                "struct { \n"
                "    __uint(type, BPF_MAP_TYPE_PERCPU_ARRAY);\n"
                "    __type(key, __u32);\n"
                "    __type(value, __u64);\n"
                "    __uint(max_entries, 1);\n"
                "} percpu_packet_counter SEC(\".maps\");\n\n"
                "static __always_inline int process_packet(struct __sk_buff *skb) {\n"
                "    __u32 key = 0;\n"
                "    __u64 *count = bpf_map_lookup_elem(&percpu_packet_counter, &key);\n"
                "    if (count) (*count)++;\n"
                "    return TC_ACT_OK;\n"
                "}"
            ),
            "prevention_checklist": [
                "Audit all kernel eBPF probes for shared spinlock contention under 100Gbps network simulation",
                "Enforce per-CPU map primitives for high-frequency telemetry counters",
                "Integrate CI load-testing with soft-lockup detector threshold set to 5 seconds"
            ]
        }

    def test_record_instantiation_and_markdown(self):
        record = IncidentRecord.from_dict(self.sample_valid_data)
        self.assertEqual(record.incident_id, "INC-2026-TEST-01")
        self.assertEqual(record.severity, "CRITICAL")
        self.assertEqual(len(record.service_stack), 4)

        md = record.to_markdown()
        self.assertIn("# [INC-2026-TEST-01] Kernel Lock Contention Outage", md)
        self.assertIn("## 2. Root Cause Analysis", md)
        self.assertIn("## 4. Remediation Patch", md)
        self.assertIn("## 5. Prevention & Hardening Checklist", md)
        self.assertIn("bpf_spin_lock", md)

    def test_to_dict_roundtrip(self):
        record = IncidentRecord.from_dict(self.sample_valid_data)
        d = record.to_dict()
        self.assertEqual(d["incident_id"], record.incident_id)
        self.assertEqual(d["company"], record.company)
        self.assertEqual(d["categories"], record.categories)


class TestIncidentValidator(unittest.TestCase):
    def setUp(self):
        self.validator = IncidentValidator()
        self.valid_data = {
            "incident_id": "INC-2026-TEST-02",
            "company": "SaaS Platform",
            "date": "2026-04-10",
            "title": "Postgres Read Replica Starvation Under Analytics Query Spill",
            "severity": "HIGH",
            "service_stack": ["PostgreSQL", "Patroni", "Python"],
            "categories": ["DATABASE_REPLICATION", "RESOURCE_STARVATION"],
            "symptom_logs": (
                "FATAL: terminating connection due to conflict with recovery\n"
                "DETAIL: User query might have needed to see row versions that must be removed.\n"
                "HINT: In a moment you should be able to reconnect to the database and repeat your command.\n"
                "STATEMENT: SELECT COUNT(*) FROM ledger_events GROUP BY customer_id;"
            ),
            "root_cause_analysis": (
                "Long-running unindexed batch analytics queries executed directly on primary read replicas "
                "caused replication conflicts when WAL records for dead tuple cleanup arrived, causing Patroni "
                "heartbeat timeouts and subsequent false failover cascading loops."
            ),
            "breaking_config_code": (
                "# Unbounded replica query execution timeout:\n"
                "max_standby_archive_delay = -1\n"
                "max_standby_streaming_delay = -1\n"
                "hot_standby_feedback = off"
            ),
            "remediation_patch": (
                "# Bounded replica statement limits and feedback activation:\n"
                "max_standby_streaming_delay = 30s\n"
                "hot_standby_feedback = on\n"
                "statement_timeout = 15000\n"
                "idle_in_transaction_session_timeout = 10000"
            ),
            "prevention_checklist": [
                "Route analytical workloads to dedicated decoupled read-only replicas",
                "Set strict 15-second statement_timeout on all customer-facing read replicas",
                "Alert on replication lag exceeding 100MB WAL backlog"
            ]
        }

    def test_valid_record_passes(self):
        record = IncidentRecord.from_dict(self.valid_data)
        is_valid, errors = self.validator.validate_record(record)
        self.assertTrue(is_valid, f"Expected valid record but got errors: {errors}")
        self.assertEqual(len(errors), 0)

    def test_banned_stub_triggers_failure(self):
        bad_data = dict(self.valid_data)
        bad_data["root_cause_analysis"] = "This is a TODO stub that needs more research later in production."
        record = IncidentRecord.from_dict(bad_data)
        with self.assertRaises(ValidationError) as ctx:
            self.validator.assert_valid(record)
        self.assertIn("Prohibited stub/placeholder token detected: 'TODO'", str(ctx.exception))

    def test_short_root_cause_triggers_failure(self):
        bad_data = dict(self.valid_data)
        bad_data["root_cause_analysis"] = "Database crashed."
        record = IncidentRecord.from_dict(bad_data)
        with self.assertRaises(ValidationError) as ctx:
            self.validator.assert_valid(record)
        self.assertIn("root_cause_analysis must be dense and explanatory", str(ctx.exception))

    def test_empty_prevention_checklist_fails(self):
        bad_data = dict(self.valid_data)
        bad_data["prevention_checklist"] = []
        record = IncidentRecord.from_dict(bad_data)
        with self.assertRaises(ValidationError) as ctx:
            self.validator.assert_valid(record)
        self.assertIn("prevention_checklist must contain at least 2", str(ctx.exception))


class TestSearchEngineAndCLI(unittest.TestCase):
    def setUp(self):
        self.db_path = Path("data/incident_database.jsonl")
        self.assertTrue(self.db_path.exists(), "Master database file must exist for tests.")
        self.records = load_records(self.db_path)
        self.engine = IncidentSearchEngine(self.records)

    def test_database_record_count(self):
        self.assertGreaterEqual(len(self.records), 20)

    def test_search_by_company(self):
        results = self.engine.search(query="Cloudflare")
        self.assertGreaterEqual(len(results), 1)
        self.assertEqual(results[0]["record"].company, "Cloudflare")

    def test_search_by_keyword(self):
        results = self.engine.search(query="OpenAI")
        self.assertGreaterEqual(len(results), 1)
        self.assertEqual(results[0]["record"].company, "OpenAI")

    def test_filter_by_severity(self):
        critical_results = self.engine.search(query="", severity="CRITICAL")
        self.assertGreaterEqual(len(critical_results), 5)
        for r in critical_results:
            self.assertEqual(r["record"].severity, "CRITICAL")

    def test_statistics_aggregation(self):
        stats = self.engine.get_statistics()
        self.assertIn("total_incidents", stats)
        self.assertEqual(stats["total_incidents"], len(self.records))
        self.assertIn("severity_distribution", stats)
        self.assertIn("category_distribution", stats)
        self.assertIn("top_technologies", stats)

    def test_export_rag_vault(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            args = argparse.Namespace(data=str(self.db_path), output=tmp_dir)
            cmd_export_rag(args)
            tmp_path = Path(tmp_dir)
            md_files = list(tmp_path.rglob("*.md"))
            self.assertEqual(len(md_files), len(self.records))
            
            # Check content of one file
            sample_file = md_files[0]
            content = sample_file.read_text(encoding="utf-8")
            self.assertIn("# [INC-", content)
            self.assertIn("## 2. Root Cause Analysis", content)
            self.assertIn("## 4. Remediation Patch", content)


if __name__ == "__main__":
    unittest.main()
