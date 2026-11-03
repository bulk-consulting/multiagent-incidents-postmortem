"""
Monta os pacotes de revisão de um lote para conferência em outro modelo (ex.: ChatGPT).

Para cada ficha do lote gera um único arquivo com o pedido de revisão, o documento
original (extracted_text) e a ficha. Junto vai o prompt de extração sem o comentário
interno. Em cada chat novo anexam-se 2 arquivos: o prompt e o pacote da ficha.

Uso (a partir da raiz do repositório):
    multiagent_env/bin/python ingestion/fichas/montar_revisao.py 01

Lê:
    ingestion/fichas/saida_lotes/lote_NN/DAN-xxx.json
Saída (a pasta é recriada):
    revisao/lote_NN/prompt_extracao.md
    revisao/lote_NN/DAN-xxx_revisao.md
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PASTA = Path(__file__).resolve().parent
EXTRAIDOS = ROOT / "datasets" / "danluu-ingestion" / "data" / "extracted"

PEDIDO = """# Revisão da ficha {cid}

Anexos: `prompt_extracao.md` (regras e definições usadas para gerar a ficha, versão {versao};
ignore o bloco INPUT no final) e este arquivo, que traz o documento original e a ficha.

Revise a ficha contra o documento, seguindo as regras do prompt. Já foi verificado
por programa que todos os "trechos" existem literalmente no documento; não precisa conferir isso.

Para cada campo, diga se está CORRETO, DISCUTÍVEL ou ERRADO, e por quê:
- lendo SÓ os "trechos" daquela afirmação, dá para confirmar todo detalhe do "texto"
  (nomes, datas, números, quem fez, resultados)?
- o "texto" liga fatos com relação de causa que o documento não afirma?
- algo que o documento apresenta como plano ou proposta está escrito como feito?
- a incerteza do original foi mantida?
- os valores escolhidos (status, nivel, categoria_causa, forma, tipo...) seguem as definições do prompt?
- gatilho e causa raiz seguem as definições do prompt?
- confianca: se "baixa", os campos citados em motivo_confianca_baixa têm de fato dois valores
  possíveis pelas regras? se "alta", algum campo deveria ter sido marcado como dúvida?

Depois, liste o que o documento diz de importante e ficou fora da ficha
(fatores, passos de mitigação, ações de prevenção, perguntas em aberto).
Lembre que o prompt diz que a timeline completa fica no texto original, não na ficha.

Não avalie o bloco "extracao" (modelo, data, versão). Não reescreva a ficha.
Responda em português, citando o trecho do documento quando apontar um problema.
No fim, dê uma linha de resumo: "ERRADOS: n | DISCUTÍVEIS: n".

---

## Documento original ({cid})

catalog_id: {cid}
source URL: {url}

````text
{texto}
````

---

## Ficha

```json
{ficha}
```
"""


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    lote = sys.argv[1].zfill(2)
    origem = PASTA / "saida_lotes" / f"lote_{lote}"
    fichas = sorted(origem.glob("DAN-*.json"))
    if not fichas:
        sys.exit(f"Nenhuma ficha em {origem.relative_to(ROOT)}")

    destino = ROOT / "revisao" / f"lote_{lote}"
    destino.mkdir(parents=True, exist_ok=True)
    for velho in destino.iterdir():
        velho.unlink()

    prompt = (PASTA / "prompt_extracao.md").read_text(encoding="utf-8")
    (destino / "prompt_extracao.md").write_text(
        re.sub(r"\A<!--.*?-->\s*", "", prompt, flags=re.S), encoding="utf-8")

    for caminho in fichas:
        ficha = json.loads(caminho.read_text(encoding="utf-8"))
        cid = ficha["catalog_id"]
        doc = json.loads((EXTRAIDOS / f"{cid}.json").read_text(encoding="utf-8"))
        texto = PEDIDO.format(
            cid=cid,
            versao=ficha["extracao"]["versao_prompt"],
            url=doc.get("source_url") or "",
            texto=doc.get("extracted_text") or "",
            ficha=json.dumps(ficha, ensure_ascii=False, indent=2),
        )
        (destino / f"{cid}_revisao.md").write_text(texto, encoding="utf-8")
    print(f"{len(fichas)} pacotes -> {destino.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
