"""Chat screen for the analyst. It only talks to the FastAPI API (it never calls the agents directly).

Run from the repository root, with the API already running:

    streamlit run frontend/streamlit_app.py
"""
import os

import requests
import streamlit as st

# 127.0.0.1 and not "localhost": on Windows, "localhost" tries IPv6 first and each failed try takes seconds.
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/api/v1")
TIMEOUT_SECONDS = 600  # the real agents can take several minutes (3 to 6 with the free NIM)
CONFIDENCE = {"high": "alta", "medium": "média", "low": "baixa"}

st.set_page_config(page_title="Incident Copilot", page_icon="🛠️")
st.title("🛠️ Incident Copilot")
st.caption("Descreva o incidente. O sistema busca post-mortems parecidos e sugere causas e correções.")

# The conversation lives in the browser session. Each item: {"role", "content", "report" (only assistant)}.
if "messages" not in st.session_state:
    st.session_state.messages = []


def api_is_up() -> bool:
    try:
        return requests.get(f"{API_URL}/health", timeout=3).ok
    except requests.RequestException:
        return False


def show_details(report: dict, incident_id: str, seconds: float) -> None:
    """Sources and other details, folded under the answer."""
    sources = {s["url"]: s for cause in report["causes"] for s in cause["sources"]}

    # Questions or "already under investigation": nothing to unfold, only the small line at the end.
    if not sources and not report["suggested_checks"]:
        st.caption(f"{incident_id} · {seconds:.1f}s · tipo: {report['kind']}")
        return

    with st.expander(f"Fontes e detalhes ({len(sources)} fonte(s))"):
        if sources:
            st.markdown("**Post-mortems usados**")
            for s in sources.values():
                st.markdown(f"- [{s['incident_id']} — {s['title']}]({s['url']})")
        for i, cause in enumerate(report["causes"], start=1):
            st.markdown(f"**Causa {i}** — confiança {CONFIDENCE.get(cause['confidence'], cause['confidence'])}")
        if report["suggested_checks"]:
            st.markdown("**Verificações sugeridas**")
            st.markdown("\n".join(f"- {c}" for c in report["suggested_checks"]))
        st.caption(f"{incident_id} · {seconds:.1f}s · tipo: {report['kind']}")


with st.sidebar:
    if api_is_up():
        st.success("API conectada")
    else:
        st.error(f"API fora do ar ({API_URL})")
    if st.button("Nova conversa", use_container_width=True):
        st.session_state.messages = []
        st.session_state.pending = None
        st.rerun()

# Show the conversation so far.
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "report" in msg:
            show_details(msg["report"], msg["incident_id"], msg["seconds"])

# The investigation runs in two steps, so the chat box can be locked while it runs: if the analyst sent
# a second message in the middle, Streamlit would stop the script and the first answer would be lost.
#   1. the analyst sends a message → we save it as "pending" and redraw the page (box now locked);
#   2. with a pending message → we call the API, save the answer and redraw the page (box unlocked).
pending = st.session_state.get("pending")

if error := st.session_state.pop("error", None):
    st.error(f"Não foi possível investigar: {error}")

if prompt := st.chat_input("Ex.: desde as 21h40 o PUT /objects devolve 401 Unauthorized...", disabled=pending is not None):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.pending = prompt
    st.rerun()

if pending is not None:
    # everything before the pending message (which is the last one in the list)
    history = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages[:-1]]
    with st.chat_message("assistant"):
        try:
            with st.spinner("Investigando o incidente..."):
                response = requests.post(
                    f"{API_URL}/incidents",
                    json={"message": pending, "history": history},
                    timeout=TIMEOUT_SECONDS,
                )
            response.raise_for_status()
            data = response.json()
            st.session_state.messages.append({
                "role": "assistant",
                "content": data["report"]["message"],
                "report": data["report"],
                "incident_id": data["incident_id"],
                "seconds": data["seconds"],
            })
        except requests.ConnectionError:
            st.session_state.error = f"a API não responde em {API_URL}. Ela está rodando?"
            st.session_state.messages.pop()
        except requests.Timeout:
            st.session_state.error = f"a investigação passou de {TIMEOUT_SECONDS} segundos."
            st.session_state.messages.pop()
        except requests.RequestException as exc:
            detail = str(exc)
            if exc.response is not None:
                try:
                    detail = exc.response.json().get("detail", detail)
                except ValueError:
                    pass
            st.session_state.error = detail
            st.session_state.messages.pop()  # remove the message, so the analyst can send it again
    st.session_state.pending = None
    st.rerun()
