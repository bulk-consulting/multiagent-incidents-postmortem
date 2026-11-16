import sys,json,re,subprocess,os,html
from bs4 import BeautifulSoup
base=sys.argv[1]; out=sys.argv[2]; os.makedirs(out,exist_ok=True)
def norm(s): return re.sub(r'[^a-z0-9 ]','',re.sub(r'\s+',' ',s.lower())).strip()
def sents(t): return [s.strip() for s in re.split(r'(?<=[.!?])\s+|\n+',t) if len(s.split())>=8]
rows=[]
for f in sorted(os.listdir(f'{base}/data/extracted')):
    cid=f[:-5]; X=json.load(open(f'{base}/data/extracted/{f}'))
    tr=X.get('extracted_text') or ''
    raw_pdf=f'{base}/data/raw/{cid}.pdf'; raw_html=f'{base}/data/raw/{cid}.html'
    if os.path.exists(raw_pdf):
        ind=subprocess.run(['pdftotext','-layout',raw_pdf,'-'],capture_output=True,text=True).stdout; how='pdftotext'
    else:
        soup=BeautifulSoup(open(raw_html,'rb').read(),'lxml')
        for t in soup(['script','style','noscript','nav','header','footer','aside','form','svg','iframe']): t.decompose()
        cands=[n for n in (soup.find('article'),soup.find('main'),soup.body,soup) if n is not None]
        node=next((n for n in cands if len(n.get_text(' ').split())>=150),cands[-1])
        how='bs4:'+node.name
        ind=node.get_text('\n')
        ind=re.sub(r'\n\s*\n+','\n\n',re.sub(r'[ \t]+',' ',ind)).strip()
    open(f'{out}/{cid}.txt','w').write(ind)
    A={norm(s) for s in sents(ind)}; B={norm(s) for s in sents(tr)}
    rec=len(A&B)/len(A) if A else 0; prec=len(A&B)/len(B) if B else 0
    hangul=len(re.findall(r'[가-힣]',tr))
    rows.append((cid,how,len(ind.split()),len(tr.split()),round(rec,2),round(prec,2),hangul,X.get('title','')[:60] if X.get('title') else ''))
    miss=[s for s in sents(ind) if norm(s) not in B]; extra=[s for s in sents(tr) if norm(s) not in A]
    json.dump({'missing_in_pipeline':miss,'extra_in_pipeline':extra},open(f'{out}/{cid}.diff.json','w'),ensure_ascii=False,indent=0)
print(f"{'id':8} {'método':12} {'pal.indep':>9} {'pal.pipe':>8} {'cobert':>6} {'precis':>6} {'hangul':>6}  título")
for r in rows: print(f"{r[0]:8} {r[1]:12} {r[2]:9} {r[3]:8} {r[4]:6} {r[5]:6} {r[6]:6}  {r[7]}")
