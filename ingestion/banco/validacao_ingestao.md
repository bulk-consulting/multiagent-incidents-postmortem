# Validação da ingestão — 2026-11-09 15:22

## 1. Contagens

| tabela | dataset | tipo | linhas | tokens médios |
|---|---|---|---|---|
| documents | danluu | — | 212 | — |
| chunks | danluu | ficha | 867 | 206 |
| chunks | danluu | resumo | 212 | 88 |
| chunks | danluu | texto | 2024 | 297 |

Última carga: 212 documentos e 3103 chunks, modelo Qwen/Qwen3-Embedding-0.6B, em 2026-11-09 15:22, commit 073fa50.

## 2. Integridade

| checagem | resultado | esperado |
|---|---|---|
| documentos sem chunk de resumo | 0 ✔ | 0 |
| documentos sem chunk de texto | 0 ✔ | 0 |
| vetores com dimensão diferente de 1024 | 0 ✔ | 0 |
| vetores com norma fora de 1 ± 0,01 | 0 ✔ | 0 |
| chunks sem conteúdo | 0 ✔ | 0 |
| chunks de causa, mitigação ou prevenção sem trechos de evidência | 0 ✔ | 0 |
| chunks de resumo diferentes do resumo do documento | 0 ✔ | 0 |
| documentos sem título, URL ou empresa | 0 ✔ | 0 |

## 3. Amostra de vetores

| chunk | tipo | dimensões | norma | primeiras 5 dimensões |
|---|---|---|---|---|
| danluu:DAN-043:texto:000 | texto | 1024 | 1.0000 | -0.0072, -0.0155, -0.0104, -0.0473, +0.0818 |
| danluu:DAN-086:ficha:mitigacao | ficha | 1024 | 0.9998 | +0.0343, +0.0096, -0.0060, -0.0574, +0.1083 |
| danluu:DAN-189:resumo | resumo | 1024 | 0.9999 | +0.0079, +0.0226, -0.0104, -0.0400, +0.0386 |

## 4. Perguntas de teste (busca em duas etapas)

**Pergunta:** Todos os servidores do datacenter reiniciaram de uma vez, logo depois de um operador rodar uma ferramenta para reiniciar alguns servidores em manutenção.

Esperado: DAN-189 → posição 1

1. `danluu:DAN-189` (0.671) Joyent — Postmortem for outage of us-east-1 ← esperado
   - resumo: An operator used a tool with lax input validation to reboot a small number of servers undergoing maintenance but forgot to type `-n` and instead rebooted all servers in the datacenter. This caused an outage that lasted 2
   - achado pelo chunk de resumo
   - texto, etapa 2 [What Happened?]: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for customer instances 
2. `danluu:DAN-103` (0.653) Allegro — Post-mortem report on 23-24, October 2014 failure
3. `danluu:DAN-070` (0.637) GitHub — January 28th Incident Report

**Pergunta:** Acabamos de apagar o banco de dados de produção sem querer, e o último backup é de horas atrás.

Esperado: DAN-043 → posição 1

1. `danluu:DAN-043` (0.723) Keepthescore — We deleted the production database by accident 💥 ← esperado
   - resumo: Engineers deleted the production database by accident. Database is a managed database from DigitalOcean with backups once a day. 30 minutes after the disaster, it went back online, however 7 hours of scoreboard data was 
   - achado pelo chunk de resumo
   - texto, etapa 2 [sem seção]: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  Thankfully our databa
2. `danluu:DAN-146` (0.676) Dropbox — Outage post-mortem
3. `danluu:DAN-056` (0.655) TravisCI — Major outage on travis-ci.com

**Pergunta:** Hoje, 29 de fevereiro, desde a meia-noite os certificados estão sendo rejeitados e a criação de novas instâncias falha em toda a plataforma.

Esperado: DAN-086 → posição 1

1. `danluu:DAN-086` (0.616) Azure — Summary of Windows Azure Service Disruption on Feb 29th, 2012 ← esperado
   - resumo: Certificates that were valid for one year were created. Instead of using an appropriate library, someone wrote code that computed one year to be the current date plus one year. On February 29th 2012, this resulted in the
   - achado pelo chunk de resumo
   - texto, etapa 2 [The Leap Day Bug in Action]: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. Storage clusters were
2. `danluu:DAN-103` (0.558) Allegro — Post-mortem report on 23-24, October 2014 failure
3. `danluu:DAN-015` (0.554) Cloudflare — Cloudflare incident on March 21, 2025

**Pergunta:** Depois de um deploy, um serviço central passou a responder 401 para todas as requisições e vários produtos que dependem dele estão falhando.

Esperado: DAN-017 → fora do top-3

1. `danluu:DAN-220` (0.631) Spotify — Incident Management at Spotify
   - resumo: Lack of exponential backoff in a microservice caused a cascading failure, leading to notable service degradation.
   - achado pelo chunk de resumo
   - texto, etapa 2 [The night of April 27th]: ## The night of April 27th  It was a rainy Saturday night in Stockholm. Some of our engineers were online on IRC, and discovered that Popcount was unhealthy again. We thought the fast fail logic we introduced in Popcount
2. `danluu:DAN-067` (0.611) Cloudflare — Post mortem on the Cloudflare Control Plane and Analytics Outage
3. `danluu:DAN-211` (0.601) Roblox — Roblox Return to Service

Incidente esperado no top-3: 3 de 4 perguntas.

## 5. Avaliação completa (índice resumo+texto, Qwen3)

| recorte | perguntas | 1º lugar | top-5 |
|---|---|---|---|
| todas | 278 | 73% | 92% |
| sintoma em português | 60 | 62% | 92% |
| sintoma, difíceis | 52 | 58% | 88% |

Detalhes em ingestion/avaliacao/RESULTADOS.md.

**Resultado:** todas as checagens de integridade passaram.
