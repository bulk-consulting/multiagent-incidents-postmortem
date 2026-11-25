# E6 — API (FastAPI) e Interface (Streamlit)

Versão simples para a semana de 24/11: o analista escreve no chat, a interface chama a API, a API
roda o grafo do começo ao fim e devolve o relatório.

```
Streamlit (frontend/)  ──HTTP──►  FastAPI (app/)  ──►  grafo dos 4 agentes (agents/orchestration/graph.py)
                                                       Triagem → Pesquisa → Diagnóstico → Relatório
```

## Como rodar

Na raiz do repositório, com o `.venv` ativo e `pip install -r requirements.txt`. Antes, ligar o Docker
(o Agente Pesquisa busca no PostgreSQL + pgvector) e conferir a chave do NIM no `.env`:

```powershell
uvicorn app.main:app --reload
```

```powershell
streamlit run frontend/streamlit_app.py
```

- Interface: http://localhost:8501
- Swagger (documentação automática da API): http://localhost:8000/docs
- Logs: no terminal da API aparece uma linha por agente (`[triage]`, `[research]`, `[diagnosis]`,
  `[report]`), com o tempo e o resumo do resultado. Uma investigação leva de 2 a 6 minutos com o NIM gratuito.

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

A saída é `{incident_id, seconds, report}`, em que `report` tem sempre o formato do Agente Relatório
(`agents/reporting/schema.py`, classe `Report`). Entrada inválida (mensagem vazia, por exemplo) → `422`.

O campo `report.kind` diz que tipo de resposta é. Todas têm `summary` e `message` (o texto para o chat):

| `kind` | Quando | Quem monta |
|---|---|---|
| `diagnosis` | a evidência basta: causas, correção e fontes | Agente Relatório (LLM) |
| `inconclusive` | a evidência não basta, ou um agente falhou | Agente Relatório, ou código no grafo |
| `questions` | falta informação: as perguntas para o analista | código na API |
| `related_incident` | o problema já está em investigação | código (`agents/reporting/related.py`) |

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
- **Sem retomada:** quando o grafo pausa para perguntar (`interrupt()`), a API devolve as perguntas
  (tipo `questions`) e a execução termina ali. O analista responde com uma nova mensagem, que roda o
  grafo de novo com toda a conversa.
- **Limite de perguntas:** a API passa ao grafo as respostas que o analista já deu na conversa
  (`analyst_answers`: as mensagens depois da primeira). Com 3 respostas (`MAX_ANALYST_ROUNDS`), o grafo
  não pergunta mais e entrega o relatório com o que tem (inconclusivo, se a evidência não basta).
- **Idioma:** o texto fixo antes das perguntas sai em português ou inglês (os idiomas do projeto).
- **Conversa sem banco:** a interface guarda o histórico e o envia a cada mensagem; a API junta
  tudo o que o analista disse em uma única descrição e roda o grafo de novo. Nada fica salvo na API.
- **`incident_id`:** gerado pela API (`INC-xxxxxxxx`) só para acompanhar a execução nos logs; ainda
  não existe tabela de investigações.

## Testes

```powershell
python -m app.tests.test_api
```

Roda a API com o grafo real, mas com agentes falsos (sem LLM e sem banco, em segundos), e confere que
cada final do grafo (`diagnosis`, `questions`, `related_incident`, agente com erro) vira o mesmo formato.

## Cenário para a demonstração

O analista vê o sintoma, não a causa. O post-mortem parecido é o do R2 da Cloudflare (DAN-015):
credenciais rotacionadas e publicadas no ambiente errado.

> o upload de arquivos está dando erro

> Desde as 21h40 todos os uploads para o nosso armazenamento de objetos falham: o PUT /objects
> devolve 401 Unauthorized com {"error": "invalid_credentials"} e mais ou menos um terço das
> leituras também falha. Não fizemos nenhum deploy hoje.
