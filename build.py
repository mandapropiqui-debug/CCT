import re,os,shutil,html
R='/tmp/claude-0/cct'
t=open(R+'/src/template.html').read()
svg=open(R+'/site/logo.svg').read()
paths=re.findall(r'<path id="(p\d)" fill="(#[0-9A-Fa-f]{6})" d="([^"]+)"',svg)
assert len(paths)==6
defs='<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>'
for i,(pid,col,d) in enumerate(paths,1): defs+=f'<path id="d{i}" d="{d}"/>'
defs+='<symbol id="star-color" viewBox="0 0 3696.89 3697.04">'+''.join(f'<use href="#d{i}" fill="{c}" clip-path="url(#nodot)"/>' for i,(p,c,d) in enumerate(paths,1))+'</symbol>'
defs+='<symbol id="star-mono" viewBox="0 0 3696.89 3697.04">'+''.join(f'<use href="#d{i}" fill="currentColor"/>' for i in range(1,7))+'</symbol></defs></svg>'
pos=[(-70,-60,-24,0),(70,-70,28,.4),(-90,40,-30,.8),(80,50,22,1.2),(40,100,-40,1.6),(-40,100,36,2.0)]
petals=''
for i,(p,c,d) in enumerate(paths,1):
    dx,dy,rot,dl=pos[i-1]
    petals+=f'<svg class="pt" viewBox="0 0 3696.89 3697.04" style="--dx:{dx}px;--dy:{dy}px;--rot:{rot}deg;--d:{dl}s"><use href="#d{i}" fill="{c}" clip-path="url(#nodot)"/></svg>'
ICD=R+'/npm/node_modules/@phosphor-icons/core/assets/bold/'
def ic(m):
    n=m.group(1);s=open(ICD+n+'-bold.svg').read()
    s=re.sub(r'<svg ','<svg class="ic" aria-hidden="true" ',s,1)
    return s
tiles=[('feiras','Feiras','uma feira'),('seg-congressos','Congressos','um congresso'),('seg-shows','Shows','um show'),('seg-teatro','Teatro','uma peça ou espetáculo de teatro'),('sociais','Sociais','um evento social'),('seg-formaturas','Formaturas','uma formatura'),('seg-corporativos','Corporativos','um evento corporativo'),('seg-exposicoes','Exposições','uma exposição')]
cls=['l','r','z','r','l','z','l','r']
th=''
for (f,n,w),c in zip(tiles,cls):
    msg={'Feiras':'Oi! Vim pelo biolink do CCT e queria falar sobre fazer uma feira no Centro de Convenções.','Congressos':'Oi! Vim pelo biolink do CCT e queria falar sobre fazer um congresso no Centro de Convenções.','Shows':'Oi! Vim pelo biolink do CCT e queria falar sobre fazer um show no Centro de Convenções.','Teatro':'Oi! Vim pelo biolink do CCT e queria falar sobre fazer uma peça ou espetáculo de teatro no Centro de Convenções.','Sociais':'Oi! Vim pelo biolink do CCT e queria falar sobre fazer um evento social no Centro de Convenções.','Formaturas':'Oi! Vim pelo biolink do CCT e queria falar sobre fazer uma formatura no Centro de Convenções.','Corporativos':'Oi! Vim pelo biolink do CCT e queria falar sobre fazer um evento corporativo no Centro de Convenções.','Exposições':'Oi! Vim pelo biolink do CCT e queria falar sobre fazer uma exposição no Centro de Convenções.'}[n]
    th+=f'<div class="tile rv {c}"><div class="ph"><img src="img/{f}.webp" alt="{n} no Centro de Convenções"></div><div class="bar"><h3>{n}</h3><a class="btn sol sm" data-msg="{msg}" href="#" target="_blank" rel="noopener">{{{{ic:whatsapp-logo}}}}Pedir orçamento</a></div></div>'
strip=[('ceu-da-lingua','O Céu da Língua com Gregório Duvivier'),('louvor-para-jesus','Louvor para Jesus'),('acaiteria-de-elite','Acaíteria de Elite'),('gestao-que-transforma','Gestão que Transforma'),('pre-enem-eja','Pré-Enem EJA'),('g12-evento','Mundo Bita'),('nossa-missao-piaui','Nossa Missão Piauí'),('maratona-piaui-para-o-mundo','Maratona Piauí para o Mundo'),('meia-solidaria','Meia Solidária'),('g20-membros-e-convidados','G20 Brasil 2024'),('semana-do-meio-ambiente','Semana do Meio Ambiente'),('g01-3palavrinhas','3 Palavrinhas'),('g05-evento','Papo Outlet'),('seminario-regional-infancia','Seminário Regional')]
sh=''.join(f'<figure><div class="ph"><img src="img/{f}.webp" alt="{html.escape(n)}"></div><figcaption>{html.escape(n)}</figcaption></figure>' for f,n in strip)
strip2=[('mundo-bita','Mundo Bita no Teatro Mandu'),('g02-3palavrinhas','3 Palavrinhas'),('g20-discussoes','G20 Brasil 2024'),('meia-solidaria-02','Meia Solidária'),('configuracoes-papo-outlet','Papo Outlet'),('g07-evento','Evento no CCT'),('artistas-publico-mandu-02','Show no Teatro Mandu'),('artistas-publico-mandu-04','Público no Teatro Mandu'),('g04-3palavrinhas','3 Palavrinhas')]
sh2=''.join(f'<figure><div class="ph"><img src="img/{f}.webp" alt="{html.escape(n)}"></div><figcaption>{html.escape(n)}</figcaption></figure>' for f,n in strip2)
def vf(r): return ''.join(f'<figure><div class="ph"><img src="img/vc{n:02d}.webp" alt="Visitante no Centro de Convenções"></div></figure>' for n in r)
voce1=vf(range(0,9));voce2=vf(range(9,18))
MAPS='https://www.google.com/maps/search/?api=1&amp;query=Av.+Mal.+Castelo+Branco+1275+Teresina+PI'
WA='https://wa.me/5586988090791'
t=t.replace('{{DEFS}}',defs).replace('{{PETALS}}',petals).replace('{{TILES}}',th).replace('{{STRIP}}',sh).replace('{{STRIP2}}',sh2).replace('{{VOCE1}}',voce1).replace('{{VOCE2}}',voce2).replace('{{MAPS}}',MAPS).replace('{{WA}}',WA)
t=re.sub(r'\{\{ic:([a-z\-]+)\}\}',ic,t)
t=t.replace('.ready .mas,.ready .bub{opacity:1}','.ready .mas{opacity:1}')
t=t.replace('<div class="bg"><i class="conic">','<div class="bg"><i class="gl"></i><i class="conic">').replace('<div class="bg"><i class="blob"','<div class="bg"><i class="gl"></i><i class="blob"')
import base64
def inl(m):
    f=m.group(1);d=open(R+'/site/img/'+f,'rb').read();return 'src="data:image/webp;base64,'+base64.b64encode(d).decode()+'"'
t=re.sub(r'src="img/([a-z0-9\-]+\.webp)"',inl,t)
assert '{{' not in t, re.findall(r'\{\{[^}]+\}\}',t)[:3]
os.makedirs(R+'/dist',exist_ok=True)
open(R+'/dist/index.html','w').write(t)
if os.path.exists(R+'/dist/img'): shutil.rmtree(R+'/dist/img')
shutil.copytree(R+'/site/img',R+'/dist/img',ignore=shutil.ignore_patterns('estrela.png'))
print('ok',len(t)//1024,'KB html')
import glob
from PIL import Image
for f in glob.glob(R+'/dist/img/vista-*.webp'): print(os.path.basename(f),Image.open(f).size)
