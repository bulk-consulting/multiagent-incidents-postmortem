# E6 — API (FastAPI) e Interface (Streamlit)

Versão simples para a semana de 24/11: o analista escreve no chat, a interface chama a API, a API
roda o grafo do começo ao fim e devolve o relatório.

```
Streamlit (frontend/)  ──HTTP──►  FastAPI (app/)  ──►  grafo LangGraph
                                                       hoje: grafo fake (app/services/fake_graph.py)
                                                       depois: grafo real dos 4 agentes
```

## Como rodar

Na raiz do repositório, com o `.venv` ativo e `pip install -r requirements.txt`:

```powershell
uvicorn app.main:app --reload
```

```powershell
streamlit run frontend/streamlit_app.py
```

- Interface: http://localhost:8501
- Swagger (documentação automática da API): http://localhost:8000/docs

## Endpoints

Todos sob `/api/v1`.

| Método | Rota | Função |
|---|---|---|
| `GET` | `/health` | Verifica se a API está no ar |
| `POST` | `/incidents` | Recebe a mensagem (e o histórico da conversa), roda o grafo e devolve o relatório |

Exemplo de entrada:

```json
{
  "message": "a replicação atrasou e um admin apagou o diretório errado",
  "history": [
    {"role": "user", "content": "o banco caiu"},
    {"role": "assistant", "content": "Pode me contar um pouco mais?..."}
  ]
}
```

A saída é `{incident_id, seconds, report}`, em que `report` tem o formato do Agente Relatório
(`agents/reporting/schema.py`, classe `Report`). Entrada inválida (mensagem vazia, por exemplo) → `422`.

## Organização (camadas da E1.4, seção 7)

| Pasta | O que faz |
|---|---|
| `app/main.py` | cria a aplicação FastAPI e registra as rotas |
| `app/api/` | rotas HTTP (só entrada e saída) |
| `app/schemas/` | classes Pydantic de entrada e saída |
| `app/services/` | lógica: monta a entrada do grafo, roda o grafo, devolve o relatório |
| `frontend/` | tela de chat em Streamlit; só conversa com a API |

## Diferenças em relação à E1.4 (decididas para esta semana)

- **Síncrono:** o `POST /incidents` espera o grafo terminar e já devolve o relatório. A E1.4 propõe
  responder `202` e consultar o andamento depois (polling); fica para uma próxima versão.
- **Sem pausa/retomada:** se faltar informação, o relatório (tipo `inconclusive`) traz as perguntas e
  o fluxo termina. O analista responde com uma nova mensagem.
- **Conversa sem banco:** a interface guarda o histórico e o envia a cada mensagem; a API junta
  tudo o que o analista disse em uma única descrição e roda o grafo de novo. Nada fica salvo na API.
- **`incident_id`:** gerado pela API (`INC-xxxxxxxx`) só para acompanhar a execução nos logs; ainda
  não existe tabela de investigações.

## Grafo fake e grafo real

**Temporário (24/11):** enquanto o grafo dos 4 agentes não fica pronto, a API usa
`app/services/fake_graph.py`: um grafo LangGraph de verdade, com um único nó falso, sem LLM e sem banco.

- Com poucas palavras, devolve um relatório `inconclusive` pedindo mais informação.
- Com mais palavras, devolve um `diagnosis` baseado em um post-mortem real: Cloudflare R2, março de
  2025 (DAN-015), credenciais rotacionadas e publicadas no ambiente errado.

Cenário para a demonstração (o analista vê o sintoma, não a causa):

> o upload de arquivos está dando erro

> Desde as 21h40 todos os uploads para o nosso armazenamento de objetos falham: o PUT /objects
> devolve 401 Unauthorized com {"error": "invalid_credentials"} e mais ou menos um terço das
> leituras também falha. Não fizemos nenhum deploy hoje.

Para ligar o grafo real, basta trocar o import em `get_graph()` (`app/services/incident_service.py`).
O grafo real precisa:

1. aceitar a entrada `{"incident_id": str, "description": str}`;
2. devolver no estado final a chave `report` com um `Report` de `agents/reporting/schema.py`.

Se o grafo real usar outros nomes, a adaptação fica só em `app/services/incident_service.py`.
A API e a interface não mudam. O Agente Pesquisa precisa do PostgreSQL + pgvector (Docker) ligado.
