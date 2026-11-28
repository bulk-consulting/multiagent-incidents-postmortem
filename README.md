# Assistente Inteligente de Incidentes com Post-Mortem (Incident Copilot)

## Sobre o projeto

Quando um sistema cai em produção, o analista precisa entender rápido o que está acontecendo. E muitas vezes
um problema parecido já aconteceu antes na empresa e ficou registrado num post-mortem.

O Incident Copilot ajuda nessa investigação. O analista conta no chat o que está vendo e o sistema procura
post-mortems parecidos, compara com o caso dele e responde com:

- as causas mais prováveis e o post-mortem de onde cada uma saiu
- como o problema foi resolvido e como evitar que aconteça de novo
- o que o analista pode verificar agora

Se faltar informação, o sistema pergunta antes de responder.

Como ainda não temos post-mortems internos, neste projeto usamos post-mortems públicos de outras empresas para
simular essa base.

## Como funciona 

Quatro agentes trabalham em sequência:

1. **Triagem** entende o que o analista escreveu e vê se já dá para investigar.
2. **Pesquisa** procura post-mortems parecidos na base de conhecimento.
3. **Diagnóstico** compara esses post-mortems com o incidente e levanta as possíveis causas.
4. **Relatório** escreve a resposta final em português ou inglês.

O projeto usa LangGraph para orquestrar os agentes, modelos da NVIDIA NIM, PostgreSQL com pgvector para guardar
os post-mortems, FastAPI na API e Streamlit no chat.

> Este README será completado ao final do projeto.
