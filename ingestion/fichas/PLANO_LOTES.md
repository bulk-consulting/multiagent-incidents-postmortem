# Plano de extração em lotes

## Escopo

Lista completa em [`lotes/lotes.csv`](lotes/lotes.csv): **169 documentos em 17 lotes de 10** (o último tem 9).

| Lote | Conteúdo |
|---|---|
| 00 | As 10 fichas do [gabarito](gabarito/LEIAME.md): teste de regressão do prompt |
| 01–16 | 159 documentos com qualidade `ok` ou `precisa_limpeza` no [inventário](../triagem/saida/inventario.csv), em ordem sorteada (semente 42) para misturar empresas e tipos |

**Ficam de fora por enquanto (71):** 27 `inutilizavel`, 40 `precisa_reextracao` e 4 com lista perdida dentro de tabela (DAN-035, 040, 058, 072, achadas a partir da DAN-166). Voltam depois da reextração.

Observações:
- `precisa_limpeza` (7) entra: são textos repetidos em outro idioma ou trechos repetidos, que a ficha resolve (o extrator cita a parte em inglês; ver DAN-063). DAN-002 está só em coreano.
- DAN-216 tem 2 palavras e o inventário a marcou `ok` por engano; o esperado é `catalogo: nao_verificavel`.

## Cada lote

1. **Montar os prompts** (Claude ou André):
   `multiagent_env/bin/python ingestion/fichas/montar_prompts.py --lote NN`
2. **Extrair numa sessão NOVA do Claude Code** (André), com o texto abaixo. Nunca nesta sessão de desenho do prompt, que conhece o gabarito.
3. **Validar** (Claude): `validar_fichas.py` nas fichas do lote; contagem de `alta`/`baixa`.
4. **Lote 00:** comparar com o gabarito (`comparar_fichas.py ingestion/fichas/saida_lotes/lote_00`). Se a concordância ficar perto da do 2º teste (≥ 93%) e as divergências forem de fronteira, seguir. Se não, ajustar o prompt antes do lote 01.
5. **Conferência no GPT (primeiros lotes)**: `montar_revisao.py NN` gera `revisao/lote_NN/`. Um chat novo por ficha, com 2 anexos (`prompt_extracao.md` e `DAN-xxx_revisao.md`) e a frase: *"Siga as instruções do arquivo DAN-xxx_revisao.md."* André cola as respostas; Claude separa o que procede, corrige a ficha e, se for falha de regra, propõe ajuste no prompt.
6. **Aceitar**: fichas conferidas e corrigidas são copiadas para `saida/`.

**Até quando conferir tudo no GPT:** nos primeiros lotes, todas as 10. Quando dois lotes seguidos tiverem no máximo 1 ERRADO procedente no lote inteiro, passar a conferir só as `baixa` + 2 `alta` sorteadas por lote.

**Mudança de prompt no meio:** se um lote levar a uma nova versão do prompt, os lotes seguintes usam a nova; as fichas já aceitas não são refeitas (o `versao_prompt` registra com qual foram geradas). Antes de seguir, rodar o lote 00 de novo se a mudança for grande.

## Texto para a sessão de extração

Trocar `NN` pelo número do lote:

```
Tarefa de extração. Para cada arquivo em ingestion/fichas/prompts_prontos/lote_NN/:

1. Leia o arquivo inteiro. Ele contém as instruções e o documento a analisar.
2. Siga as instruções dele exatamente e produza o JSON pedido.
3. Grave o JSON em ingestion/fichas/saida_lotes/lote_NN/DAN-xxx.json (mesmo número do arquivo).
   No campo extracao.modelo use o nome do seu modelo + " (Claude Code)".

Regras desta tarefa:
- Use SOMENTE os arquivos de prompts_prontos/lote_NN/.
- NÃO abra nada em ingestion/fichas/gabarito/, ingestion/fichas/saida/, ingestion/fichas/saida_teste*/,
  ingestion/fichas/saida_lotes/ (fora do lote_NN), revisao/, nem outros arquivos do projeto.
- Faça um documento por vez, sem comparar um com o outro.
- No fim, rode:
  multiagent_env/bin/python ingestion/fichas/validar_fichas.py ingestion/fichas/saida_lotes/lote_NN/DAN-*.json
  Se algum trecho falhar, corrija só aquela ficha contra o próprio prompt pronto e rode de novo.
```
