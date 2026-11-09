# Avaliação da busca (2026-11-09)

Gerado por `multiagent_env/bin/python -I ingestion/avaliacao/avaliar.py --resumo`.
- **278 perguntas com resposta** e 5 sem resposta (suite_ipa.json + suite_propria.json).
- Mais as **12 perguntas da Mari** (suite_mari.json): as 6 do validate_rag.py dela, em português e em
  inglês, escritas sem olhar as fichas. Elas ficam fora do total "TODAS".
- h1 / h5 = documento esperado em 1º / entre os 5 primeiros; mrr = média de 1/posição.
- Os índices com resumo só foram avaliados com o Qwen3. O e5 e o bge-m3 são da avaliação de 2026-11-04,
  antes do chunk de resumo, do DAN-084 e da correção de dois títulos, e por isso não têm as suítes novas.

## Decisão: etapa 1 com resumo + texto (e não com as fichas)

| Recorte (Qwen3) | resumo+texto (usado) | fichas (antes) | só resumo | só texto |
|---|---|---|---|---|
| Todas (278) | **73% / 92%** | 72% / 88% | 68% / 92% | 61% / 85% |
| Sintoma em português (60) | 62% / **92%** | **67%** / 83% | 58% / 92% | 45% / 80% |
| Sintoma difícil (52) | **58% / 88%** | 54% / 79% | 52% / 88% | 46% / 81% |
| Suíte do IPA (38, independente) | 50% / 82% | **61% / 84%** | 39% / 79% | 47% / 79% |
| Mari (12, independente) | 83% / **100%** | 83% / 83% | 92% / 100% | 67% / 100% |

- **No geral, resumo + texto empata com as fichas no 1º lugar e ganha entre os 5 primeiros.** O resumo é
  o do catálogo do danluu, escrito por pessoas: não precisa de LLM nem de processo curado.
- **O custo aparece no 1º lugar** das perguntas de sintoma em português (−5 pontos) e da suíte do IPA
  (−11 pontos, ou seja, 4 de 38 perguntas). No top-5, a diferença diminui ou se inverte: 92% contra 83% no
  português e 82% contra 84% no IPA (1 pergunta). Como o agente recebe os 5 primeiros incidentes, a troca
  compensa.
- Nas perguntas próprias, que foram escritas a partir das fichas, a vantagem esperada seria das fichas, mas
  resumo + texto ganha (77% / 94% contra 73% / 89%).
- As fichas continuam no banco como enriquecimento opcional para os agentes.

## Decisão: chunks de texto sem sobreposição

`multiagent_env/bin/python -I ingestion/avaliacao/testar_overlap.py` (Qwen3, 278 perguntas, vetores
gerados na hora). O overlap entra só no texto que vira vetor.

```text
sem overlap (hoje, 450)        chunks  2024  com overlap     0  tokens mediana 318 max 450
A: 450 + 60 mesma seção        chunks  2024  com overlap   856  tokens mediana 335 max 582
B: 390 + 60 mesma seção        chunks  2272  com overlap  1086  tokens mediana 313 max 580
C: 390 + 60 qualquer vizinho   chunks  2272  com overlap  2060  tokens mediana 331 max 580

variante                                                    Todas       Sintoma PT  Sintoma difícil            Causa   (n=278)
A: 450 + 60 mesma seção | só texto                      63% / 86%        48% / 78%        44% / 79%        69% / 91%   MRR 0.726
B: 390 + 60 mesma seção | só texto                      65% / 85%        57% / 78%        54% / 83%        68% / 88%   MRR 0.737
C: 390 + 60 qualquer vizinho | só texto                 65% / 85%        55% / 78%        50% / 81%        71% / 89%   MRR 0.733
sem overlap (hoje, 450) | só texto                      61% / 85%        45% / 80%        46% / 81%        68% / 90%   MRR 0.717
A: 450 + 60 mesma seção | resumo+texto                  74% / 92%        63% / 92%        62% / 88%        81% / 95%   MRR 0.814
B: 390 + 60 mesma seção | resumo+texto                  74% / 92%        65% / 90%        62% / 85%        80% / 95%   MRR 0.809
C: 390 + 60 qualquer vizinho | resumo+texto             76% / 91%        67% / 92%        62% / 87%        82% / 94%   MRR 0.817
sem overlap (hoje, 450) | resumo+texto                  73% / 92%        62% / 92%        58% / 88%        80% / 96%   MRR 0.808
```

- **Com o resumo junto (a busca usada),** sobreposição ganha de 1 a 3 pontos no 1º lugar (73% → 74–76%),
  dentro do ruído, e nada entre os 5 primeiros (92% → 91–92%). As variantes B e C criam 12% mais chunks.
- **Só com o texto,** ela ajuda um pouco mais (61% → 63–65% em 1º lugar). Esse seria o caso de um
  incidente novo ainda sem resumo, mas a solução para ele é gerar o resumo.
- Decisão: **sem sobreposição**, como antes. Agora a escolha se apoia em medição.

## Tabelas completas

```text
Perguntas com resposta (documento esperado entre os primeiros):

## índice: resumo+texto
corte                               qwen3
TODAS              h1 0.73 h5 0.92 mrr 0.81   (n=278)
sintoma            h1 0.66 h5 0.88 mrr 0.75   (n=137)
causa              h1 0.80 h5 0.96 mrr 0.86   (n=137)
sintoma pt         h1 0.62 h5 0.92 mrr 0.73   (n=60)
sintoma en         h1 0.69 h5 0.86 mrr 0.76   (n=77)
sintoma difícil    h1 0.58 h5 0.88 mrr 0.70   (n=52)
IPA (todas)        h1 0.50 h5 0.82 mrr 0.64   (n=38)
própria (todas)    h1 0.77 h5 0.94 mrr 0.83   (n=240)
Mari pt            h1 0.83 h5 1.00 mrr 0.92   (n=6)
Mari en            h1 0.83 h5 1.00 mrr 0.92   (n=6)

## índice: resumo
corte                               qwen3
TODAS              h1 0.68 h5 0.92 mrr 0.78   (n=278)
sintoma            h1 0.58 h5 0.91 mrr 0.71   (n=137)
causa              h1 0.77 h5 0.93 mrr 0.84   (n=137)
sintoma pt         h1 0.58 h5 0.92 mrr 0.71   (n=60)
sintoma en         h1 0.58 h5 0.90 mrr 0.71   (n=77)
sintoma difícil    h1 0.52 h5 0.88 mrr 0.67   (n=52)
IPA (todas)        h1 0.39 h5 0.79 mrr 0.57   (n=38)
própria (todas)    h1 0.73 h5 0.94 mrr 0.82   (n=240)
Mari pt            h1 0.83 h5 1.00 mrr 0.92   (n=6)
Mari en            h1 1.00 h5 1.00 mrr 1.00   (n=6)

## índice: texto
corte                              bge-m3                      e5                   qwen3
TODAS              h1 0.59 h5 0.81 mrr 0.69  h1 0.42 h5 0.64 mrr 0.51  h1 0.61 h5 0.85 mrr 0.72   (n=278)
sintoma            h1 0.47 h5 0.79 mrr 0.60  h1 0.36 h5 0.59 mrr 0.45  h1 0.53 h5 0.80 mrr 0.66   (n=137)
causa              h1 0.69 h5 0.83 mrr 0.76  h1 0.47 h5 0.68 mrr 0.56  h1 0.68 h5 0.90 mrr 0.77   (n=137)
sintoma pt         h1 0.40 h5 0.75 mrr 0.55  h1 0.10 h5 0.33 mrr 0.19  h1 0.45 h5 0.80 mrr 0.60   (n=60)
sintoma en         h1 0.52 h5 0.82 mrr 0.65  h1 0.56 h5 0.79 mrr 0.65  h1 0.60 h5 0.81 mrr 0.70   (n=77)
sintoma difícil    h1 0.40 h5 0.67 mrr 0.53  h1 0.31 h5 0.58 mrr 0.42  h1 0.46 h5 0.81 mrr 0.61   (n=52)
IPA (todas)        h1 0.53 h5 0.79 mrr 0.67  h1 0.39 h5 0.71 mrr 0.54  h1 0.47 h5 0.79 mrr 0.62   (n=38)
própria (todas)    h1 0.60 h5 0.82 mrr 0.69  h1 0.42 h5 0.63 mrr 0.50  h1 0.63 h5 0.86 mrr 0.73   (n=240)
Mari pt                                 —                       —  h1 0.67 h5 1.00 mrr 0.83   (n=6)
Mari en                                 —                       —  h1 0.67 h5 1.00 mrr 0.81   (n=6)

## índice: fichas
corte                              bge-m3                      e5                   qwen3
TODAS              h1 0.63 h5 0.85 mrr 0.73  h1 0.49 h5 0.67 mrr 0.57  h1 0.72 h5 0.88 mrr 0.79   (n=278)
sintoma            h1 0.56 h5 0.82 mrr 0.67  h1 0.42 h5 0.62 mrr 0.51  h1 0.69 h5 0.83 mrr 0.75   (n=137)
causa              h1 0.69 h5 0.87 mrr 0.77  h1 0.55 h5 0.71 mrr 0.62  h1 0.74 h5 0.93 mrr 0.82   (n=137)
sintoma pt         h1 0.58 h5 0.75 mrr 0.67  h1 0.28 h5 0.48 mrr 0.37  h1 0.67 h5 0.83 mrr 0.74   (n=60)
sintoma en         h1 0.55 h5 0.87 mrr 0.67  h1 0.53 h5 0.73 mrr 0.62  h1 0.70 h5 0.83 mrr 0.76   (n=77)
sintoma difícil    h1 0.46 h5 0.77 mrr 0.60  h1 0.37 h5 0.60 mrr 0.46  h1 0.54 h5 0.79 mrr 0.64   (n=52)
IPA (todas)        h1 0.50 h5 0.82 mrr 0.62  h1 0.37 h5 0.63 mrr 0.49  h1 0.61 h5 0.84 mrr 0.70   (n=38)
própria (todas)    h1 0.65 h5 0.85 mrr 0.74  h1 0.51 h5 0.68 mrr 0.58  h1 0.73 h5 0.89 mrr 0.80   (n=240)
Mari pt                                 —                       —  h1 0.83 h5 0.83 mrr 0.83   (n=6)
Mari en                                 —                       —  h1 0.83 h5 0.83 mrr 0.83   (n=6)

## índice: fichas+texto
corte                              bge-m3                      e5                   qwen3
TODAS              h1 0.64 h5 0.86 mrr 0.73  h1 0.48 h5 0.68 mrr 0.57  h1 0.68 h5 0.92 mrr 0.78   (n=278)
sintoma            h1 0.54 h5 0.82 mrr 0.66  h1 0.42 h5 0.60 mrr 0.50  h1 0.63 h5 0.88 mrr 0.74   (n=137)
causa              h1 0.73 h5 0.88 mrr 0.80  h1 0.53 h5 0.74 mrr 0.63  h1 0.73 h5 0.96 mrr 0.82   (n=137)
sintoma pt         h1 0.48 h5 0.82 mrr 0.61  h1 0.20 h5 0.38 mrr 0.30  h1 0.55 h5 0.88 mrr 0.68   (n=60)
sintoma en         h1 0.58 h5 0.83 mrr 0.69  h1 0.58 h5 0.77 mrr 0.66  h1 0.69 h5 0.87 mrr 0.77   (n=77)
sintoma difícil    h1 0.44 h5 0.73 mrr 0.57  h1 0.37 h5 0.58 mrr 0.46  h1 0.52 h5 0.87 mrr 0.66   (n=52)
IPA (todas)        h1 0.55 h5 0.84 mrr 0.69  h1 0.39 h5 0.74 mrr 0.54  h1 0.61 h5 0.89 mrr 0.73   (n=38)
própria (todas)    h1 0.65 h5 0.86 mrr 0.74  h1 0.50 h5 0.67 mrr 0.58  h1 0.70 h5 0.92 mrr 0.79   (n=240)
Mari pt                                 —                       —  h1 1.00 h5 1.00 mrr 1.00   (n=6)
Mari en                                 —                       —  h1 1.00 h5 1.00 mrr 1.00   (n=6)

Sem resposta: maior similaridade (top-1) nas perguntas sem resposta x nas com resposta (índice resumo+texto):
  qwen3    sem resposta: 0.510, 0.552, 0.587, 0.601, 0.653 | com resposta: p10 0.620, mediana 0.702
```
