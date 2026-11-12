# E2.1 — Ambiente de Desenvolvimento

Instruções para preparar e iniciar o ambiente local no Windows (Git Bash), a partir da raiz do projeto.

## Pré-requisitos

- Python 3.11
- Docker Desktop
- Microsoft Visual C++ Redistributable 14.44 ou superior (necessário para o PyTorch): <https://aka.ms/vs/17/release/vc_redist.x64.exe>

## 1. Ambiente virtual

Criar (só na primeira vez):

```bash
python -m venv .venv
```

Ativar (toda vez que abrir um terminal novo):

```bash
source .venv/Scripts/activate
```

O terminal passa a mostrar `(.venv)` no início da linha.

## 2. Dependências

Sem GPU NVIDIA, instalar antes o PyTorch só para processador (bem menor que a versão com CUDA):

```bash
pip install torch==2.15.0 --index-url https://download.pytorch.org/whl/cpu
```

Instalar o resto (só na primeira vez, ou quando o `requirements.txt` mudar):

```bash
pip install -r ./requirements.txt
```

O modelo de embeddings (`Qwen/Qwen3-Embedding-0.6B`, ~1,2 GB) é baixado do Hugging Face na primeira execução de `embed.py` ou `search.py`.

## 3. Configuração (`.env`)

As senhas ficam no arquivo `.env`, que não vai para o Git. Criar a partir do exemplo (só na primeira vez) e trocar a senha em `POSTGRES_PASSWORD` e em `DATABASE_URL`:

```bash
cp .env.example .env
```

## 4. PostgreSQL + pgvector

Abrir o Docker Desktop e esperar ele iniciar. Depois, subir o banco:

```bash
docker compose up -d
```

O `docker-compose.yml` usa a imagem `pgvector/pgvector:0.8.7-pg17` (versão fixa), o banco só aceita conexões da própria máquina (`127.0.0.1`) e o contêiner volta sozinho depois de reiniciar o Docker ou o computador.

Para parar (os dados continuam salvos no volume `pgdata`):

```bash
docker compose down
```

## 5. Verificar se o banco está ativo

Ver o estado do contêiner (deve aparecer `healthy`):

```bash
docker compose ps
```

Confirmar que a extensão pgvector está instalada (deve retornar `0.8.7`):

```bash
docker exec incident-copilot-db psql -U copilot -d incident_copilot -c "SELECT extversion FROM pg_extension WHERE extname = 'vector';"
```

## Dados de conexão

| Campo | Valor |
|---|---|
| Host | `localhost` (só a própria máquina) |
| Porta | `5432` |
| Banco | `POSTGRES_DB` do `.env` (`incident_copilot`) |
| Usuário | `POSTGRES_USER` do `.env` (`copilot`) |
| Senha | `POSTGRES_PASSWORD` do `.env` |

Os scripts leem a conexão de `DATABASE_URL`, no mesmo `.env`.
