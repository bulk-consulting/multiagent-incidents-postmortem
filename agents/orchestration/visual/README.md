# Replay visual de uma investigação

Uma página que mostra, com animação, uma investigação real passando pelo grafo: o nó que está trabalhando acende,
a seta por onde o fluxo passou fica marcada, um painel diz o que o agente fez (buscas, comparações do Diagnóstico,
regra que escolheu o próximo nó) e a coluna do estado compartilhado acende cada campo quando ele é escrito.

É um **replay**: reproduz uma execução gravada. Não chama o modelo nem o banco, então sempre roda igual (bom para
apresentar). Cada página é um arquivo HTML só, com os dados dentro: basta abrir no navegador, sem servidor e sem
internet.

## Abrir

No Windows, cole o caminho na barra do navegador (ou rode `explorer.exe <arquivo>` no WSL):

```
\\wsl.localhost\Ubuntu\home\andre\bulk_projetos\treinamento_dell\agents\orchestration\visual\replay_dan104.html
```

| Página | O que mostra |
|---|---|
| `replay_dan104.html` | o caminho direto: a Triagem pergunta → pausa → resposta → Pesquisa acha o post-mortem do S3 → Diagnóstico `high` → Relatório |
| `replay_dan197.html` | o caminho mais completo: pergunta da Triagem → 3 rodadas de busca sem evidência (laço de nova busca) → o Diagnóstico pergunta ao analista → a investigação recomeça → a busca acha o post-mortem certo → Relatório |
| `replay_dan104_detalhe.html`, `replay_dan197_detalhe.html` | os mesmos casos, abrindo também o que acontece **dentro** de cada agente (veja abaixo) |

## Replay detalhado (dentro dos nós)

Nos arquivos `_detalhe`, quando o fluxo entra num agente, a área do grafo se divide: o grafo principal encolhe à
esquerda (com o nó ativo aceso) e, à direita, aparece **“Dentro do nó”**, um mini-grafo com os passos daquele agente,
que acendem do mesmo jeito:

| Agente | Passos internos |
|---|---|
| Triagem | modelo lê a mensagem → ferramenta `list_investigations` → modelo compara → resultado validado (sem serviço: vai direto às perguntas) |
| Pesquisa | busca em código (texto do analista) → modelo busca (`find_similar_incidents`, pode repetir: contador “chamada N”) → modelo aprofunda (`search_inside_incidents`) → monta os achados |
| Diagnóstico | monta o texto → modelo escreve as hipóteses e as 3 comparações → validação (JSON e IDs; se falhar, corrige) → `decide()` |
| Relatório | monta o texto → modelo escreve → conferência em código (fontes, links, causas = hipóteses; se falhar, corrige) → relatório |

Na pausa para o analista e no início e no fim, o grafo volta a ocupar a área toda. No DAN-197 dá para ver o problema
do Pesquisa: o fluxo fica girando em “Modelo busca” (chamadas 1 a 4) e nunca desce para “Modelo aprofunda”.

Controles: Play/Pausa, passo a passo (◀ ▶ ou as setas do teclado), velocidade (0,5× a 4×) e a barra para pular
para qualquer ponto. A página cabe numa tela (testada em 1366×768 e 1920×1080).

## Gerar o replay de outra investigação

1. Gravar a investigação (grafo real, modelo real; o analista é simulado com as respostas do caso):

   ```bash
   multiagent_env/bin/python -I agents/orchestration/experiments/capture_walkthrough.py dan104   # ou dan197
   # → agents/orchestration/experiments/results/walkthrough_<caso>_<data>.json
   ```

2. Gerar a página:

   ```bash
   multiagent_env/bin/python -I agents/orchestration/visual/build_replay.py \
       agents/orchestration/experiments/results/walkthrough_<caso>_<data>.json
   # → agents/orchestration/visual/replay_<caso>.html
   # com --detail no fim: o replay detalhado → replay_<caso>_detalhe.html
   ```

Para um caso novo, acrescente a mensagem inicial e a resposta do analista em `SCENARIOS` no
`capture_walkthrough.py` (e o id do caso em `CASE_IDS`, de onde vêm as respostas às perguntas do Diagnóstico).

## Arquivos

| Arquivo | O que é |
|---|---|
| `build_replay.py` | lê uma gravação e a transforma em "quadros" (um momento da animação cada), embutidos na página |
| `replay_template.html` | o desenho do grafo (SVG), o painel, o estado, os controles e a animação; fontes do sistema, sem bibliotecas |
| `replay_detail_template.html` | o mesmo, mais os mini-grafos de dentro de cada agente e o zoom (usado com `--detail`) |
| `replay_*.html` | as páginas geradas |

## Limites

- Mostra só execuções gravadas. Uma versão **ao vivo** (a página acompanhando a investigação enquanto ela roda) pede
  um endpoint na API que repasse os eventos do grafo ao navegador; fica como próximo passo, junto com a tela da E6.
- O analista simulado escolhe as respostas por palavras-chave: na gravação do DAN-197, a resposta à pergunta do
  Diagnóstico foi fraca (repetiu o serviço), e o acerto depois do recomeço veio da busca nova, que desta vez usou
  palavras mais próximas do post-mortem certo.
