# Avaliação — postmortem-intelligence

Avaliação feita em 30/10/2026 do repositório
[akashhalgekar/postmortem-intelligence](https://github.com/akashhalgekar/postmortem-intelligence),
commit `a4ef1bbe3da186ed071f934b58869da2cba6e75a` (27/09/2026). Licença MIT.

## Veredito

**Descartar como fonte de dados.** Todos os registros são fictícios, e o próprio repositório declara isso.
Usar esses dados no RAG faria o Incident Copilot citar incidentes que nunca aconteceram.

O repositório é uma ferramenta (busca de post-mortems similares + resumo para gestores), não um dataset.
Algumas ideias de arquitetura servem de referência para a E1.4.

## Dados do repositório

| Arquivo | Conteúdo |
|---|---|
| `data/sample_postmortems.csv` | 36 registros: cadeia de suprimentos (13), logística (7), manufatura (7), gestão de projetos (5), TI e sistemas (4) |
| `data/examples/it_incidents_example.csv` | 6 incidentes de TI curtos, só para demonstrar o mapeamento de colunas |
| `data/examples/markdown/INC-2024-017.md` | 1 exemplo em Markdown (impressora de etiquetas numa doca de expedição) |

Campos do CSV principal: `incident_id`, `title`, `date`, `domain`, `category`, `severity`, `description`,
`root_cause`, `contributing_factors`, `actions_taken`, `outcome`, `lessons_learned`, `kpis_impacted`.

## Por que descartar

- **Dados fictícios.** O cabeçalho de `data/build_sample_data.py`, que gera o CSV, avisa que todo registro é
  fictício: empresas, fornecedores, fábricas e números foram inventados para parecer reais. O README repete
  o aviso ("Sample data is fictional").
- **Quase nada de TI.** Só 4 de 36 registros são de TI, e são de sistemas de negócio (go-live de ERP,
  migração de WMS, cadastro duplicado de fornecedor, ransomware num operador logístico), não de
  infraestrutura.
- **Pouco detalhe.** Cada campo tem 1 a 3 frases, sem timeline nem sintomas técnicos.

## Referências de arquitetura (para a E1.4)

- **Recusa por falta de evidência:** se nenhum incidente passa de um limite mínimo de similaridade, a
  ferramenta informa que não há evidência em vez de gerar resposta (`postmortem_intel/engine.py`).
- **Validação de citações:** cada ponto do resumo gerado é conferido; citações de incidentes que não foram
  recuperados são removidas e pontos sem citação válida são descartados (`brief.validate()` em
  `postmortem_intel/brief.py`).
- **Cache invalidado por versão:** a chave inclui pergunta, configuração de busca, índice, modelo e versão do
  prompt (`postmortem_intel/cache.py`).
- **Mapeamento de colunas configurável** para ingerir CSV, Excel, JSON ou Markdown (`config.yaml`,
  `postmortem_intel/ingest.py`).

Como a licença é MIT, o código pode ser reaproveitado com atribuição.
