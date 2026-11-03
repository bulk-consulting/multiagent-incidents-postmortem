# Régua de classificação — danluu

**Status:** rascunho para discussão (André e Mari)

## Para que serve

Classificar os 224 documentos extraídos do danluu com as mesmas perguntas e respostas, seja quem for que classifique (script, LLM ou pessoa). A régua **só descreve** cada documento; ela não decide quem entra no RAG. A regra de entrada será definida depois, olhando a contagem de cada combinação de respostas.

## Regras gerais

1. **Responder pelo que está no texto**, não pelo que se sabe do incidente. Se o texto não diz, a resposta é "ausente", mesmo que o incidente seja famoso.
2. **Toda resposta (exceto as do script) vem com um trecho literal do texto** que a justifica, em inglês e copiado como está.
3. **Na dúvida entre duas respostas, escolher a mais fraca** e marcar confiança baixa. A revisão humana resolve.
4. **Todo documento recebe uma linha**, inclusive os vazios e os duplicados.

## Quem responde o quê

| # | Pergunta | Quem responde |
|---|---|---|
| P1 | É o incidente do catálogo? | LLM |
| P2 | Quem escreveu? | LLM |
| P3 | Que tipo de texto é? | LLM |
| P4 | Qual o domínio do incidente? | LLM |
| P5 | Envolve segurança ou privacidade? | LLM |
| P6 | A causa está explicada? | LLM |
| P7 | A recuperação está descrita? | LLM |
| P8 | A mudança técnica que causou o problema está identificada? | LLM |
| P9 | Há ações de prevenção? | LLM |
| P10 | Problemas do texto extraído | Script (parte) + LLM (parte) |
| P11 | Qualidade geral do texto | Derivada de P10 |

---

## P1 — É o incidente do catálogo?

Compara o texto com a descrição do incidente em `catalog.csv`.

| Resposta | Definição | Exemplo |
|---|---|---|
| `sim` | O texto trata principalmente do incidente descrito no catálogo | DAN-211 (Roblox, outage do Consul) |
| `parcial` | O incidente aparece, mas é uma parte pequena de um texto sobre outro assunto, **ou** o texto mistura vários incidentes | DAN-022 (Etsy: artigo sobre replicação com BitTorrent; o outage é um parágrafo) |
| `nao` | O texto tem conteúdo, mas sobre **outro** incidente ou assunto (ex.: redirecionamento para outro artigo) | — |
| `nao_verificavel` | Não há conteúdo do artigo para comparar: texto vazio ou só menus e navegação | DAN-041, DAN-212 (página montada por JavaScript, vazia) |

> Se P1 for `nao` ou `nao_verificavel`, deixe P2 a P9 em branco: não há incidente sobre o qual responder.

## P2 — Quem escreveu?

| Resposta | Definição | Exemplo |
|---|---|---|
| `primaria` | A própria empresa afetada, ou o provedor responsável pelo serviço | DAN-009 (blog da Cloudflare sobre o incidente da Cloudflare) |
| `secundaria` | Terceiros: imprensa, Wikipédia, análise externa, órgão investigador | DAN-059 (Valve: "no official postmortem", análise de terceiros) |

> Relatórios de órgãos oficiais sobre a própria infraestrutura (ex.: relatório de investigação) contam como `secundaria`, salvo se escritos pela organização afetada.

## P3 — Que tipo de texto é?

| Resposta | Definição | Exemplo |
|---|---|---|
| `postmortem` | Relato estruturado após o incidente: o que aconteceu, por quê, o que será feito | DAN-143 (Datadog), DAN-164 (GitLab) |
| `atualizacoes_status` | Atualizações publicadas durante o incidente, com ou sem um post-mortem no final | DAN-235 (Twilio: só atualizações, sem post-mortem) |
| `relatorio_periodico` | Relatório que cobre vários incidentes de um período | DAN-162 (GitHub availability report de outubro de 2024) |
| `artigo_tecnico` | Artigo sobre um tema técnico em que o incidente é uma parte | DAN-022 (Etsy) |
| `relatorio_formal` | Relatório extenso de investigação, consultoria ou governança | DAN-191 (King's College, relatório de consultoria) |
| `noticia_enciclopedia` | Matéria jornalística ou verbete | forbes.com, wikipedia.org |
| `outro` | Nenhum dos anteriores: lista de e-mails, fórum, issue, thread | DAN-088 (lista do kernel Linux), DAN-236 (issue no GitHub) |

## P4 — Qual o domínio do incidente?

Classificar **pela origem do problema**, não pelo efeito.

| Resposta | Definição | Exemplo |
|---|---|---|
| `software_servicos` | Falha em software, configuração, deploy, banco de dados, rede lógica, nuvem, dependências | DAN-137 (regex no WAF), DAN-078 (failover MySQL) |
| `infra_fisica_datacenter` | Energia, refrigeração, hardware ou rede física **dentro de datacenter** | DAN-061 (AWS: gerador falhou), DAN-068 (Cloudflare: disjuntores), DAN-070 (GitHub: queda de energia) |
| `seguranca` | A origem é uma ação maliciosa: invasão, credencial roubada, pacote malicioso, cadeia de suprimentos | DAN-140 (Okta → Cloudflare), DAN-157 (Gentoo), DAN-177 (Homebrew) |
| `fora_de_ti` | Sistemas que não são de TI: rede elétrica pública, aviação, espaço, saúde, naval, indústria | DAN-069 e DAN-202 (rede elétrica dos EUA), DAN-200 (NASA Pathfinder), DAN-046 (estação de tratamento de água) |

> Atenção: queda de energia **em datacenter** é `infra_fisica_datacenter`, não `fora_de_ti`. Software embarcado em sistema não-TI (ex.: NASA Pathfinder) é `fora_de_ti`.

## P5 — Envolve segurança ou privacidade?

Marca efeitos de segurança mesmo quando a origem não foi maliciosa.

| Resposta | Definição | Exemplo |
|---|---|---|
| `nao` | Sem exposição de dados nem ação maliciosa | DAN-211 (Roblox) |
| `exposicao_dados` | Dados de usuários expostos por falha, sem ataque | DAN-204 (OpenAI: bug no redis-py mostrou dados de outros usuários) |
| `ataque` | Houve ação maliciosa (então P4 deve ser `seguranca`) | DAN-141 (Salesloft), DAN-122 (pacotes Maven maliciosos) |

## P6 — A causa está explicada?

| Resposta | Definição | Exemplo |
|---|---|---|
| `concreta` | Diz **o que** falhou e **por quê**, com mecanismo técnico verificável | DAN-143: atualização do systemd reiniciou o networkd, que apagou as rotas do Cilium |
| `incerta` | Apresenta hipóteses ou mecanismo parcial, e o próprio texto diz que a causa não foi confirmada | DAN-230 (Tarsnap: origem dos erros no S3 não confirmada), DAN-183 (incident.io) |
| `vaga` | Só a categoria ou um termo genérico, sem mecanismo | DAN-235 ("filtragem na operadora"); textos como "a network issue" ou "an upstream provider" |
| `ausente` | Não diz por que aconteceu | — |

> Teste rápido: um engenheiro de outra empresa conseguiria procurar esse mesmo problema no próprio ambiente só com o que está escrito? Se sim, é `concreta`.

## P7 — A recuperação está descrita?

O que foi feito **durante** o incidente para restaurar o serviço.

| Resposta | Definição | Exemplo |
|---|---|---|
| `especifica` | Passos concretos: o que foi alterado, em que ordem, com quais componentes | DAN-211 (desligar o streaming do Consul, reimplantar o cache, liberar jogadores em lotes de 10%) |
| `generica` | Só a ação genérica: "revertemos", "reiniciamos", "aplicamos uma correção" | DAN-027 (revert), DAN-192 (revert) |
| `ausente` | Não diz como o serviço voltou | — |

## P8 — A mudança técnica que causou o problema está identificada?

A config, o código, a versão ou o parâmetro que **disparou** o incidente.

| Resposta | Definição | Exemplo |
|---|---|---|
| `especifica` | Nomeia o item exato: parâmetro, arquivo, versão, regra, comando | DAN-002 (parâmetro de mínimo de hosts saudáveis), DAN-045 (código VCL `req.backend` + restart), DAN-135 (versões incompatíveis de kubelet e kube-proxy) |
| `generica` | Diz que houve uma mudança, sem identificar qual | DAN-027 ("mudança de configuração nos bancos") |
| `nao_se_aplica` | O disparo não foi uma mudança: falha física, carga, ataque, bug latente sem mudança | DAN-061 (gerador), DAN-064 (bug em software de terceiro) |
| `ausente` | Houve mudança, mas o texto não diz qual | — |

## P9 — Há ações de prevenção?

| Resposta | Definição | Exemplo |
|---|---|---|
| `especificas` | Ações concretas e verificáveis: limite novo, validação, teste, alerta, mudança de arquitetura | DAN-002 (validação semântica de config e limite por hora na remoção de hosts) |
| `genericas` | Intenções sem detalhe: "vamos melhorar nossos processos" | DAN-027 |
| `ausentes` | O texto não fala em prevenção | DAN-235 |

## P10 — Problemas do texto extraído

Lista de marcações (pode haver várias ou nenhuma).

| Marcação | Definição | Quem detecta | Exemplo |
|---|---|---|---|
| `nao_coletado` | O link não foi baixado (falha de coleta ou `robots.txt`) | Script | DAN-021 |
| `vazio` | Nenhum texto extraído | Script | DAN-041 |
| `curto` | Menos de 300 palavras | Script | — |
| `duplicado` | Mesmo conteúdo de outro documento com texto (registrar qual); páginas vazias contam só como `vazio` | Script | nenhum caso no corpus atual |
| `outro_idioma` | Trechos relevantes em idioma diferente do inglês | Script | DAN-002 (coreano), DAN-064 (4 idiomas) |
| `repeticao` | Mais de 10% dos parágrafos repetidos | Script | DAN-072 (84%) |
| `titulos_perdidos` | O HTML tem títulos de seção e o texto extraído não | Script | DAN-078, DAN-143, DAN-183, DAN-234 |
| `atualizacoes_perdidas` | Página de Statuspage cujas atualizações não foram extraídas | Script | DAN-135, DAN-144, DAN-147 |
| `sem_conteudo` | Há texto, mas só menus, navegação ou chamadas da página, sem o artigo | LLM | — |
| `pdf_embaralhado` | Colunas ou ordem do PDF misturadas | LLM | DAN-191 |
| `comentarios` | Comentários de leitores incluídos no texto | LLM | DAN-022 |
| `rodape_marketing` | Rodapé, propaganda ou chamada de vagas no texto | LLM | DAN-027, DAN-083 |

## P11 — Qualidade geral do texto

Derivada automaticamente de P10.

| Resposta | Regra |
|---|---|
| `inutilizavel` | `nao_coletado`, `vazio`, `sem_conteudo`, `duplicado` (a cópia), ou `pdf_embaralhado` grave |
| `precisa_reextracao` | `titulos_perdidos` ou `atualizacoes_perdidas` (corrige-se a partir do HTML em `data/raw/`) |
| `precisa_limpeza` | `outro_idioma`, `repeticao`, `comentarios` ou `rodape_marketing` |
| `ok` | Nenhuma marcação |

---

## Campos extras (aproveitam a mesma leitura do LLM)

Não entram na triagem, mas viram metadados no RAG.

| Campo | Formato | Observação |
|---|---|---|
| `data_incidente` | `AAAA-MM-DD`, `AAAA-MM` ou `AAAA` | Só se estiver no texto; 92 documentos não têm ano na URL nem no título |
| `tecnologias` | Lista curta (ex.: `PostgreSQL`, `BGP`, `Kubernetes`) | Usada como tag de filtro |
| `resumo_causa` | 1 frase em português | Só quando P6 for `concreta` ou `incerta` |

## Saída esperada por documento

```json
{
  "catalog_id": "DAN-143",
  "p1_catalogo": "sim",
  "p2_autoria": "primaria",
  "p3_tipo": "postmortem",
  "p4_dominio": "software_servicos",
  "p5_seguranca": "nao",
  "p6_causa": "concreta",
  "p7_recuperacao": "especifica",
  "p8_mudanca": "especifica",
  "p9_prevencao": "especificas",
  "p10_problemas": ["titulos_perdidos", "rodape_marketing"],
  "p11_qualidade": "precisa_reextracao",
  "evidencias": {
    "p6_causa": "a security update to systemd was automatically applied to a number of VMs, which caused a latent adverse interaction in the network stack",
    "p8_mudanca": "`systemd-networkd` forcibly deleted the routes managed by the Container Network Interface (CNI) plugin (Cilium)"
  },
  "confianca": "alta",
  "classificado_por": "llm",
  "data_incidente": "2023-03-08",
  "tecnologias": ["systemd", "Cilium", "Kubernetes", "Ubuntu 22.04"],
  "resumo_causa": "Atualização automática do systemd reiniciou o networkd, que apagou as rotas do Cilium e isolou os nós."
}
```

## Pontos em aberto para André e Mari

1. **P4 `infra_fisica_datacenter`:** manter separado de `software_servicos`, ou juntar? (Separado permite decidir depois.)
2. **P6 `incerta`:** separar de `vaga` faz sentido para vocês? Na curadoria E1.3 isso foi importante (DAN-183, 188, 218, 230).
3. **P2 `secundaria`:** relatos de terceiros contam como evidência fraca ou não entram?
4. **Confiança:** usar só `alta`/`baixa`, ou três níveis?
5. **Exemplos:** trocar ou acrescentar exemplos que vocês conheçam melhor.
