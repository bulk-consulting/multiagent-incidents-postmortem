# Plano de extração em lotes

## Escopo

Lista completa em [`lotes/lotes.csv`](lotes/lotes.csv): **169 documentos em 17 lotes de 10** (o último tem 9).

| Lote | Conteúdo |
|---|---|
| 00 | As 10 fichas do [gabarito](gabarito/LEIAME.md): teste de regressão do prompt |
| 01–16 | 159 documentos com qualidade `ok` ou `precisa_limpeza` no [inventário](../triagem/saida/inventario.csv), em ordem sorteada (semente 42) para misturar empresas e tipos |

**Ficam de fora por enquanto (71):** 27 `inutilizavel`, 40 `precisa_reextracao` e 4 com lista perdida dentro de tabela (DAN-035, 040, 058, 072, achadas a partir da DAN-166). Voltam depois da reextração.

Observações:
- `precisa_limpeza` (7) entra: são textos repetidos em outro idioma ou parágrafos repetidos. Desde o lote 05, o `montar_prompts.py` remove do prompt os parágrafos em escrita não latina (quando sobra texto latino suficiente) e os parágrafos longos repetidos; só remove parágrafos inteiros, então os trechos continuam batendo com o texto original no validador. Age em DAN-002, 060, 062, 064, 111, 113, 114 e 155 (DAN-002 tem a versão em inglês depois do coreano). Cópias em outro idioma de escrita latina (o português da DAN-063) não são removidas.
- DAN-216 tem 2 palavras e o inventário a marcou `ok` por engano; o esperado é `catalogo: nao_verificavel`.
- DAN-210 tem 4.501 palavras, mas são só menus, cabeçalhos de comentários e rodapé do Reddit; saiu `nao_verificavel` no lote 03. DAN-156 (lote 04) trouxe só a página do Hacker News com um comentário. DAN-150 (lote 11) trouxe só a página índice do blog. DAN-034 e DAN-209 (lote 16) trouxeram só título e navegação do blog e do Reddit. DAN-202 (lote 13) trouxe a página da EPA sobre a licença da usina Merrimack (o PDF do catálogo redireciona), sem nada do apagão de 2003. A contagem de palavras do inventário não detecta páginas sem artigo: as sete vão para a reextração.

## Cada lote

1. **Montar os prompts** (Claude ou André):
   `multiagent_env/bin/python ingestion/fichas/montar_prompts.py --lote NN`
2. **Extrair numa sessão NOVA do Claude Code** (André), com o texto abaixo. Nunca nesta sessão de desenho do prompt, que conhece o gabarito.
3. **Validar** (Claude): `validar_fichas.py` nas fichas do lote; contagem de `alta`/`baixa`.
4. **Lote 00:** comparar com o gabarito (`comparar_fichas.py ingestion/fichas/saida_lotes/lote_00`). Se a concordância ficar perto da do 2º teste (≥ 93%) e as divergências forem de fronteira, seguir. Se não, ajustar o prompt antes do lote 01.
5. **Conferência no GPT (primeiros lotes)**: `montar_revisao.py NN` gera `revisao/lote_NN/`. Um chat novo por ficha, com 2 anexos (`prompt_extracao.md` e `DAN-xxx_revisao.md`) e a frase: *"Siga as instruções do arquivo DAN-xxx_revisao.md."* André cola as respostas; Claude separa o que procede, corrige a ficha e, se for falha de regra, propõe ajuste no prompt.
6. **Aceitar**: fichas conferidas e corrigidas são copiadas para `saida/`.

**Até quando conferir tudo no GPT:** decidido após o lote 03 (ERRADOS procedentes por ficha: 2,6 no lote 01, 2,1 no 02, 1,5 no 03): conferir todas as fichas até o lote 05. Se os lotes 04 e 05 ficarem abaixo de 1 ERRADO procedente por ficha, passar a conferir só as `baixa` + 4 `alta` sorteadas por lote, voltando a conferir tudo se a amostra piorar.

**A partir do lote 06 (decidido após o lote 05, taxa estável em ~1,5 ERRADO por ficha desde o lote 03):**
- a sessão de extração faz uma **autorrevisão** ([`autorrevisao.md`](autorrevisao.md)) depois de validar, e lista o que mudou em cada ficha;
- a conferência no GPT é por **amostra**: as fichas `baixa` + 3 `alta` sorteadas + as que a autorrevisão passou de `baixa` para `alta` (`montar_revisao.py NN --amostra DAN-xxx ...`; desde o lote 08);
- se a amostra passar de 1,5 ERRADO procedente por ficha, volta a conferir tudo no lote seguinte.

Resultado da amostra por lote (ERRADOS procedentes / fichas da amostra): lote 06 = 6/6 (1,0) → segue por amostra; gerou a v2.13. Lote 07 = 5/5 (1,0), 4 dos 5 por detalhe sem trecho → segue por amostra, sem mudança de prompt.
Lote 08 = 6/5 (1,2), amostra ampliada com as 2 fichas que a autorrevisão passou de baixa para alta (124, 240; a 197 já tinha sido sorteada): nenhuma das 3 viradas foi contestada → segue por amostra, sem mudança de prompt.
Lote 09 = 4/7 (0,6) → segue por amostra; gerou a v2.14 (regra de duração que só existia no lembrete da revisão).
Lote 10 = 6/5 (1,2), amostra com 3 sorteadas + 2 escolhidas (157, 187), todas alta → segue por amostra, sem mudança de prompt.
Lote 11 = 5/6 (0,8) → segue por amostra, sem mudança de prompt. DAN-150 saiu nao_verificavel (página índice do blog): reextração.
Lote 12 = 7/7 (1,0) → segue por amostra; gerou a v2.15 (configuration-error sem mudança recente).
Lote 13 = 8/6 (1,3) + 1 fora da amostra (duração da DAN-013) → segue por amostra; gerou a v2.16. DAN-202 saiu catalogo nao (página errada da EPA): reextração.
Lote 14 = 6/6 (1,0) → segue por amostra, sem mudança de prompt.
Lote 15 = 10/6 (1,7) + 2 fora da amostra (ano deduzido em DAN-086 e 195) → passou de 1,5: o lote 16 volta a ser conferido inteiro.
Lote 16 = 5/7 (0,7), conferido inteiro (as 7 fichas com incidente; DAN-034 e 209 saíram nao_verificavel) → extração do plano concluída.

**Fichas vazias:** documentos que saem `nao_verificavel` (só menus ou rodapé) não precisam de conferência; entram na lista de reextração.

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
- Depois que o validador passar, faça a autorrevisão: leia ingestion/fichas/autorrevisao.md
  (pode abrir esse arquivo) e siga o checklist dele em cada ficha, uma por vez, conferindo contra
  o próprio prompt pronto. Rode o validador de novo e, no resumo final, diga o que mudou em cada ficha.
  No fim do resumo, liste numa linha as fichas cuja confianca mudou na autorrevisão (ex.: "baixa→alta: DAN-x, DAN-y").
```

## Revisão das fichas antigas (2026-11-04)

As 70 fichas geradas antes da v2.13 foram relidas só nos campos que as regras novas mudaram (detecção `equipe_interna`, duração, `software-bug` residual, mudança causadora, motivos de `baixa`). Mudei 4; a conferência no GPT derrubou 2, que voltaram ao valor anterior: DAN-179 ("the worst of its impact lasted 4 hours" não diz quando o serviço voltou: duração `null`) e DAN-111 (há mais de uma recuperação parcial com horário: continua `baixa`). Ficaram 2, com o motivo em `observacoes` ("Revised on 2026-11-04 under prompt v2.17 rules"): DAN-217 (detecção `nao_informada`, duração 14) e DAN-062 (`baixa` pela duração, como DAN-106). As correções foram feitas em `saida/`; as cópias em `saida_lotes/` ficam como histórico da extração. Conferência das 4 no GPT: `montar_revisao.py saida --amostra DAN-062 DAN-111 DAN-179 DAN-217`.

Depois dessa conferência veio a v2.18 (regra de volta parcial mais estrita; fim ambíguo dá duração `null` sem baixar a confiança). Com ela, DAN-062, 106 e 111 passaram de `baixa` para `alta`, com duração `null` e os horários candidatos em `observacoes`.
