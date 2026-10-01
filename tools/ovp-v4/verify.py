import re, os, glob, html
from html.parser import HTMLParser
R=os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'ovp-demo-v4')) + os.sep
pages=sorted(glob.glob(R+'**/*.html',recursive=True))
ids={}; problems=[]
class P(HTMLParser):
    def __init__(s): super().__init__(); s.links=[]; s.ids=set(); s.heads=[]; s.imgs=[]; s.scripts=[]
    def handle_starttag(s,t,a):
        a=dict(a)
        if 'id' in a: s.ids.add(a['id'])
        if t=='a' and 'href' in a: s.links.append((a['href'],a))
        if re.fullmatch(r'h[1-6]',t): s.heads.append(int(t[1]))
        if t=='img': s.imgs.append(a)
        if t=='script': s.scripts.append(a.get('src'))
        if t=='link' and a.get('rel')=='stylesheet': s.links.append((a['href'],a))
parsed={}
for f in pages:
    p=P(); p.feed(open(f,encoding='utf8').read()); parsed[f]=p
for f,p in parsed.items():
    rel=f[len(R):]
    if p.heads.count(1)!=1: problems.append(f'{rel}: h1 count {p.heads.count(1)}')
    for a,b in zip(p.heads,p.heads[1:]):
        if b>a+1: problems.append(f'{rel}: heading jump h{a}->h{b}')
    src=open(f,encoding='utf8').read()
    if 'name="robots" content="noindex, nofollow"' not in src: problems.append(rel+': no noindex')
    if '<!--' in src: problems.append(rel+': html comment')
    for s in p.scripts:
        if s and s.startswith('http'): problems.append(rel+': 3rd party script '+s)
    for im in p.imgs:
        if 'alt' not in im: problems.append(rel+': img no alt '+im.get('src',''))
        if not im.get('width'): problems.append(rel+': img no width '+im.get('src',''))
        path=os.path.normpath(os.path.join(os.path.dirname(f),im['src']))
        if not os.path.exists(path): problems.append(rel+': missing img '+im['src'])
    for h,a in p.links:
        if h.startswith('https://fonts.'): continue
        if h.startswith('http'):
            if a.get('rel')!='noopener noreferrer': problems.append(rel+': ext link rel '+h)
            continue
        if h.startswith(('mailto:','tel:')): continue
        path,_,frag=h.partition('#')
        target=os.path.normpath(os.path.join(os.path.dirname(f),path)) if path else f
        if not os.path.exists(target): problems.append(f'{rel}: broken link {h}'); continue
        if frag and target.endswith('.html') and frag not in parsed[target].ids: problems.append(f'{rel}: missing anchor {h}')
print('PAGES',len(pages)); print('\n'.join(problems) or 'NO STRUCTURE/LINK PROBLEMS')
# banned terms (visible + source)
for f in pages:
    t=open(f,encoding='utf8').read()
    for w in [r'prepared',r'\bdemo\b',r'claude',r'\bAI\b',r'TODO',r'proposal',r'concept',r'mockup',r'lorem']:
        for m in re.finditer(w,t,re.I): print('BANNED',f[len(R):],w,t[max(0,m.start()-40):m.end()+40].replace('\n',' '))
# weights
js=os.path.getsize(R+'assets/js/ovp.js'); print('ovp.js bytes',js)
import subprocess
idx=open(R+'index.html').read()
imgs=set(re.findall(r'src="(assets/img/[^"]+)"',idx))
tot=sum(os.path.getsize(R+i) for i in imgs)+os.path.getsize(R+'assets/css/ovp.css')+js+len(idx.encode())
print('home weight KB (excl. Google Fonts ~40KB)', tot//1024)
print('max image KB', max((os.path.getsize(x)//1024,os.path.basename(x)) for x in glob.glob(R+'assets/img/*')))
# placeholders
tbd=set()
for f in pages: tbd|=set(re.findall(r'\[OVP: ([^\]]+)\]',open(f,encoding='utf8').read()))
print('PLACEHOLDERS',len(tbd)); print(sorted(tbd))
