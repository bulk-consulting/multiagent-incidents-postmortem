# Conferência das respostas: prompt v1 × v2 (2026-11-11)

## O que foi testado

As 12 perguntas de [perguntas.json](../perguntas.json) rodaram **3 vezes com cada versão do system prompt**. Todas as rodadas usaram 4 trechos por incidente e o mesmo modelo (`openai/gpt-oss-20b` no NIM, `temperature=1.0`). Ao todo, são 72 respostas.

| rodada | prompt | arquivo |
|---|---|---|
| v1a | v1 | [2026-11-11_1733](2026-11-11_1733.md) |
| v1b | v1 | [2026-11-11_1848](2026-11-11_1848.md) |
| v1c | v1 | [2026-11-11_1920](2026-11-11_1920.md) |
| v2a | v2 | [2026-11-11_1802](2026-11-11_1802.md) |
| v2b | v2 | [2026-11-11_1904](2026-11-11_1904.md) |
| v2c | v2 | [2026-11-11_1938](2026-11-11_1938.md) |

As duas versões do prompt estão em [rag/prompts.py](../../prompts.py), em `SISTEMA_V1` e `SISTEMA_V2`. A v2 traz quatro mudanças:
- **Proíbe contas e generalizações.** Não aceita cálculos, comparações, estimativas nem generalizações que não estejam no texto.
- **Manda admitir o que falta.** Se a causa ou a correção não está no contexto, a resposta deve dizer que não está descrita, em vez de deduzir.
- **Pede português correto.** Também proíbe emojis.
- **Não repete metadados no texto.** Os IDs e o nível de evidência ficam só nos campos da ferramenta.

Para repetir o teste:

```bash
multiagent_env/bin/python -I rag/avaliacao/avaliar_qualitativo.py --trechos 4 --prompt v1   # ou v2
```

## Como foi conferido

Li as 72 respostas. Cada afirmação que levantou dúvida foi procurada no **contexto exato que o modelo recebeu**. A busca devolve sempre o mesmo resultado para a mesma pergunta, então o contexto foi o mesmo nas 6 rodadas. A classificação abaixo é leitura humana, não uma métrica automática:

- **Invenção:** o fato não está no contexto.
- **Leitura errada:** o fato está no contexto, mas a resposta o troca, distorce ou atribui a quem não é.
- **Formatação:** ruído no texto que não muda o conteúdo.

## Resumo

| | v1 (3 rodadas) | v2 (3 rodadas) |
|---|---|---|
| cita o incidente esperado | 30/30 | 30/30 |
| q10 e q12 marcadas como `insuficiente` (a resposta certa) | 6/6 | 6/6 |
| cita ID fora do contexto | 0 | 0 |
| **invenções** | **4** | **2** |
| **leituras erradas** | 6 | 6 |
| formatação estranha | 7 | 3 |

**Conclusões:**
- **A v2 reduz a invenção.** As invenções graves da v1 (contas e generalizações) não apareceram em nenhuma rodada da v2.
- **As leituras erradas não dependem do prompt.** Ficaram em 6 contra 6 e, com uma exceção (q07), nenhuma se repetiu entre rodadas. Isso indica ruído do modelo somado a `temperature=1.0`, que o prompt não corrige.
- **O ponto forte é estável.** Nas 6 rodadas, o modelo nunca inventou um incidente para a q10 (o certo não chega ao contexto) nem para a q12 (incidente fora do corpus).
- **A amostra é pequena.** Com 36 respostas de cada lado, o 4 × 2 é tendência, não prova.

## Invenções

| rodada | pergunta | o que a resposta diz | o que o contexto diz |
|---|---|---|---|
| v1a | q05 | "a Knight Capital perdeu cerca de US$ 460 milhões, **~2,5 vezes o capital disponível**" | *"realized a $460 million loss in 45-minutes. Remember, Knight only has $365 million in cash and equivalents."* A razão é ~1,3, e o texto não faz essa conta. |
| v1a | q11 | o código usava "adicionar um ano ao ano atual **sem considerar o século**" | *"someone wrote code that computed one year to be the current date plus one year"*. Não fala em século. |
| v1a | q01 | no caso [DAN-043]: "alinhar **políticas de review de código e deploy**" | A palavra *review* não aparece no contexto. O postmortem só conclui que *"having a function that deletes your database is too dangerous to have lying around"*. |
| v1c | q01 | "as lições foram [...] **revisar scripts de manutenção**" | Não aparece no contexto. |
| v2b | q03 | "foram lançadas **dezenas de correções e um processo de validação mais robusto** foi implementado" | *dozens* aparece no postmortem do crates.io e *validation* no da CrowdStrike, ambos no mesmo contexto. Nada disso está no da Mozilla ([DAN-090]). |
| v2b | q01 | no caso [DAN-043]: "implementação de proteções adicionais (por exemplo, **backups automatizados, checagens de estado, documentação revisada**)" | O postmortem do DAN-043 não lista essas medidas. É uma generalização. |

## Leituras erradas

| rodada | pergunta | o que a resposta diz | o que o contexto diz |
|---|---|---|---|
| v1b | q08 | "O **Facebook** post-mortem [DAN-145]" | O DAN-145 é do **Discord**. *Facebook* não aparece no contexto. |
| v1b | q05 | "**mais de 400 milhões** de ações trocadas" | *"4 million transactions against 154 stocks for more than **397 million** shares"* |
| v1b | q01 | "**eliminando todo o banco de dados em 30 minutos**" | 30 minutos foi o tempo para voltar: *"At around 11:15pm CET, 30 minutes after the disaster, we went back online"* |
| v1b | q07 | "**Não há registro no contexto de ocorrência semelhante** antes desse evento" | A pergunta é se já aconteceu antes, e o próprio DAN-088, citado na resposta, é esse registro. |
| v1c | q05 | "havia aprovado, mas **não havia instalado**, o novo código [...] em apenas sete dos oito servidores" | É o contrário: o código foi instalado em 7 e faltou no 8º (*"did not copy the new code to one of the eight SMARS computer servers"*). |
| v1c | q11 | a equipe gerenciou o certificado "**sabendo que ele estava expirado**" | A equipe sabia que **ia** expirar: *"knew the certificate was expiring"*, mas achava (incorretamente) que o Firefox ignorava a data. |
| v2a | q04 | "**Quase todas** as Standard Persistent Disks" foram afetadas | *"approximately **5%** of the Standard Persistent Disks in the zone experienced at least one I/O read or write failure"* |
| v2a | q05 | "Quando o mercado abriu o dia depois (**1 out 2012**)" | *"At 9:30 AM Eastern Time on **August 1, 2012** the markets opened"*. O "October" vem de *"SEC Filing [...] October 16, 2013"*, a data do relatório. |
| v2b | q02 | "Esses subsistemas **precisam ser reinicializados quando a capacidade é alterada**" | Generaliza um fato pontual: *"Removing a significant portion of the capacity caused each of these systems to require a full restart"* |
| v2c | q01 | "copiar dados do ambiente de staging (**últimos 18 h de trabalho**)" | 18 horas foi a duração da recuperação, não um período de dados. A perda foi de ~6 h (*"between 17:20 and 00:00 UTC"*). |
| v2c | q07 | "**Não há registro no contexto de outra ocorrência anterior** desse mesmo tipo de travamento" | Mesmo erro da v1b: o DAN-088 é o registro anterior. |
| v2c | q11 | "uma falha de comunicação entre a equipe responsável pela assinatura e o QA, **que acreditou** que o Firefox ignorava a data" | Quem acreditou foi a equipe de assinatura. O QA só não tinha teste de expiração: *"the Firefox QA plan didn't incorporate testing for certificate expiration"*. |

## Formatação estranha

| rodada | pergunta | o que aparece |
|---|---|---|
| v1a | q01 | emojis (1️⃣ 2️⃣) |
| v1b | q03 | termina com "**[CNPJ: DAN-090]**" |
| v1b | q07 | termina com a palavra "**XML**" solta |
| v1b | q02 | "Referência: [DAN-104]" repetido no fim |
| v1c | q02 | tags `<br>` no meio do texto |
| v1c | q03 e q06 | "Citação: [DAN-090]" e "Referência: [DAN-236]" repetidos no fim |
| v1c | q09 | IDs entre colchetes chineses: 【DAN-122】 |
| v2a | q09 | emojis (1️⃣ 2️⃣), mesmo com a regra 7 proibindo |
| v2a | q06 | "[DAN-236]" sozinho numa linha |
| v2c | q10 | "[DAN-xxx]" literal no texto |

## Português

O português ruim aparece com a mesma frequência nos dois prompts e não entrou na contagem de erros. Exemplos:
- "e-psi CPU insaturada", "seis horinhas", "aprofissional", "tradeiro" (v1);
- "rendeu-o", "auditoram", "indexo", "derramamento de serviço", "discos de prontidão", "escutar em xtime_lock" (v2).

A regra 7 da v2 (frases corretas e naturais) não teve efeito visível. Parece um limite do modelo de 20B.

## Citações extras (não contadas como erro)

- **q08:** o DAN-234 (Twilio, cluster Redis de faturamento) foi citado em 3 de 6 rodadas, como caso parecido. Os fatos ditos sobre ele estão corretos, mas a v2a diz que os dois casos mostram "exatamente o tipo" de problema perguntado, o que é exagero.
- **q01:** a v1c citou também o DAN-186 (Instapaper, limite de sistema de arquivos), uma analogia fraca.
- **q09:** a v1b listou DAN-124, DAN-142 e DAN-157 só para dizer que não se aplicam.

## Limitações da avaliação

As 12 perguntas e os `esperado` ficaram como estavam, para os resultados continuarem comparáveis. Os pontos abaixo devem ser considerados ao ler as tabelas.

- **Perguntas que entregam a resposta.** Na q03 (certificado do Firefox) e na q05 (US$ 460 milhões), a pergunta praticamente identifica o incidente. O acerto ali não mostra diagnóstico a partir de sintomas.
- **Outros incidentes pertinentes.**
  - Na q09, o DAN-152 (conta npm de um mantenedor do ESLint invadida) também responde à pergunta, embora o mecanismo seja outro: o DAN-122 é de pacotes falsos no JCenter. As 6 rodadas citaram os dois.
  - Na q11, o DAN-049 (crates.io, certificados recriados no deploy) também envolve certificados. Nenhuma rodada o citou.
- **A checagem automática conta acerto se aparecer qualquer um dos esperados ou aceitos.** Na q11, que espera dois incidentes, é preciso conferir os dois; nas 6 rodadas, a resposta citou DAN-090 e DAN-086.
- **Só os 5 primeiros incidentes vão para o prompt.** Na q10, o DAN-017 fica em 8º na busca, então o modelo não recebe a evidência. A resposta certa ali é "insuficiente".
- **Citação válida não é citação que sustenta o texto.** O nó `verificar_citacoes` só confere se o ID citado está entre os recuperados. Se o texto do incidente sustenta a afirmação, só a leitura manual verifica.
- **Fontes com hipóteses.** O DAN-236 (Steam) é uma thread de issue: a causa (`rm -rf "$STEAMROOT/"*` com a variável vazia) aparece junto com especulação dos participantes.

## Próximos passos sugeridos

1. **Manter a v2 como padrão.** Já é o padrão em `prompts.py`.
2. **Atacar as leituras erradas fora do prompt.** As opções são testar o `openai/gpt-oss-120b` no NIM (basta trocar `LLM_MODEL` no `.env`) ou baixar a temperatura. Depois, repetir esta conferência para comparar.
3. **Confirmar esta classificação.** Pode haver casos de fronteira entre invenção e leitura errada, e o ideal é que você e o André revisem.
