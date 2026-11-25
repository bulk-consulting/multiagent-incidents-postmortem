# Análise manual: saídas do Triagem e do Pesquisa híbrido com sintomas (2026-11-23)

Arquivos analisados:
- Triagem nas 32 perguntas: `triage_2026-11-23_1639.json` (`run_triage.py`);
- Pesquisa híbrido com descrição + sintomas, nas 21 que o Triagem mandou adiante:
  `agents/research/experiments/results/research_2026-11-23_1657_symptoms_hybrid.json` e
  `research_2026-11-23_1658_questions_hard_symptoms_hybrid.json`.

## 1. Triagem (32 saídas lidas)

**Decisões:** 21 `go_to_research`, 11 `ask_user`, 0 duplicados, 0 erros. As barradas usam 1 chamada ao
modelo (sem ferramenta); as que seguem usam 2 (uma chama `list_investigations`). De 6 a 25 s por pergunta.

**O que funciona bem:**
- sintomas curtos e em inglês, mesmo com a mensagem em português;
- as perguntas ao analista saem no idioma dele e são objetivas ("Qual é o nome do serviço central que está
  retornando 401?");
- `category` só aparece com pista clara: `Hardware/Power Failures` (raio), `Time` (leap second), `Database`
  (banco apagado).

**Problemas encontrados:**

| # | Problema | Exemplos | Efeito |
|---|---|---|---|
| T1 | **Os sintomas perdem o gatilho e a causa**, que são justamente o que distingue um incidente de outro | q02: "comando digitado errado removeu servidores demais" vira só *"S3 storage is down"*; q03 perde "certificado expirou"; q07 perde "leap second"; q-022 e q-032 perdem "o operador rodou um comando para remover servidores"; q-228 e q-229 perdem "reduzimos o tamanho do banco"; q-262/q-263 perdem "alguns dias depois de entrar em operação" | explica a piora do modo padrão do Pesquisa com sintomas: as consultas pelos sintomas ficam genéricas e trazem incidentes genéricos |
| T2 | **Rigidez com o serviço afetado**: barra mensagens que descrevem bem o problema, mas não dão o nome do serviço | q10 ("um serviço central passou a responder 401"), q-219/q-218 ("um serviço crítico"), q-034 ("todo o nosso tráfego bloqueado por uma regra de firewall"), q-260/q-261 (caso Metrist: "nosso serviço falha nas chamadas à API de um provedor de nuvem") | o analista precisa responder uma pergunta a mais antes de qualquer busca |
| T3 | **Perguntas sobre o histórico** não têm caminho no fluxo | q11 ("Quais incidentes do histórico envolveram certificados?") vira `ask_user`; já a q12 ("O que causou a indisponibilidade do Pix?") segue como incidente | comportamento inconsistente para o mesmo tipo de pergunta |
| T4 | **Sintoma em português**, contra a regra do prompt | q-218: *"todos os servidores caíram ao mesmo tempo"* | pequeno |
| T5 | **Ferramenta chamada sem o serviço**, mesmo quando ele foi identificado | q07 (`linux`) e q-170 (`api`) chamaram `list_investigations` com `service=""` | sem efeito hoje (a ferramenta devolve tudo), mas pode deixar passar duplicado com muitas investigações |
| T6 | **Nome do serviço inconsistente** | `onboard computer` (q-263) e `onboard_computer` (q-262); `service discovery` com espaço; mesmo incidente vira `video-player` (q-222, PT) e `database` (q-223, EN) | atrapalha a comparação com investigações abertas quando houver dados reais |

## 2. Pesquisa híbrido com sintomas (21 saídas lidas)

**Resultado:** incidente certo aprofundado em 17 de 20 (a q12 não tem incidente certo).

**As 3 "falhas", olhadas de perto:**
- **q-020** ("apagamos sem querer um banco de produção durante uma manutenção"): o esperado (DAN-164, GitLab)
  estava nos achados, em 4º; o LLM aprofundou só o DAN-043, que também é um banco de produção apagado sem
  querer. É uma resposta plausível; o gabarito aceita só o GitLab.
- **q-243 e q-242** ("a CDN caiu no mundo todo"): o esperado (DAN-154, Fastly) não apareceu; o LLM aprofundou
  três quedas mundiais da Cloudflare (DAN-005, DAN-011, DAN-016). Também são plausíveis: a mensagem não traz o
  detalhe que separa o caso da Fastly (uma configuração de cliente que disparou um bug).

Ou seja, nas 3, o agente entregou incidentes do mesmo tipo; a falha é contra um gabarito de uma resposta só.

**O que funciona bem:**
- as consultas do LLM usam detalhes da descrição que os sintomas perderam ("typo command removed servers",
  "downsized database", "leap second", "after frontend deploy");
- o `why` é bom na maioria: diz o que bate e o que não bate ("though the trigger was Slack disconnections...",
  "though no explicit downsizing mentioned");
- a q12 (Pix, fora do corpus) fez 8 consultas, não aprofundou nada e não inventou incidente;
- nos post-mortems bem estruturados, os trechos trazem causa e correção completas: Discord (DAN-145), Roblox
  (DAN-211), Mars Pathfinder (DAN-200), Cloudflare (DAN-018), Buildkite (DAN-125).

**Problemas encontrados:**

| # | Problema | Exemplos | Efeito |
|---|---|---|---|
| P1 | **A consulta fixa de causa traz muitas vezes a introdução ou a narrativa**, não a causa | Firefox: nota do editor; GCE: só o cabeçalho com datas; Buildkite: "What a morning…"; Steam: um comentário perguntando "o que causou isso?" | a causa chega mesmo assim, pelos trechos da consulta do LLM ou da busca inicial, mas o trecho marcado como "cause" engana |
| P2 | **A consulta fixa de correção às vezes traz seção sem conteúdo útil** | Firefox: "Where to Learn More" (links); kernel (DAN-089): código de teste | ruído para o Diagnóstico |
| P3 | **Documentos com uma seção só** anulam a preferência por título de correção | S3 (DAN-104): todos os trechos têm o mesmo título "Summary of the Amazon S3 Service Disruption..." | a correção aparece, mas por acaso |
| P4 | **O LLM usa o que já sabe dos incidentes famosos** | consultas com "priority inversion VxWorks" (Mars), "Consul streaming BoltDB" (Roblox), "React dependency array" (Cloudflare) antes de ler os trechos | ajuda a busca, mas infla o resultado: os post-mortems são públicos e o modelo os conhece (a "contaminação" do cap. 10 do livro do Dibia). Com incidentes internos de verdade, o acerto tende a ser menor |
| P5 | **`why` fora do padrão** | q03 em português ("Corresponde ao incidente atual..."); q-022 com várias frases | o campo não diz o idioma (a descrição da ferramenta pede "uma frase curta", sem idioma) |
| P6 | **3º incidente aprofundado por "comparação"**, com relação fraca | q08: DAN-219 ("somewhat related"); q-262: DAN-198 ("included for comparison") | mais trechos de ruído para o Diagnóstico |
| P7 | **`final_note` sempre vazio** no híbrido | todas as 21 | o fluxo termina depois de `search_inside_incidents`, sem chamada final; o campo não serve neste modo |
| P8 | **Tempo variável** | 5 a 61 s; as de ~50–60 s esperaram o limitador (2 perguntas em paralelo) | normal com o limite de 10 chamadas por minuto |

## 3. Conclusões

1. **O sintoma do Triagem não serve como consulta de busca** (T1): ele descreve o que está falhando, mas tira o
   gatilho e a causa, que são o que diferencia os incidentes. A descrição completa continua sendo a melhor
   entrada para a busca; os sintomas podem ir ao LLM do Pesquisa como contexto.
2. **O híbrido é robusto mesmo assim**, porque garante os candidatos da descrição e porque o LLM escreve consultas
   com os detalhes que os sintomas perderam. As 3 falhas são respostas plausíveis contra um gabarito de uma
   resposta só.
3. **Para o Diagnóstico, a qualidade dos trechos importa mais que o acerto do incidente**: os rótulos "cause" e
   "fix" nem sempre correspondem ao conteúdo (P1, P2, P3). O Diagnóstico deve ler os trechos, não confiar no rótulo.
4. **O acerto medido nos post-mortems públicos é otimista** (P4).

## 4. Sugestões (para decidir)

| Para quem | Sugestão |
|---|---|
| Triagem (Mari) | um campo novo, por exemplo `trigger` ou `context`, com o gatilho e as pistas de causa ("after an operator ran a command to remove servers", "certificate expired"); avaliar se a falta do nome do serviço deve barrar quando o problema está bem descrito (T2); sintomas sempre em inglês (T4); usar o serviço identificado na ferramenta (T5) |
| Pesquisa (André) | no modo padrão, os 10 candidatos da descrição entram sempre e os sintomas só acrescentam; no `why`, pedir inglês e uma frase; revisar a consulta fixa de causa (P1) |
| Avaliação | aceitar mais de um incidente certo quando houver casos equivalentes (q-020, q-242, q-243); lembrar da contaminação ao apresentar os números |
