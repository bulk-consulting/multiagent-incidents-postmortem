# Gabarito humano — como preencher

Classificação feita **por uma pessoa**, sem consultar avaliações anteriores (E1.3, investigação independente ou LLM). É com este gabarito que a classificação do LLM será medida.

## Passo a passo

1. Abra `gabarito.csv` no Excel ou no Google Sheets.
2. Para cada linha, na ordem, leia o arquivo indicado em `arquivo_texto`.
   - Para a P1, compare o texto com a **descrição do catálogo** no topo do arquivo.
   - Se precisar ver a página original (títulos, imagens), use o caminho em "Arquivo original".
3. Preencha as colunas `p1` a `p9` com **exatamente** um dos valores da régua (`docs/triagem/regua.md`).
   - Se P1 for `nao` ou `nao_verificavel`, deixe P2 a P9 em branco.
4. Em `p10_problemas_leitura`, liste só o que o script não detecta: `sem_conteudo`, `comentarios`, `rodape_marketing`, `pdf_embaralhado`. Separe por `;`. Deixe vazio se não houver.
5. Em `evidencia_p6`, cole o trecho do texto (em inglês) que justifica a resposta da causa.
6. Em `confianca`, use `alta` ou `baixa`.
7. Em `minutos`, anote quanto tempo levou (ajuda a estimar a revisão humana depois).
8. Em `observacoes`, registre dúvidas sobre a régua: são elas que melhoram as definições.

## Valores permitidos (resumo)

| Coluna | Valores |
|---|---|
| `p1_catalogo` | `sim`, `parcial`, `nao`, `nao_verificavel` |
| `p2_autoria` | `primaria`, `secundaria` |
| `p3_tipo` | `postmortem`, `atualizacoes_status`, `relatorio_periodico`, `artigo_tecnico`, `relatorio_formal`, `noticia_enciclopedia`, `outro` |
| `p4_dominio` | `software_servicos`, `infra_fisica_datacenter`, `seguranca`, `fora_de_ti` |
| `p5_seguranca` | `nao`, `exposicao_dados`, `ataque` |
| `p6_causa` | `concreta`, `incerta`, `vaga`, `ausente` |
| `p7_recuperacao` | `especifica`, `generica`, `ausente` |
| `p8_mudanca` | `especifica`, `generica`, `nao_se_aplica`, `ausente` |
| `p9_prevencao` | `especificas`, `genericas`, `ausentes` |

## Regras da régua que mais pesam

- Responda pelo que **está no texto**, não pelo que você sabe do incidente.
- Na dúvida entre duas respostas, escolha a **mais fraca** e marque `confianca = baixa`.
- Não abra `02_gerar_gabarito.py` antes de terminar: ele registra por que cada documento foi escolhido.
