# Avaliação da busca (2026-11-04)

Gerado por `multiagent_env/bin/python -I ingestion/avaliacao/avaliar.py --resumo`. 278 perguntas com resposta e 5 sem resposta (suite_ipa.json + suite_propria.json); h1/h5 = documento esperado em 1º / entre os 5 primeiros; mrr = média de 1/posição.

```text
Perguntas com resposta (documento esperado entre os primeiros):

## índice: fichas
corte                              bge-m3                      e5                   qwen3
TODAS              h1 0.63 h5 0.85 mrr 0.73  h1 0.49 h5 0.67 mrr 0.57  h1 0.72 h5 0.88 mrr 0.79   (n=278)
sintoma            h1 0.56 h5 0.82 mrr 0.67  h1 0.42 h5 0.62 mrr 0.51  h1 0.69 h5 0.83 mrr 0.75   (n=137)
causa              h1 0.69 h5 0.87 mrr 0.77  h1 0.55 h5 0.71 mrr 0.62  h1 0.74 h5 0.93 mrr 0.82   (n=137)
sintoma pt         h1 0.58 h5 0.75 mrr 0.67  h1 0.28 h5 0.48 mrr 0.37  h1 0.67 h5 0.83 mrr 0.74   (n=60)
sintoma en         h1 0.55 h5 0.87 mrr 0.67  h1 0.53 h5 0.73 mrr 0.62  h1 0.70 h5 0.83 mrr 0.76   (n=77)
sintoma difícil    h1 0.46 h5 0.77 mrr 0.60  h1 0.37 h5 0.60 mrr 0.46  h1 0.54 h5 0.79 mrr 0.64   (n=52)
IPA (todas)        h1 0.50 h5 0.82 mrr 0.62  h1 0.37 h5 0.63 mrr 0.49  h1 0.61 h5 0.84 mrr 0.69   (n=38)
própria (todas)    h1 0.65 h5 0.85 mrr 0.74  h1 0.51 h5 0.68 mrr 0.58  h1 0.73 h5 0.89 mrr 0.80   (n=240)

## índice: texto
corte                              bge-m3                      e5                   qwen3
TODAS              h1 0.59 h5 0.81 mrr 0.69  h1 0.42 h5 0.64 mrr 0.51  h1 0.61 h5 0.85 mrr 0.72   (n=278)
sintoma            h1 0.47 h5 0.79 mrr 0.60  h1 0.36 h5 0.59 mrr 0.45  h1 0.54 h5 0.80 mrr 0.66   (n=137)
causa              h1 0.69 h5 0.83 mrr 0.76  h1 0.47 h5 0.68 mrr 0.56  h1 0.67 h5 0.90 mrr 0.76   (n=137)
sintoma pt         h1 0.40 h5 0.75 mrr 0.55  h1 0.10 h5 0.33 mrr 0.19  h1 0.47 h5 0.80 mrr 0.61   (n=60)
sintoma en         h1 0.52 h5 0.82 mrr 0.65  h1 0.56 h5 0.79 mrr 0.65  h1 0.60 h5 0.81 mrr 0.70   (n=77)
sintoma difícil    h1 0.40 h5 0.67 mrr 0.53  h1 0.31 h5 0.58 mrr 0.42  h1 0.46 h5 0.81 mrr 0.61   (n=52)
IPA (todas)        h1 0.53 h5 0.79 mrr 0.67  h1 0.39 h5 0.71 mrr 0.54  h1 0.47 h5 0.79 mrr 0.61   (n=38)
própria (todas)    h1 0.60 h5 0.82 mrr 0.69  h1 0.42 h5 0.63 mrr 0.50  h1 0.63 h5 0.86 mrr 0.73   (n=240)

## índice: fichas+texto
corte                              bge-m3                      e5                   qwen3
TODAS              h1 0.64 h5 0.86 mrr 0.73  h1 0.48 h5 0.68 mrr 0.57  h1 0.69 h5 0.91 mrr 0.78   (n=278)
sintoma            h1 0.54 h5 0.82 mrr 0.66  h1 0.42 h5 0.60 mrr 0.50  h1 0.64 h5 0.88 mrr 0.74   (n=137)
causa              h1 0.73 h5 0.88 mrr 0.80  h1 0.53 h5 0.74 mrr 0.63  h1 0.73 h5 0.95 mrr 0.82   (n=137)
sintoma pt         h1 0.48 h5 0.82 mrr 0.61  h1 0.20 h5 0.38 mrr 0.30  h1 0.57 h5 0.88 mrr 0.69   (n=60)
sintoma en         h1 0.58 h5 0.83 mrr 0.69  h1 0.58 h5 0.77 mrr 0.66  h1 0.69 h5 0.87 mrr 0.77   (n=77)
sintoma difícil    h1 0.44 h5 0.73 mrr 0.57  h1 0.37 h5 0.58 mrr 0.46  h1 0.52 h5 0.87 mrr 0.66   (n=52)
IPA (todas)        h1 0.55 h5 0.84 mrr 0.69  h1 0.39 h5 0.74 mrr 0.54  h1 0.61 h5 0.87 mrr 0.72   (n=38)
própria (todas)    h1 0.65 h5 0.86 mrr 0.74  h1 0.50 h5 0.67 mrr 0.58  h1 0.70 h5 0.92 mrr 0.79   (n=240)

Sem resposta: maior similaridade (top-1) nas perguntas sem resposta x nas com resposta (índice fichas):
  bge-m3   sem resposta: 0.443, 0.482, 0.546, 0.593, 0.688 | com resposta: p10 0.585, mediana 0.643
  e5       sem resposta: 0.760, 0.816, 0.817, 0.821, 0.845 | com resposta: p10 0.804, mediana 0.824
  qwen3    sem resposta: 0.393, 0.538, 0.577, 0.593, 0.630 | com resposta: p10 0.585, mediana 0.674
```
