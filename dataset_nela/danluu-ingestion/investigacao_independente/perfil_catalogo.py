import re,sys,collections,statistics as st
from urllib.parse import urlparse
lines=open(sys.argv[1],encoding='utf-8').read().split('\n')
sec=None; E=[]; other=[]
for l in lines:
    m=re.match(r'^## (.+)',l)
    if m: sec=m.group(1).strip(); continue
    m=re.match(r'^\[([^\]]+)\]\((\S+?)\)\.?\s*(.*)',l)
    if m and sec:
        E.append(dict(sec=sec,co=m.group(1),url=m.group(2),txt=m.group(3)))
C=collections.Counter
print("entradas por seção:",C(e['sec'] for e in E))
inc=[e for e in E if e['sec'] not in('Other lists of postmortems','Analysis','Contributors')]
print("\nincidentes (sem listas/análises):",len(inc))
print("empresas distintas:",len({e['co'] for e in inc}))
print("top empresas:",C(e['co'] for e in inc).most_common(15))
dom=lambda u: urlparse(u).netloc.replace('www.','')
print("\nlinks via web.archive.org:",sum('web.archive.org' in e['url'] for e in inc))
print("top domínios:",C(dom(e['url']) for e in inc).most_common(15))
w=[len(e['txt'].split()) for e in inc]
print("\npalavras no resumo: mediana",st.median(w),"| min",min(w),"| max",max(w),"| <15 palavras:",sum(x<15 for x in w))
yrs=C()
for e in inc:
    y=re.findall(r'(?<!\d)(19[89]\d|20[0-2]\d)(?!\d)',e['url']+' '+e['txt'])
    yrs[max(y) if y else 'sem ano']+=1
print("ano (inferido de URL/texto):",sorted(yrs.items(),key=lambda x:str(x[0])))
kw={'kubernetes|k8s':0,'postgres|mysql|database|db':0,'dns':0,'bgp|rout':0,'config':0,'certificate|cert':0,'retry|retries':0,'disk|storage|volume':0,'deploy':0}
for k in kw: kw[k]=sum(bool(re.search(k,e['txt'],re.I)) for e in inc)
print("menções no resumo:",kw)
import json; json.dump(inc,open('danluu_entradas.json','w'),ensure_ascii=False,indent=1)
