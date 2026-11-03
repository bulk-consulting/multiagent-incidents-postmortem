# Gabarito das fichas

As 10 fichas desta pasta foram **revisadas**: cada uma foi conferida por outro modelo (ChatGPT, chat novo por ficha, com o prompt, o original e a ficha), e as críticas que procediam foram corrigidas à mão. Servem de referência para medir o prompt.

**Não editar** estas fichas para acompanhar mudanças do prompt. Elas são o padrão; quem muda é o prompt.

## Como ler

- O campo `extracao.versao_prompt` diz com qual versão a ficha **foi gerada**. O conteúdo inclui correções feitas depois da revisão, alinhadas à versão em `corrigida_ate` de [`revisoes.csv`](revisoes.csv).
- Não há campo `revisada` no JSON porque o schema não aceita campos extras. A marcação é este LEIAME e o `revisoes.csv`.

## Cobertura

| Caso | Fichas |
|---|---|
| Post-mortem primário de software | 053, 164, 169, 183 |
| Status page (`atualizacoes_status`, `misto`) | 166 |
| Fonte secundária (`artigo_tecnico`, `noticia_enciclopedia`) | 024, 046 |
| Ataque (`seguranca`) | 152 |
| Relatório periódico | 027 |
| Falha física de datacenter (`hardware-power`) | 063 |
| Fora de TI, `catalogo: parcial` | 046 |
| `gatilho: null` | 024, 027, 183 |
| `perguntas_em_aberto` preenchido | 063 |

Desde a v2.7, 9 têm `confianca: alta` e 1 tem `baixa` (024): `baixa` só quando as regras deixam dois valores possíveis num campo. As notas que não são escolhas ficam em `observacoes`.

## Uso: teste de regressão

1. Gerar as 10 de novo com o prompt atual, sem olhar esta pasta, em outra pasta de saída.
2. Comparar campo a campo com estas: `multiagent_env/bin/python ingestion/fichas/comparar_fichas.py <pasta_gerada>`.
3. Divergências apontam regras ambíguas no prompt.
