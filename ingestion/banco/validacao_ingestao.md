# Validação da ingestão — 2026-11-05 09:27

## 1. Contagens

| tabela | dataset | tipo | linhas | tokens médios |
|---|---|---|---|---|
| documents | danluu | — | 211 | — |
| chunks | danluu | ficha | 867 | 206 |
| chunks | danluu | texto | 2018 | 297 |

Última carga: 211 documentos e 2885 chunks, modelo Qwen/Qwen3-Embedding-0.6B, em 2026-11-05 09:27, commit babb85e.

## 2. Integridade

| checagem | resultado | esperado |
|---|---|---|
| documentos sem chunk de ficha | 0 ✔ | 0 |
| documentos sem chunk de texto | 0 ✔ | 0 |
| vetores com dimensão diferente de 1024 | 0 ✔ | 0 |
| vetores com norma fora de 1 ± 0,01 | 0 ✔ | 0 |
| chunks sem conteúdo | 0 ✔ | 0 |
| chunks de causa, mitigação ou prevenção sem trechos de evidência | 0 ✔ | 0 |
| documentos sem título, URL ou empresa | 0 ✔ | 0 |

## 3. Amostra de vetores

| chunk | tipo | dimensões | norma | primeiras 5 dimensões |
|---|---|---|---|---|
| danluu:DAN-043:ficha:causa | ficha | 1024 | 0.9998 | -0.0046, -0.0392, -0.0058, -0.0250, +0.0787 |
| danluu:DAN-086:texto:000 | texto | 1024 | 0.9999 | +0.0213, +0.0250, -0.0060, -0.0394, +0.0889 |
| danluu:DAN-189:ficha:resumo | ficha | 1024 | 1.0004 | +0.0268, +0.0518, -0.0073, -0.0126, +0.0429 |

## 4. Perguntas de teste (busca em duas etapas)

**Pergunta:** Todos os servidores do datacenter reiniciaram de uma vez, logo depois de um operador rodar uma ferramenta para reiniciar alguns servidores em manutenção.

Esperado: DAN-189 → posição 1

1. `danluu:DAN-189` (0.648) Joyent — Postmortem for outage of us-east-1 ← esperado
   - ficha (causa): Root cause (concreta): The remote-execution tool did not have enough input validation to prevent a reboot of all servers without extra steps or confirmation, and it issued a reboot command to every server in the us-east-
   - texto, etapa 2 [What Happened?]: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for customer instances 
2. `danluu:DAN-070` (0.626) GitHub — January 28th Incident Report
3. `danluu:DAN-068` (0.610) Cloudflare — Major data center power failure (again): Cloudflare Code Orange tested

**Pergunta:** Acabamos de apagar o banco de dados de produção sem querer, e o último backup é de horas atrás.

Esperado: DAN-043 → posição 1

1. `danluu:DAN-043` (0.672) Keepthescore — We deleted the production database by accident 💥 ← esperado
   - ficha (causa): Root cause (concreta): A function that deletes the local database and recreates all required tables from scratch connected to the production database during late evening coding and wiped it, although its host was hardcod
   - texto, etapa 2 [sem seção]: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  Thankfully our databa
2. `danluu:DAN-164` (0.620) Gitlab — Postmortem of database outage of January 31
3. `danluu:DAN-056` (0.619) TravisCI — Major outage on travis-ci.com

**Pergunta:** Hoje, 29 de fevereiro, desde a meia-noite os certificados estão sendo rejeitados e a criação de novas instâncias falha em toda a plataforma.

Esperado: DAN-086 → posição 1

1. `danluu:DAN-086` (0.551) Azure — Summary of Windows Azure Service Disruption on Feb 29th, 2012 ← esperado
   - ficha (causa): Root cause (concreta): The guest agent calculated the transfer certificate's valid-to date by adding one to the current date's year, so on leap day it set February 29, 2013, an invalid date that made certificate creation
   - texto, etapa 2 [The Leap Day Bug in Action]: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. Storage clusters were
2. `danluu:DAN-015` (0.549) Cloudflare — Cloudflare incident on March 21, 2025
3. `danluu:DAN-090` (0.546) Mozilla — Add-Ons Outage Post-Mortem Result

**Pergunta:** Depois de um deploy, um serviço central passou a responder 401 para todas as requisições e vários produtos que dependem dele estão falhando.

Esperado: DAN-017 → posição 3

1. `danluu:DAN-050` (0.606) rust-lang — crates.io Postmortem: Broken Crate Downloads
   - ficha (mitigacao): Mitigation steps: 1. The deploying developer rolled back to the previous deployment through the Heroku user interface (taking about one minute); the deployment was rolled back at 12:30 UTC and the system immediately prod
   - texto, etapa 2 [Response / Recovery]: ## Response  After the incident was detected, the deploying developer immediately initiated a rollback to the previous deployment through the Heroku user interface. This process took about one minute due to the login pro
2. `danluu:DAN-220` (0.598) Spotify — Incident Management at Spotify
3. `danluu:DAN-017` (0.594) Cloudflare — Cloudflare incident on October 30, 2023 ← esperado

Incidente esperado no top-3: 4 de 4 perguntas.

## 5. Avaliação completa (índice de fichas, Qwen3)

| recorte | perguntas | 1º lugar | top-5 |
|---|---|---|---|
| todas | 278 | 72% | 88% |
| sintoma em português | 60 | 67% | 83% |
| sintoma, difíceis | 52 | 54% | 79% |

Detalhes em ingestion/avaliacao/RESULTADOS.md.

**Resultado:** todas as checagens de integridade passaram.
