# Ficha de post-mortem — formulário

**Versão:** 1.0 (rascunho) · **Schema:** [`ficha.schema.json`](ficha.schema.json) · **Prompt:** [`prompt_extracao.md`](prompt_extracao.md) v2.21

Cada documento do danluu vira uma ficha `DAN-xxx.json`. A ficha **não substitui** o texto original: o RAG continua indexando e citando o original. A ficha organiza o que o texto diz, para triagem, metadados e chunking.

## A regra principal

**Toda afirmação vem com trechos literais do texto original** (campo `trechos`, em inglês, copiados sem alteração). O validador confere se cada trecho existe no texto. Se o texto não diz, o campo fica `null`, vazio ou `ausente`: **nunca se completa com conhecimento próprio**.

Os campos `texto` são frases curtas escritas pelo LLM. São derivados; a evidência são os `trechos`. **Os trechos de uma afirmação precisam sustentar sozinhos todo detalhe do texto** (nome, data, número, quem fez, resultado): quem lê não deve precisar de outra parte do documento para conferir.

Duas regras completam essa (prompt v2): **não ligar fatos com "por isso" se o texto não liga**, e **não escrever como feito o que era só plano** ("would involve", "we will").

## Idioma

**Todo o conteúdo da ficha é em inglês**: `resumo`, `texto`, `perguntas_em_aberto`, `motivo_confianca_baixa`, além dos `trechos`. Motivos: evita perder nuances na tradução (ex.: *"we believe"* virar certeza), facilita conferir a ficha contra o original e mantém o mesmo idioma dos documentos para a busca. A tradução para português acontece só na resposta do Copilot ao analista.

Os **nomes dos campos e os valores das listas** (`causa_raiz`, `concreta`, `especifica`…) seguem em português, como na régua: são o vocabulário do projeto e não afetam a extração.

## Estrutura

```
ficha
├── catalog_id, schema_version
├── triagem            ← perguntas da régua sobre o documento
├── incidente          ← o que aconteceu (null se o documento não tem o incidente)
├── confianca          ← alta / baixa (+ motivo se baixa)
├── observacoes        ← notas opcionais que não são escolhas
└── extracao           ← modelo, data, versão do prompt
```

## Bloco `triagem`

Mesmas perguntas e respostas da régua ([`docs/triagem/regua.md`](../../docs/triagem/regua.md)).

| Campo | Régua | Respostas |
|---|---|---|
| `catalogo` | P1 | `sim`, `parcial`, `nao`, `nao_verificavel` |
| `autoria` | P2 | `primaria`, `secundaria` |
| `tipo` | P3 | `postmortem`, `atualizacoes_status`, `relatorio_periodico`, `artigo_tecnico`, `relatorio_formal`, `noticia_enciclopedia`, `outro` |
| `dominio` | P4 | `software_servicos`, `infra_fisica_datacenter`, `seguranca`, `fora_de_ti` |
| `seguranca` | P5 | `nao`, `exposicao_dados`, `ataque` |
| `problemas_texto` | P10 (parte do LLM) | lista de `sem_conteudo`, `comentarios`, `rodape_marketing`, `pdf_embaralhado` |

Se `catalogo` for `nao` ou `nao_verificavel`, `autoria`, `tipo`, `dominio` e `seguranca` ficam `null` e `incidente` fica `null`.

## Bloco `incidente`

| Campo | O que é | Origem da ideia | Régua |
|---|---|---|---|
| `resumo` | 1 a 3 frases em inglês (até 600 caracteres), neutras | todos os templates | — |
| `data_incidente` | `AAAA-MM-DD`, `AAAA-MM` ou `AAAA`, só se estiver no texto | IPA | — |
| `status_relatorio` | `final`, `preliminar`, `misto` (atualizações preliminares + relatório final no mesmo texto) ou `indefinido` | agent-postmortems, The Cloud Book | — |
| `servicos_afetados` | Serviços ou produtos impactados | IPA | — |
| `tecnologias` | Componentes técnicos citados (ex.: `PostgreSQL`, `BGP`, `Kubernetes`) | — | — |
| `categoria_causa` | Origem da falha (ver abaixo) | IPA, ampliada | — |
| `deteccao` | `forma` (como foi percebido) + `descricao` (sintoma notado e, se houver, como) | SRE Book, Kehoe | — |
| `gatilho` | O evento que **disparou** o incidente | SRE Book, Kehoe, agent-postmortems | — |
| `causa_raiz` | `status` + `descricao`: a falha **de fundo** | todos | P6 |
| `fatores_contribuintes` | Até 6 fatores que agravaram ou atrasaram a recuperação | agent-postmortems, Kehoe (*process breakdowns*), The Cloud Book | — |
| `mudanca_causadora` | `nivel` + `descricao`: config, código, versão ou parâmetro que mudou | IncidentDB (só o nome do campo) | P8 |
| `mitigacao` | `nivel` + `passos` em ordem: o que foi feito durante o incidente | todos | P7 |
| `prevencao` | `nivel` + `acoes`: o que será feito para não repetir | todos | P9 |
| `duracao` | `minutos` + `trechos`, só se o texto permitir calcular | Kehoe, IPA | — |
| `perguntas_em_aberto` | O que o próprio texto diz que ficou sem resposta | Kehoe (*open questions*) | — |

### Gatilho × causa raiz

São coisas diferentes e ficam em campos separados:

- **Gatilho:** o evento imediatamente anterior ao início do impacto (deploy, mudança de política, rotação de senha, pico de tráfego, comando de um operador).
- **Causa raiz:** o defeito ou a condição do sistema que fez o gatilho virar impacto. Fica no nível técnico; causas organizacionais (sem dono, sem teste, sem documentação) vão para `fatores_contribuintes`.

Exemplo: "uma adição de capacidade" (gatilho) fez os servidores ultrapassarem "o limite de threads do sistema operacional" (causa raiz). Se o texto não separa os dois, a mesma informação pode aparecer só em `causa_raiz`, com `gatilho = null`.

Se o texto descreve **mais de um mecanismo** (ex.: DAN-053, vazamento de VMs + limite de CPU Reservations), a causa raiz fica com o principal, os outros vão para `fatores_contribuintes` com o papel que o texto dá a eles, e a confiança fica `baixa`.

### `causa_raiz.status`

Igual à P6 da régua: `concreta` (o que falhou e por quê, com mecanismo), `incerta` (hipóteses; o texto diz que não foi confirmado), `vaga` (só a categoria), `ausente` (não diz; então `descricao = null`).

### `deteccao.forma`

`alerta_automatico`, `usuarios_clientes`, `equipe_interna` (alguém da equipe percebeu sem alerta), `terceiros` (outra empresa, imprensa), `nao_informada`.

### `categoria_causa`

8 das 9 categorias do IPA (`configuration-error`, `human-error`, `credential-auth`, `database-storage`, `cascading-failure`, `network-bgp`, `supply-chain`, `other`; `agent-ai` foi retirada por não se aplicar), mais três que aparecem muito no danluu:

| Nova categoria | Quando usar |
|---|---|
| `capacity-load` | Carga, limite ou capacidade esgotada sem mudança de configuração |
| `hardware-power` | Energia, refrigeração ou falha de hardware |
| `software-bug` | Defeito de código que não se encaixa nas outras |

Regra do IPA mantida: **classificar pela origem, não pelo efeito**. A categoria classifica a **causa raiz, não o gatilho**: uma mudança de política (gatilho) que atinge código sem tratamento de erro (causa raiz) é `software-bug`, não `configuration-error`. `null` se a causa for `ausente`.

## Confiança e observações

`confianca` mede se **as regras decidiram todos os campos**, não a certeza do texto (essa fica em `causa_raiz.status`).
- `alta`: para todo campo, as regras deixam um único valor.
- `baixa`: em pelo menos um campo, dois valores continuam cabendo depois de aplicar as regras. `motivo_confianca_baixa` é obrigatório e diz quais campos e quais valores. É isso que manda a ficha para a revisão.

`observacoes` (opcional) guarda notas que **não** são escolhas: de onde veio um valor (ano tirado da data de publicação), a outra duração quando o texto dá duas, lista anunciada mas ausente no texto extraído, texto repetido em outro idioma. Não baixa a confiança. Até a v2.5 essas notas iam para `motivo_confianca_baixa`, o que forçava quase toda ficha a `baixa`.

## O que ficou de fora, e por quê

- **Severidade:** o danluu não tem severidade comparável entre empresas; seria opinião do LLM.
- **Pessoas envolvidas, autores:** não ajudam no diagnóstico e trazem risco de expor nomes.
- **Lições aprendidas (o que foi bem / mal / sorte):** pouco úteis para diagnosticar um incidente novo; parte delas já cabe em `fatores_contribuintes` e `prevencao`.
- **Timeline completa:** fica no texto original e no chunking; copiar para a ficha duplicaria conteúdo.

## Histórico do prompt

- **v1** ([`prompt_extracao_v1.md`](prompt_extracao_v1.md); fichas em `saida/v1/`): piloto com DAN-053, 164, 169, 183. A revisão por outro LLM mostrou textos que diziam mais que seus trechos, causalidade inventada entre dois mecanismos, plano escrito como feito, resumo sem desfecho e correção concreta omitida.
- **v2**: regras acima; definições de gatilho, causa raiz, detecção (como foi percebido, não a resposta) e categoria pela causa raiz.
- **v2.1** (revisão da DAN-164): passo só planejado não entra em `mitigacao`; comando de operador não é `mudanca_causadora` (`nao_se_aplica`); `confianca` alta só se nenhum campo exigiu escolha.
- **v2.2** (revisão das DAN-169 e 183): ação já feita marcada como feita em `prevencao`; quem registra dúvida entre níveis escolhe o mais fraco; gatilho não é observação feita na investigação (senão `null`); migração sem ligação declarada não é `mudanca_causadora`; passo "worth trying" precisa de trecho que confirme a execução.
- **v2.3** (revisão das DAN-024, 152, 166): regra do gatilho `null` (texto não separa gatilho e causa) posta em destaque; recomendações a terceiros podem entrar em `prevencao`, marcadas "Recommendation to…".
- **v2.4** (revisão das DAN-027, 046, 063): gatilho só quando há condição prévia distinta do evento (mudança que é ela mesma o erro → `null`); "X e depois identificaram Y" não é "Y causou X"; ano pode vir da data de publicação escrita no texto, nunca do título ou da URL; categoria segue a causa raiz mesmo contra a manchete (`other` se não há mecanismo).
- **v2.5** (teste às cegas, 97% de concordância): `postmortem` inclui blog narrativo da própria empresa; status pages são `atualizacoes_status`; `status_relatorio` é a fase do texto (pendências vão para `perguntas_em_aberto`); `incerta` só quando o texto põe em dúvida o que falhou; duração declarada prevalece sobre a calculada.
- **v2.6** (leitura do prompt inteiro pelo GPT): consolidação. Campo `observacoes`, separado da confiança; `confianca` passa a medir só escolhas que as regras não resolvem; bloco causal reescrito como um todo (gatilho só com condição prévia; ação de operador sem condição → `causa_raiz` `human-error`); `mudanca_causadora` `generica` (tipo e lugar da mudança) × `ausente` (nada sobre o quê); `catalogo: parcial` extrai só o incidente do catálogo; mitigação `especifica` se um passo diz o que mudou e onde; duração é a do impacto.
- **v2.7** (2º teste às cegas, 93%, quase toda a diferença na confiança): `deteccao.descricao` inclui o sintoma notado mesmo sem dizer como; `human-error` quando a ação do operador é o gatilho e a causa é a condição que a permitiu; exemplo de ataque no gatilho; `prevencao` `especificas` só se uma ação diz o mecanismo e onde (mesmo critério da mitigação).
- **v2.8** (revisão do lote 01: 23 ERRADOS procedentes em 9 fichas; 8 de 8 `baixa` sem dúvida real): checklist antes de marcar `baixa`; duração declarada só vale se medir o impacto; trechos com referência ao contexto ("at this point", "something"); tentado/concebido/agendado não é resultado; fator contribuinte não é impacto, mecanismo nem atraso de comunicação; ataques classificados pelo mecanismo (DDoS → `capacity-load`); catálogo que descreve vários incidentes → causa comum, gatilho `null`; autoria `primaria` para quem era do time responsável.
- **v2.9** (revisão do lote 02: 21 ERRADOS em 10 fichas, metade de trecho que não prova o texto; 4 de 5 `baixa` sem dúvida real): passo obrigatório de verificação detalhe a detalhe (todo nome, número, hora e resultado do texto aponta para um trecho da mesma afirmação); `motivo_confianca_baixa` precisa dizer por que a definição do campo não decide; mitigação só até o fim do impacto (o que vem depois vai para prevenção como "Already done").
- **v2.10** (revisão do lote 03: 15 ERRADOS em 10 fichas; 0 `baixa`, nenhuma dúvida escondida): passos de resposta (abrir incidente, montar equipe, investigar, detectar, comunicar) não são mitigação; funcionamento normal do sistema e mitigação repetida não são fator contribuinte; `rodape_marketing` inclui rodapé de lista de e-mail e de site.
- **v2.11** (revisão do lote 04: 14 ERRADOS em 9 fichas; 4 de 5 `baixa` com dúvida legítima): pedido a outra equipe ("asked X to") não é feito; detecção sem passos de resposta; fator contribuinte não é afirmação sobre pessoa; cabeçalho dentro do texto extraído vale para a data; verificação detalhe a detalhe também em cada passo de mitigação e ação de prevenção.
- **v2.12** (revisão do lote 05: 15 ERRADOS em 10 fichas; taxa estável em ~1,5 por ficha desde o lote 03): objetivo ("to determine", "to ensure") não é resultado; "decided at X" numa timeline não é "did at X"; horário vindo de parágrafo de resumo entra como trecho; software de controle de sistemas físicos do data center é `infra_fisica_datacenter`; bug antigo sem queda delimitada tem duração `null` e a correção é a mitigação. A partir do lote 06, a sessão de extração faz uma autorrevisão ([`autorrevisao.md`](autorrevisao.md)) e a conferência no GPT passa a ser por amostra.
- **v2.13** (amostra do lote 06: 6 ERRADOS em 6 fichas, 1,0 por ficha, contra 1,5 no lote 05): `equipe_interna` só quando o texto diz que uma pessoa notou sem alerta; "detected internally" ou só o sintoma é `nao_informada`. Atividade operacional automática (scaling, failover) é `nao_se_aplica` em `mudanca_causadora`.
- **v2.14** (amostra do lote 09: 4 ERRADOS em 7 fichas, 0,6 por ficha): a regra de duração que só existia no lembrete do pedido de revisão entrou no prompt. Marcas "Impact starts"/"Impact ends" no texto valem mais que outros horários; sem marca de fim, o horário em que o serviço voltou (mesmo degradado) é o fim; faixa ("10-15 minutes") dá `null`. O lembrete da revisão foi alinhado ao prompt.
- **v2.15** (amostra do lote 12: 7 ERRADOS em 7 fichas, 1,0 por ficha): `configuration-error` passa a cobrir também um valor de configuração errado há muito tempo, sem mudança recente (antes a definição exigia "a change" e esses casos não tinham categoria). Não muda nenhuma ficha aceita (DAN-001 já estava assim).
- **v2.16** (amostra do lote 13: 8 ERRADOS em 6 fichas, 1,3 por ficha): `software-bug` é residual (outra categoria que caiba vence; código que funcionava não é `software-bug`); "total duration of the incident" diferente das marcas de impacto não vence as marcas. Os dois casos entram na lista de dúvidas que a regra já decide.
- **v2.17** (amostra do lote 15: 10 ERRADOS em 6 fichas, 1,7 por ficha, acima do limite; o lote 16 volta a ser conferido inteiro): mudança antiga que só impediu a recuperação ou ampliou o impacto fica na causa raiz, não em `mudanca_causadora` (disparo por hardware ou dependência → `nao_se_aplica`); mudança não diagnosticada no comportamento de uma dependência externa é `nao_se_aplica` (pode ser o gatilho).
- **v2.18** (revisão das fichas antigas, quando o GPT e eu escolhemos recuperações parciais diferentes para a mesma ficha): a volta parcial só encerra o impacto se o texto disser que o serviço afetado voltou para a maioria; volta de subsistema, de outra região ou "a pior parte durou X" não contam; várias voltas desse tipo ou nenhuma → `null`, sem baixar a confiança. DAN-062, 106 e 111 passaram de `baixa` para `alta` com duração `null`.
- **v2.19** (reextração de 49 documentos): nota de formato antes do bloco INPUT. `## ` marca intertítulos, e as atualizações de status page vêm da mais nova para a mais antiga, então o incidente começa na última. Não muda regra nem ficha aceita. O lote 00 não precisa rodar de novo, porque os documentos do gabarito ficam com o texto original.
- **v2.20** (lotes 17-18, quando o GPT contestou duas vezes o precedente que a conferência já usava): "engineers were paged" ou "were alerted", sem pessoa que deu o aviso, é `alerta_automatico`. Não muda ficha aceita.
- **v2.21** (lotes 18-19, DAN-097 e 160): ação de prevenção que o texto descreve em andamento é "In progress:", e "Planned:" fica para "we will" e "we plan". Saiu o "we are looking into" dos exemplos de planejado da regra 4, que contradizia isso. Não muda ficha aceita.

## Validação

O schema rejeita: campos inventados, valores fora das listas, trechos com menos de 10 caracteres, combinações incoerentes (ex.: causa `ausente` com descrição, mitigação `especifica` sem passos, `incidente` preenchido quando o documento não tem o incidente, confiança `baixa` sem motivo, motivo com confiança `alta`).

O que o schema **não** verifica, e fica para o `validar_fichas.py`: se cada trecho existe de fato no texto original.

O que **nenhum programa** verifica: se os trechos sustentam o texto, se a classificação está certa e se faltou algo importante. Isso fica para a revisão (outro LLM aponta, uma pessoa decide).
