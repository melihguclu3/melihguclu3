from pathlib import Path
from html import escape
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
import argparse
p=argparse.ArgumentParser()
p.add_argument('--font',type=Path,required=True)
p.add_argument('--personal',action='store_true')
a=p.parse_args()
ROOT=Path(__file__).resolve().parents[1]
fonts={w:instantiateVariableFont(TTFont(a.font),{'wght':w}) for w in (450,600,750,900)}
def text(s,x,y,size,color,weight=600):
 f=fonts[weight]; gs=f.getGlyphSet(); cmap=f.getBestCmap(); scale=size/f['head'].unitsPerEm; paths=[]; advance=0
 for ch in s:
  glyph=gs[cmap[ord(ch)]]; pen=SVGPathPen(gs); glyph.draw(pen)
  paths.append(f'<path transform="translate({advance},0)" d="{pen.getCommands()}"/>'); advance+=glyph.width
 return f'<g aria-label="{escape(s)}" fill="{color}" transform="translate({x},{y}) scale({scale},-{scale})">'+''.join(paths)+'</g>'
def rect(x,y,w,h,fill,stroke='none',r=0): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}"/>'
def line(x,y,x2,y2,c,width=1):return f'<path d="M{x} {y}L{x2} {y2}" stroke="{c}" stroke-width="{width}" fill="none"/>'
def svg(body,w,h,title,desc):
 return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc><style>
.flow{{stroke-dasharray:12 24;animation:travel 6s linear infinite}}.reveal{{animation:reveal 7s ease-in-out infinite}}.step2{{animation-delay:1s}}.step3{{animation-delay:2s}}
@keyframes travel{{to{{stroke-dashoffset:-144}}}}@keyframes reveal{{0%,100%{{opacity:.35}}25%,75%{{opacity:1}}}}
@media(prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
</style>{body}</svg>'''
def artwork(org,light,tr):
 bg,fg,muted,border,panel=('#f5f7fc','#172235','#536178','#d6deec','#ffffff') if light else ('#0d1420','#f3f6ff','#a3b2ca','#29374d','#142033')
 blue='#3b82f6'; b=rect(0,0,960,420,bg,r=20)
 b+=text('PIKLO STUDIO' if org else 'MELİH GÜÇLÜ  /  PIKLO STUDIO',40,45,15,muted,600)
 b+=line(40,65,920,65,border)
 if org:
  b+=text('piklo',38,208,138,fg,900)+f'<circle cx="420" cy="195" r="12" fill="{blue}"/>'
  b+=text('Tasarım. Yazılım.' if tr else 'Design. Engineering.',40,263,31,fg,750)
  b+=text('Kullanılan ürünler.' if tr else 'Products people use.',40,303,31,blue,750)
 else:
  b+=text('Melih',38,164,85,fg,750)+text('Güçlü',38,252,85,fg,750)
  b+=text('Tasarım gözü. Geliştirici eli.' if tr else 'Design-minded. Hands-on.',40,303,27,blue,600)
 # A studio drawing: a browser and a native app connected to one shared system.
 b+=f'<path d="M420 195 H435 Q452 195 452 212 V322 H833" stroke="{border}" stroke-width="2" fill="none"/>'
 b+=f'<path class="flow" d="M420 195 H435 Q452 195 452 212 V322 H833" stroke="{blue}" stroke-width="2" fill="none"/>'
 b+=rect(494,103,347,192,panel,border,12)+line(494,134,841,134,border)
 for x in (511,522,533): b+=f'<circle cx="{x}" cy="119" r="3" fill="{muted}"/>'
 b+=text('piklo.',551,124,13,fg,900)
 b+=rect(510,150,68,125,bg,r=5)
 for y,w in [(166,40),(183,28),(200,34)]: b+=rect(521,y,w,4,muted,r=2)
 b+=rect(521,246,38,14,blue,r=4)
 for i in range(3):
  b+=f'<g class="reveal step{i+1}">'+rect(593,150+i*38,137,29,bg,border,5)
  b+=rect(604,160+i*38,7,7,blue,r=2)+rect(620,159+i*38,89-i*15,4,muted,r=2)+rect(620,168+i*38,52,3,border,r=1)+'</g>'
 b+=rect(758,164,122,178,bg,border,19)+rect(802,175,33,5,fg,r=3)
 b+=text('pi',773,211,23,fg,900)+f'<circle cx="797" cy="208" r="3" fill="{blue}"/>'
 for i in range(3): b+=f'<g class="reveal step{i+1}">'+rect(770,222+i*26,98,21,panel,border,5)+rect(779,229+i*26,5,5,blue,r=1)+rect(791,230+i*26,58,3,muted,r=1)+'</g>'
 b+=rect(803,328,32,3,muted,r=2)
 b+=line(40,355,920,355,border)
 b+=text('WEB  /  NATIVE iOS  /  AI',40,389,17,fg,600)
 b+=text('AFYONKARAHİSAR, TÜRKİYE',608,389,15,muted,600)
 return svg(b,960,420,'Piklo Studio' if org else 'Melih Güçlü', 'Web, native iOS and AI product development. Animated illustration of connected web and mobile interfaces.')
def card(name,kind,light):
 bg,fg,muted,border=('#f5f7fc','#172235','#536178','#d6deec') if light else ('#101a29','#f3f6ff','#a3b2ca','#29374d')
 b=rect(0,0,400,250,bg,border,16)
 col={'meg':'#f16b3b','pi':'#3b82f6','restaurant':'#d57745'}[kind]
 if kind=='meg':
  for i in range(3):
   b+=rect(28+i*106,32,90,90,'none',border,8)
   for j in range(3): b+=rect(39+i*106,47+j*21,64,12,col if i==j else border,r=3)
 elif kind=='pi':
  b+=rect(28,32,170,38,col,r=19)+rect(213,32,151,38,'none',border,19)
  b+=f'<path d="M44 51h16m-8-8v16" stroke="{bg}" stroke-width="3"/>'
  b+=rect(28,89,58,33,col,r=16)+f'<circle cx="69" cy="105" r="11" fill="{fg}"/>'
  b+=line(111,105,359,105,border,7)+f'<circle cx="213" cy="105" r="9" fill="{col}"/>'
 else:
  for i in range(3):
   b+=rect(28+i*114,32,99,90,'none',border,8)
   b+=rect(38+i*114,43,79,5,col,r=2)
   b+=rect(38+i*114,63,79,40,border,r=4)
 b+=text(name,28,184,38,fg,750)
 b+=text({'meg':'GYM & STUDIO SOFTWARE','pi':'INTERFACE SYSTEM','restaurant':'RESTAURANT OPERATIONS'}[kind],28,219,13,muted,600)
 b+=f'<path d="M351 165h19v19m0-19-23 23" stroke="{col}" stroke-width="3" fill="none"/>'
 return svg(b,400,250,name,'Product illustration; not a live product screenshot.')
out=ROOT/'assets'
out.mkdir(exist_ok=True)
for light in (False,True):
 theme='light' if light else 'dark'
 for tr in (False,True):
  (out/f'hero-{theme}{"-tr" if tr else ""}.svg').write_text(artwork(not a.personal,light,tr))
 for name,kind in [('MEG Spor','meg'),('Pi UI','pi'),('Restaurant','restaurant')]:
  (out/f'{kind}-{theme}.svg').write_text(card(name,kind,light))
