"""
Reextrai o texto dos documentos do danluu que a extração original (trafilatura) estragou:
intertítulos perdidos, atualizações de Statuspage perdidas e listas dentro de tabelas.

Parte do HTML já baixado em datasets/danluu-ingestion/data/raw/ (só leitura; nada em
datasets/ é alterado). Dados baixados não são confiáveis: o HTML só é analisado como texto,
nada dele é executado.

Regras de saída (texto simples, parecido com Markdown):
- h1..h6 viram "## título" numa linha própria;
- itens de lista viram "- item";
- linhas de tabela viram as células separadas por " | ";
- páginas de Statuspage: o resumo/postmortem e depois cada atualização como
  "## <status>" + texto + "Posted <data>", na ordem da página (mais nova primeiro);
- menus, rodapés, scripts, formulários e blocos de "related posts" são descartados.

Uso (a partir da raiz do repositório):
    multiagent_env/bin/python -I ingestion/reextracao/reextrair.py            # todos da lista
    multiagent_env/bin/python -I ingestion/reextracao/reextrair.py DAN-053    # só os citados

Os documentos do gabarito (DAN-053, DAN-183) não são reextraídos: o lote 00 é teste de
regressão e precisa receber sempre a mesma entrada.

Lê:    ingestion/reextracao/lista.csv, datasets/danluu-ingestion/data/{raw,extracted}/
Grava: ingestion/reextracao/extraidos/DAN-xxx.json
       ingestion/reextracao/checagem.csv
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup, Comment, NavigableString, Tag
from bs4.element import Declaration, Doctype, ProcessingInstruction

NAO_TEXTO = (Comment, Doctype, Declaration, ProcessingInstruction)

ROOT = Path(__file__).resolve().parents[2]
PASTA = Path(__file__).resolve().parent
DANLUU = ROOT / "datasets" / "danluu-ingestion" / "data"
SAIDA = PASTA / "extraidos"

DESCARTAR = {"script", "style", "noscript", "nav", "footer", "form", "aside", "svg",
             "button", "iframe", "template", "select", "input", "header"}
# classes/ids de blocos que não são o artigo
LIXO = re.compile(r"(^|[-_ ])(nav|navbar|menu|footer|sidebar|share|social|related|comment|"
                  r"newsletter|subscribe|cookie|breadcrumb|banner|signup|author-bio|"
                  r"further-reading|post-meta|tags|modal)([-_ ]|$)", re.I)
# blocos que nunca são artigo (Wikipedia e afins)
REMOVER = (".navbox, .reflist, .references, .mw-editsection, .catlinks, .metadata, #toc, .toc, "
           "sup.reference, .mw-jump-link, .noprint, .sr-only, .visually-hidden")
# intertítulo a partir do qual o resto é rodapé (só vale na segunda metade do texto)
RODAPE = re.compile(r"^(written by|tags:?|related (posts|articles|stories)|more from .*|share( this)?( post| article)?|"
                    r"about the authors?|you may also like|explore more|categories|references|see also|"
                    r"external links|further reading|notes|recent posts|read more|keep reading|ready to get started\??|"
                    r"we.d love to talk to you about|we.re hiring.*|all categories|over \d[\d,]* businesses .*|"
                    r"so good, you.ll break things on purpose|see related articles)$", re.I)
BLOCOS = {"p", "li", "tr", "pre", "blockquote", "h1", "h2", "h3", "h4", "h5", "h6",
          "dt", "dd", "figcaption"}
# contêineres conhecidos, em ordem de preferência
SELETORES = ["#mw-content-text .mw-parser-output", ".incident-updates-container", ".post .cooked", ".cooked", ".post__content",
             ".entry-content", ".post-content", ".article-content", ".markdown-body",
             "article", "main", "#maia-main", ".post"]


def limpo(t: str) -> str:
    return re.sub(r"\s+", " ", t.replace("\xa0", " ")).strip()


def eh_lixo(el: Tag) -> bool:
    if el.name in DESCARTAR:
        return True
    rotulo = " ".join(el.get("class") or []) + " " + (el.get("id") or "")
    return bool(LIXO.search(rotulo)) and el.name not in ("body", "html", "main", "article")


def texto_de(el: Tag) -> str:
    partes = []
    for d in el.descendants:
        if isinstance(d, NavigableString) and not isinstance(d, NAO_TEXTO) and not any(
                isinstance(p, Tag) and p.name in DESCARTAR for p in d.parents):
            partes.append(str(d))
        elif isinstance(d, Tag) and d.name == "br":
            partes.append(" ")
    return limpo("".join(partes))


def linhas(el: Tag) -> list[str]:
    """Percorre o elemento e devolve uma linha por bloco (sem repetir texto aninhado)."""
    saida: list[str] = []

    def visita(no: Tag) -> None:
        for filho in no.children:
            if not isinstance(filho, Tag):
                if isinstance(filho, NAO_TEXTO):
                    continue
                t = limpo(str(filho))
                if t and no.name not in BLOCOS:
                    saida.append(t)
                continue
            if eh_lixo(filho):
                continue
            n = filho.name
            if n in ("h1", "h2", "h3", "h4", "h5", "h6"):
                t = texto_de(filho).lstrip("#¶ ").strip()
                if t:
                    saida.append("## " + t)
            elif n == "tr":
                cel = [texto_de(c) for c in filho.find_all(["td", "th"], recursive=False)]
                cel = [c for c in cel if c]
                if cel:
                    saida.append(" | ".join(cel))
            elif n == "li":
                # item com sublista: texto próprio na linha, sublista depois
                sub = filho.find(["ul", "ol"])
                if sub:
                    proprio = limpo("".join(texto_de(c) if isinstance(c, Tag) else str(c)
                                            for c in filho.children if c is not sub
                                            and not (isinstance(c, Tag) and c.find(["ul", "ol"]))))
                    if proprio:
                        saida.append("- " + proprio)
                    visita(sub)
                else:
                    t = texto_de(filho)
                    if t:
                        saida.append("- " + t)
            elif n == "pre":
                t = filho.get_text().strip("\n")
                if t.strip():
                    saida.append(t)
            elif n in ("p", "blockquote", "dt", "dd", "figcaption"):
                if filho.find(["p", "ul", "ol", "table", "pre", "h2", "h3", "h4"]):
                    visita(filho)
                else:
                    t = texto_de(filho)
                    if t:
                        saida.append(t)
            else:
                visita(filho)

    visita(el)
    # junta pedaços soltos de texto inline consecutivos que não são blocos
    return [l for l in saida if l]


def pontuacao(el: Tag) -> int:
    return sum(len(texto_de(p)) for p in el.find_all(["p", "li", "pre"]))


def conteiner(sopa: BeautifulSoup) -> Tag:
    for sel in SELETORES:
        achados = sopa.select(sel)
        if achados:
            el = max(achados, key=pontuacao)
            if pontuacao(el) > 300:
                return el
    # sem contêiner conhecido: o menor elemento que guarda ≥ 80% do texto de parágrafos
    corpo = sopa.body or sopa
    total = pontuacao(corpo)
    el = corpo
    while True:
        filhos = [f for f in el.find_all(recursive=False) if isinstance(f, Tag) and not eh_lixo(f)]
        melhor = max(filhos, key=pontuacao, default=None)
        if melhor is None or pontuacao(melhor) < 0.8 * total:
            return el
        el = melhor


def statuspage(sopa: BeautifulSoup) -> list[str] | None:
    linhas_upd = sopa.select(".update-row")
    if not linhas_upd:
        return None
    saida = []
    titulo = sopa.select_one(".incident-name") or sopa.find("h1")
    if titulo:
        saida.append("## " + texto_de(titulo))
    impacto = sopa.select_one(".incident-impact, .page-title .impact")
    for row in linhas_upd:
        status = row.select_one(".update-title, h2")
        corpo = row.select_one(".update-body, .markdown-display, .whitespace-pre-wrap") or row
        data = row.select_one(".update-timestamp, small")
        saida.append("## " + (texto_de(status) if status else "Update"))
        saida.extend(l for l in linhas(corpo) if not (status and l == "## " + texto_de(status)))
        if data:
            saida.append(texto_de(data))
    rodape = sopa.select_one(".components-affected, .incident-affected-components")
    if rodape:
        saida.append(texto_de(rodape))
    return saida


def google(sopa: BeautifulSoup) -> list[str] | None:
    """Painel de status do Google Cloud: tabela de atualizações com data, hora e descrição."""
    tabela = sopa.select_one("table.updates, table.status-updates")
    if not tabela:
        return None
    saida = []
    titulo = sopa.select_one("h2.incident-description")
    if not titulo:
        titulo = next((h for h in sopa.find_all("h1") if "Incident #" in texto_de(h)), None)
    if titulo:
        saida.append("## " + texto_de(titulo))
        # subtítulo do formato antigo (ex.: "502 errors for HTTP(S) Load Balancers")
        for sub in titulo.find_next_siblings("div", class_="secondary"):
            if not texto_de(sub).startswith("Incident began"):
                saida.append(texto_de(sub))
    for p in sopa.find_all("p"):
        t = texto_de(p)
        if t.startswith(("Incident affecting", "Incident began at")):
            saida.append(t)
    for tr in tabela.find_all("tr"):
        desc = tr.select_one(".description")
        if desc is None or desc.name == "th":
            continue
        data = tr.select_one(".date")
        hora = tr.select_one(".time")
        cab = " ".join(texto_de(x) for x in (data, hora) if x is not None)
        saida.append("## Update" + (f" — {cab}" if cab else ""))
        saida.extend(linhas(desc))
    # locais/produtos afetados ficam fora da tabela no formato novo
    for bloco in sopa.select("h3"):
        if "affected" in texto_de(bloco).lower():
            saida.append("## " + texto_de(bloco))
            irmao = bloco.find_next_sibling()
            if irmao is not None:
                saida.extend(linhas(irmao) or [texto_de(irmao)])
    return saida


def cortar_rodape(ls: list[str]) -> list[str]:
    for i, l in enumerate(ls):
        if i > len(ls) // 2 and l.startswith("## ") and RODAPE.match(l[3:].strip()):
            return ls[:i]
    return ls


def dedup(ls: list[str]) -> list[str]:
    """Remove linhas longas repetidas (mesmo parágrafo várias vezes na página)."""
    vistos, out = set(), []
    for l in ls:
        chave = l if len(l) > 60 else None
        if chave and chave in vistos:
            continue
        if chave:
            vistos.add(chave)
        out.append(l)
    return out


def reextrair(cid: str) -> dict:
    html = (DANLUU / "raw" / f"{cid}.html").read_text(encoding="utf-8", errors="replace")
    sopa = BeautifulSoup(html, "html.parser")
    for el in sopa.select(REMOVER):
        el.decompose()
    ls, metodo = statuspage(sopa), "bs4-statuspage"
    if ls is None:
        ls, metodo = google(sopa), "bs4-google-status"
    if ls is None:
        ls, metodo = cortar_rodape(linhas(conteiner(sopa))), "bs4-blocos"
    ls = dedup(ls)
    texto = "\n\n".join(ls)
    antigo = json.loads((DANLUU / "extracted" / f"{cid}.json").read_text(encoding="utf-8"))
    return {
        "catalog_id": cid,
        "source_url": antigo.get("source_url"),
        "final_url": antigo.get("final_url"),
        "title": antigo.get("title"),
        "company": antigo.get("company"),
        "extraction_method": metodo,
        "extracted_text": texto,
        "word_count": len(texto.split()),
        "texto_antigo_palavras": len((antigo.get("extracted_text") or "").split()),
    }


def ngramas(t: str, n: int = 5) -> set[tuple[str, ...]]:
    p = re.findall(r"\w+", t.lower())
    return {tuple(p[i:i + n]) for i in range(len(p) - n + 1)}


def checar(doc: dict) -> dict:
    antigo = json.loads((DANLUU / "extracted" / f"{doc['catalog_id']}.json").read_text(encoding="utf-8"))
    a, b = ngramas(antigo.get("extracted_text") or ""), ngramas(doc["extracted_text"])
    cobertura = len(a & b) / len(a) if a else 1.0
    novos = len(b - a) / len(b) if b else 0.0
    t = doc["extracted_text"]
    return {
        "catalog_id": doc["catalog_id"],
        "metodo": doc["extraction_method"],
        "palavras_antes": doc["texto_antigo_palavras"],
        "palavras_depois": doc["word_count"],
        "cobertura_antigo": f"{cobertura:.3f}",
        "fracao_nova": f"{novos:.3f}",
        "titulos": len(re.findall(r"^## ", t, re.M)),
        "itens_lista": len(re.findall(r"^- ", t, re.M)),
        "linhas_tabela": len(re.findall(r"^[^\n]* \| [^\n]*$", t, re.M)),
    }


def main() -> None:
    lista = [r["catalog_id"] for r in csv.DictReader((PASTA / "lista.csv").open(encoding="utf-8"))
             if r["grupo"] != "sem_artigo"]
    alvo = sys.argv[1:] or lista
    # documentos do gabarito ficam com o texto original: o lote 00 é teste de regressão
    # e precisa receber sempre a mesma entrada
    gabarito = {p.stem for p in (ROOT / "ingestion" / "fichas" / "gabarito").glob("DAN-*.json")}
    for cid in sorted(set(alvo) & gabarito):
        print(f"{cid}: no gabarito, fica com o texto original (não reextraído)")
        (SAIDA / f"{cid}.json").unlink(missing_ok=True)
    alvo = [c for c in alvo if c not in gabarito]
    SAIDA.mkdir(exist_ok=True)
    linhas_chk = []
    for cid in alvo:
        doc = reextrair(cid)
        (SAIDA / f"{cid}.json").write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n",
                                           encoding="utf-8")
        linhas_chk.append(checar(doc))
    if not sys.argv[1:]:
        with (PASTA / "checagem.csv").open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(linhas_chk[0]))
            w.writeheader()
            w.writerows(linhas_chk)
    for r in linhas_chk:
        print(" ".join(f"{k}={v}" for k, v in r.items()))


if __name__ == "__main__":
    main()
