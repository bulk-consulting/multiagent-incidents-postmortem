# Avaliação — postmortem-templates

Avaliação feita em 30/10/2026 do repositório
[dastergon/postmortem-templates](https://github.com/dastergon/postmortem-templates),
commit `ebdaf8f122cf1d9f5c2983b37861be038c9acc89` (último commit em 23/12/2021). Licença CC0 1.0 (domínio público).

## Veredito

**Não é um dataset e não entra no RAG.** O repositório tem só 7 modelos vazios de post-mortem (de 30 a 290
palavras cada) e uma lista de links. Não contém nenhum incidente.

**Serve como referência para definir o schema normalizado do corpus e o formato de saída do Copilot.** As
seções que se repetem nos 7 modelos mostram quais campos todo post-mortem deve ter, o que ajuda a extrair e
padronizar os documentos da danluu e das statuspages em campos comparáveis.

## O que tem

| Item | Valor |
|---|---|
| Modelos | 7 arquivos Markdown em `templates/`: Azure, Elastic, Google (API infra), Michael Kehoe, Real World SRE, SRE Book (Google) e The Cloud Book |
| Exemplos de post-mortems reais | 7 links no README; 4 já estão na lista da danluu (GCE #16007, DynamoDB 5467D2, GitLab 2017, Elastic Cloud 2019) |
| Outros links | Artigos sobre cultura de post-mortem sem culpados (Etsy, Box, O'Reilly e outros) |
| Tamanho | 60 KB, 35 commits; sem atualização desde 2021 |

## Seções dos modelos

| Seção | Modelos que a têm | Campo correspondente no corpus / no Copilot |
|---|---|---|
| Ações corretivas e preventivas | 7 de 7 | `acoes_preventivas` |
| Resumo | 6 de 7 (Elastic usa "contexto" e "o que aconteceu") | `resumo` |
| Impacto (usuários, infraestrutura) | 6 de 7 | `impacto`, `servicos_afetados` |
| Causa raiz | 6 de 7 (The Cloud Book usa "condições contribuintes") | `causa_raiz` (com nível CONCRETA/VAGA/SEM_CAUSA) |
| Timeline | 6 de 7 | `timeline`, `inicio`, `fim`, `duracao` |
| Resolução / mitigação | 5 de 7 | `mitigacao` |
| Gatilho (separado da causa raiz) | 2 (SRE Book, Kehoe) | `gatilho` |
| Detecção (como e quando foi detectado) | 2 (SRE Book, Kehoe); Kehoe pede TTD, TTM e TTR | `deteccao`, métricas de tempo |
| Lições aprendidas (o que foi bem, mal, sorte) | 3 (SRE Book, Kehoe, The Cloud Book) | `licoes` |

## O que vale aproveitar

- **Schema mínimo dos chunks do RAG:** resumo, impacto, gatilho, causa raiz, detecção, mitigação, ações
  preventivas e timeline. Separar **gatilho** de **causa raiz** (como fazem o SRE Book e o modelo de Kehoe)
  evita que o Copilot confunda o evento que disparou o incidente (ex.: um deploy) com a falha de fundo
  (ex.: falta de validação de configuração).
- **Formato da resposta do Copilot e do rascunho de post-mortem:** usar a estrutura do SRE Book (a mais
  citada e completa sem ser longa) como base do rascunho que o Copilot gera ao fim do incidente.
- **Métricas de tempo do modelo de Kehoe (TTD, TTM, TTR):** campos úteis para comparar incidentes e para os
  dados que a Stratus registra.
- Os 3 exemplos que não estão na danluu (Buildbucket 2015, Google API infra 2013 e o histórico de status do
  Azure) podem ser avaliados junto com os incidentes que faltam coletar; não justificam coleta separada.
