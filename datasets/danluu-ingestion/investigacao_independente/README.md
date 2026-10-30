# Avaliação independente — danluu/post-mortems

Avaliação feita em 30/10/2026, separada da curadoria E1.3 que já existe nesta pasta
(`data/reports/e13_final_validation.md`). O objetivo foi verificar, com método próprio, se a fonte e a
extração do pipeline são confiáveis e quanto do conteúdo serve ao Incident Copilot.

## Veredito

**A danluu deve ser a fonte principal de causa raiz, remediação, config/código alterado e prevenção.**

- **Conteúdo:** forte. Na amostra, praticamente todo documento legível traz causa concreta, e quase todos
  trazem remediação e prevenção. É o oposto dos status pages, onde só ~10% dos incidentes têm causa
  concreta (ver `../../incidentdb-statuspage/README.md`).
- **Coleta:** confiável. Os números dos relatórios batem entre si e com o catálogo.
- **Extração (`trafilatura`):** fiel. Nenhum post-mortem foi truncado nem perdeu causa, remediação ou
  prevenção. Há uma perda sistemática e localizada (atualizações de páginas do Statuspage) e ruído herdado
  do HTML. Os dois se corrigem com uma etapa de limpeza; não é preciso reextrair.
- **Alertas `needs_review`:** pouco confiáveis. A maioria dos alertas em documentos com conteúdo eram
  falsos positivos. **Não devem ser usados como filtro de exclusão.**

## O que foi avaliado

| Etapa | Escopo | Método |
|---|---|---|
| Perfil do catálogo | `README.md` do repositório danluu/post-mortems (commit de 31/08/2026) | Script `perfil_catalogo.py` |
| Conferência dos relatórios do pipeline | `summary.json`, `documents.csv`, `catalog.csv`, shortlist e registro editorial | Cruzamento de contagens e URLs |
| Comparação HTML x JSON | 30 documentos, escolhidos por tipo de alerta e de fonte | Extração independente (`extracao_independente.py`, BeautifulSoup e pdftotext) comparada frase a frase com o JSON do pipeline; leitura dos textos por LLM (Claude) |

## Números da fonte

| Item | Valor |
|---|---|
| Entradas de incidente no catálogo | 240, de 104 empresas |
| Coletadas | 224 (14 falhas, 2 bloqueadas por `robots.txt`) |
| Extraídas sem alerta / com alerta | 149 / 75 |
| Extrações vazias (páginas montadas por JavaScript) | 11 |
| Fora do escopo de TI (energia, aviação, espaço, equipamento médico, jogos etc.) | 24 no catálogo, 17 extraídas |
| Documentos de TI com texto | cerca de 196 (teto: ainda inclui artigos que não são post-mortem) |
| Aprovados na curadoria E1.3 | 20 |

## Achados da amostra (30 documentos)

**Alertas do pipeline (primeira amostra, 21 documentos):**

- 10 documentos com conteúdo estavam em `needs_review`: **8 eram falsos positivos** (login/paywall,
  erro HTTP disfarçado, poucos sinais de post-mortem, conteúdo diferente do catálogo) e 2 eram
  redirecionamentos legítimos com o conteúdo certo.
- Só os alertas de extração vazia (DAN-041, DAN-212) procediam.

**Problemas que os alertas não detectam:**

| Problema | Exemplos | Origem |
|---|---|---|
| Mesmo texto em vários idiomas | DAN-002 (coreano + inglês), DAN-064 (4 idiomas) | HTML original |
| Parágrafos repetidos | DAN-072: 84% repetido, até 28 vezes | HTML original |
| Comentários de leitores | DAN-022: ~1.600 palavras | Falha do extrator |
| Rodapés e marketing | DAN-027, DAN-083 | HTML original |
| Atualizações do Statuspage descartadas | DAN-053, 091, 130, 135, 144, 147, 192, 194 (todas as atualizações); DAN-235 (só as datas) | Falha do extrator |
| Colunas de PDF embaralhadas; título do PDF errado | DAN-191 | Limitação do PDF |
| Página vazia | DAN-041, DAN-212 | Página montada por JavaScript |

Os indicadores de completude do pipeline também não detectam esses casos (o DAN-002 está marcado 7/7).

**Atualizações do Statuspage:** 12 documentos do catálogo estão hospedados no Statuspage; 10 foram
verificados e o comportamento foi o mesmo em todos. O post-mortem é mantido até a última frase, mas as
atualizações publicadas durante o incidente (com data e hora) são descartadas. Em alguns casos elas trazem
informação que o post-mortem não repete (DAN-144: travamento de CPU no hypervisor do GCP; DAN-147: migração
de clientes como mitigação).

**Shortlist da E1.3:** em 5 de 15 candidatos a URL era diferente da do catálogo; em 2 (DAN-115, DAN-169)
apontava para outro incidente. O registro editorial final está correto.

**Escopo:** DAN-141 (vazamento de dados via Salesloft) e DAN-204 (exposição de dados no ChatGPT) são
incidentes de segurança e privacidade. DAN-022 (Etsy) é um artigo técnico em que o outage ocupa um
parágrafo. DAN-191 (King's College) é um relatório de consultoria mais de governança do que técnico.

## Decisões pendentes do time

1. **Tamanho do corpus:** só os 20 aprovados (revisados um a um) ou os ~196 de TI com limpeza automática.
2. **Incidentes de segurança e privacidade:** entram ou não no corpus.

## Para a E1.4

1. Etapa de limpeza depois da extração: manter só o inglês, remover parágrafos repetidos, cortar comentários
   e rodapés.
2. Parser específico para páginas do Statuspage, recuperando título, corpo e data de cada atualização.
3. Buscar outra fonte (ex.: web.archive.org) para as 11 páginas montadas por JavaScript, ou excluí-las.
4. Tratar os PDFs à parte.
5. Se o time quiser o número exato de documentos aproveitáveis: classificar todos os documentos de TI com
   leitura de LLM, com a mesma régua usada nos status pages.

## Limitações desta avaliação

- A amostra foi **estratificada** (escolhida por tipo de alerta e de fonte), não sorteada. Ela mostra que a
  extração é confiável e que o conteúdo é bom, mas **não estima a proporção exata** de documentos
  aproveitáveis entre os 224.
- DAN-091 e DAN-130 foram verificados só quanto à extração; o conteúdo não foi lido.
- Os sites originais não foram acessados nesta avaliação: tudo foi feito a partir do HTML já coletado pelo
  pipeline.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `avaliacao_amostra_danluu.csv` | Avaliação dos 30 documentos: alerta, se procede, correspondência ao catálogo, causa, remediação, config alterada, prevenção, problemas de extração e perdas |
| `extracao_independente.py` | Extração com BeautifulSoup/pdftotext e comparação frase a frase com o JSON do pipeline. Uso: `python extracao_independente.py <pasta com data/raw e data/extracted> <pasta de saída>` |
| `perfil_catalogo.py` | Perfil do `README.md` da danluu: entradas por seção, empresas, domínios, anos e temas. Uso: `python perfil_catalogo.py <README.md da danluu>` |
