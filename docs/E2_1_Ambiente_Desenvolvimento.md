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

Instalar (só na primeira vez, ou quando o `requirements.txt` mudar):

```bash
pip install -r ./requirements.txt
```

## 3. PostgreSQL + pgvector

Abrir o Docker Desktop e esperar ele iniciar. Depois, subir o banco:

```bash
docker compose up -d
```

Para parar (os dados continuam salvos no volume `pgdata`):

```bash
docker compose down
```

## 4. Verificar se o banco está ativo

Ver o estado do contêiner (deve aparecer `healthy`):

```bash
docker compose ps
```

Confirmar que a extensão pgvector está instalada (deve retornar a versão, por exemplo `0.8.7`):

```bash
docker exec incident-copilot-db psql -U copilot -d incident_copilot -c "SELECT extversion FROM pg_extension WHERE extname = 'vector';"
```

## Dados de conexão

| Campo | Valor |
|---|---|
| Host | `localhost` |
| Porta | `5432` |
| Banco | `incident_copilot` |
| Usuário | `copilot` |
| Senha | `copilot` |

Os mesmos valores estão em `.env.example`.
