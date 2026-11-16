import json, sys, re, collections, statistics as st
path = sys.argv[1]
R=[json.loads(l) for l in open(path) if l.strip()]
print("registros:",len(R))
C=collections.Counter
print("empresas:",C(r['company'] for r in R).most_common())
print("anos:",sorted(C(r['date'][:4] for r in R).items()))
print("meses mais antigos/recentes:",min(r['date'] for r in R),max(r['date'] for r in R))
print("severidade:",C(r['severity'] for r in R))
print("categorias:",C(c for r in R for c in r['categories']).most_common())
def uniq(f, norm=lambda s:s):
    vals=[norm(r[f] if isinstance(r[f],str) else json.dumps(r[f])) for r in R]
    return len(set(vals))
strip_co=lambda s: re.sub(r'(GitHub|Cloudflare|OpenAI|Datadog|Vercel|Discord|Sentry|DigitalOcean|npm|HashiCorp|Supabase|Atlassian|Reddit|CircleCI)','X',s)
for f in ['breaking_config_code','remediation_patch','prevention_checklist']:
    print(f"{f}: {uniq(f)} valores distintos; normalizando nome de empresa/stack:",
          uniq(f, lambda s: re.sub(r'\[.*?\]|".*?"|during .*','',strip_co(s))))
rca=[r['root_cause_analysis'] for r in R]
print("RCA com prefixo 'Official investigation timeline':",sum(x.startswith('Official investigation') for x in rca))
print("RCA template genérico (capacity saturation):",sum('capacity saturation and upstream' in x for x in rca))
print("RCA truncada em ~450 chars:",sum(len(x)>=440 for x in rca), " comprimento mediano:",st.median(map(len,rca)))
sl=[r['symptom_logs'] for r in R]
print("symptom_logs mediano chars:",st.median(map(len,sl))," nº updates mediano:",st.median(s.count('\n')+1 for s in sl))
kw=re.compile(r'root cause|caused by|due to|misconfig|deploy|config change|rollback|rolled back|certificate|dns|bgp|database|memory|cpu|disk|capacity|upstream|third.party|provider',re.I)
print("incidentes cujo texto real menciona alguma causa/mecanismo:",sum(bool(kw.search(s)) for s in sl))
generic=re.compile(r'^(we are (currently )?investigating|this incident has been resolved|a fix has been implemented|we are continuing to (monitor|investigate))',re.I)
def informative(s):
    lines=[re.sub(r'^\[.*?\) ?:? ?','',l) for l in s.split('\n')]
    return sum(1 for l in lines if len(l)>60 and not generic.match(l.strip()))
print("incidentes com >=1 update informativo (>60 chars, não-boilerplate):",sum(informative(s)>0 for s in sl))
print("source_url domínios:",C(re.sub(r'https?://([^/]+).*',r'\1',r['source_url']) for r in R).most_common(5))
print("ids duplicados:",len(R)-len({r['incident_id'] for r in R}),"títulos duplicados:",len(R)-len({(r['company'],r['title'],r['date']) for r in R}))
print("status metadata:",C(r['metadata'].get('status') for r in R))
print("stack (top):",C(s for r in R for s in r['service_stack']).most_common(12))
