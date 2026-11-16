# Dan Luu post-mortem ingestion

Pipeline independente e auditável para coletar, extrair e revisar o catálogo de
post-mortems do Projeto 4. O projeto não altera o repositório `post-mortems` e
não implementa chunking, embeddings nem banco vetorial.

## Preparação

Requer Python 3.12. A partir deste diretório:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
pytest
```

As opções de `.env.example` são exemplos para exportação no shell; o projeto
não carrega arquivos `.env` implicitamente nem adiciona essa dependência.

O catálogo em `data/catalog.csv` é uma cópia integral dos 240 registros de
`/tmp/danluu_catalog.csv` no momento da criação deste projeto.

## Fluxo

Sempre comece com uma amostra pequena. O modo `--test` não acessa a rede:

```bash
python scripts/collect.py --limit 5 --test
python scripts/collect.py --limit 5
python scripts/extract.py
python scripts/validate.py
python scripts/report.py
```

Todos os comandos de processamento aceitam `--catalog-id DAN-001` (repetível).
A coleta retoma por padrão e não baixa novamente manifestos bem-sucedidos;
`--no-resume` força uma nova tentativa. A extração também oferece
`--no-resume`.

Depois da inspeção humana do JSON extraído e do conteúdo bruto, registre a
decisão no cadastro editorial independente:

```bash
python scripts/editorial_review.py decide \
  --catalog-id DAN-001 \
  --decision approved \
  --reviewed-by "nome-ou-identificador" \
  --reviewed-at 2026-10-28T15:00:00Z
```

Também é possível registrar `--decision rejected`. Uma decisão final existente
não é substituída sem `--revise-existing`, que representa uma ação explícita de
revisão. Cada alteração preserva automaticamente a versão anterior em
`data/reviews/backups/` e substitui o CSV de forma atômica.

`data/reviews/editorial_reviews.csv` é a fonte de verdade para decisões
editoriais. Um documento é elegível ao futuro corpus RAG somente quando possui
`editorial_decision=approved`, `reviewed_by` não vazio e `reviewed_at` válido em
UTC. Pendentes e rejeitados nunca são elegíveis. Consultar e validar o registro
não altera os JSONs extraídos nem o campo legado `editorial_approved`:

```bash
python scripts/validate_reviews.py
python scripts/editorial_review.py eligible
```

## Dados e estados

- `data/raw/`: HTML/PDF original e um manifesto JSON por item.
- `data/extracted/`: texto legível, metadados, heurísticas e motivos de revisão.
- `data/reports/summary.json`: totais e distribuições agregadas.
- `data/reports/documents.csv`: índice por documento para auditoria.

Os estados técnicos/editoriais são `pending`, `fetched`, `extracted`,
`needs_review`, `failed`, `skipped` e `approved`. Falhas ficam isoladas no
manifesto e não interrompem o lote. Campos desconhecidos permanecem `null`.

## Segurança e comportamento de rede

O coletor aceita somente HTTP/HTTPS, resolve o host antes de cada requisição e
rejeita localhost, credenciais na URL e qualquer IP não global. A mesma regra é
aplicada a cada salto de redirecionamento. Há timeout, retries com backoff,
limite por domínio, `robots.txt`, limite de redirecionamentos e máximo de 10 MiB
por download (configurável). Apenas HTML/XHTML e PDF são armazenados.

Redirecionamentos HTTP e elementos HTML `meta http-equiv="refresh"` usam o
mesmo contador e a mesma detecção de ciclos. Um meta refresh só é seguido
quando possui uma única URL explícita e válida; URLs relativas são resolvidas
contra a URL final da resposta. Cada salto fica em `redirect_history`, com
origem, destino, tipo e resultado. O HTML intermediário é preservado como
`CATALOG_ID.redirect-NNN.html`, inclusive em novas execuções, antes que o
conteúdo final ocupe o caminho principal. Instruções inválidas, ambíguas,
inseguras, acima do limite ou bloqueadas por `robots.txt` não são seguidas.

Para impedir DNS rebinding entre validação e conexão, o transporte padrão fixa
a conexão nos IPs públicos retornados pela resolução validada, mantendo o
hostname original para HTTP e TLS/SNI. Proxies do ambiente não são usados. A
garantia pertence ao cliente padrão; clientes HTTP injetados são destinados
somente aos testes controlados.

O coletor não executa JavaScript nem interpreta redirecionamentos em scripts.
Ao retomar, um manifesto antigo em revisão cujo HTML bruto seja um meta refresh
válido continua a partir do destino sem baixar novamente a origem.
`--no-resume` refaz o fluxo, preservando intermediários sob novos nomes.

O User-Agent deve ser ajustado em `DANLUU_USER_AGENT` para conter um contato
real antes da coleta. O pipeline não tenta contornar CAPTCHA, autenticação,
paywall ou bloqueios; esses conteúdos são sinalizados para revisão.

Uma limitação deliberada da primeira versão é o processamento sequencial. A
validação de qualidade e os sete indicadores de completude são heurísticas:
eles não confirmam factualidade nem transformam hipóteses em causas provadas.

A extração preserva legendas e referências textuais a gráficos quando elas
existem no HTML, mas não interpreta imagens nem recupera valores presentes
somente dentro delas. Isso se aplica, por exemplo, aos gráficos citados no
DAN-134; qualquer análise visual continua sendo uma etapa de revisão manual.

## Testes

Os testes usam transporte HTTP simulado e fixtures locais, sem depender de
sites externos. Cobrem catálogo, metadados, HTML/PDF, retry e falhas HTTP,
conteúdo inválido, duplicatas, retomada, limite de download e bloqueio de URLs
internas inclusive após redirecionamento.
Também cobrem meta refresh absoluto e relativo, variações de sintaxe, instrução
ausente/inválida/ambígua, SSRF, `robots.txt`, ciclos, limite compartilhado,
histórico no manifesto, preservação do intermediário, retomada e DNS pinning.
