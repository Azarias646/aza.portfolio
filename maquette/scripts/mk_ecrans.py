import os
MAQ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APERCU = os.environ.get("APERCU", os.path.join(MAQ, "apercu"))
os.makedirs(APERCU, exist_ok=True)
import re
s=open(os.path.join(MAQ, 'flat.html')).read()
def r(a,b):
    global s
    assert a in s, 'MISSING: '+a[:80]; s=s.replace(a,b)
r('<title>Azarias Sawadogo — flat</title>','<title>Azarias Sawadogo — écrans et fondu</title>')
r("document.querySelectorAll('.projets, .parcours > div, .outils, .canaux')","document.querySelectorAll('.projets, .parcours > div, .outils, .canaux, .recit')")
r('<h1>Azarias<br>Sawadogo</h1>','<h1><span class="ligne-nom">Azarias</span><span class="ligne-nom">Sawadogo</span></h1>')
r('</style>',"""
  /* ===== Variante écrans + fondu : après le changement d'écran, le contenu apparaît en fondu doux, élément par élément ===== */
  section .tete h2 { transition: opacity 1100ms cubic-bezier(.25, .1, .25, 1) 120ms, transform 1300ms cubic-bezier(.2, .8, .2, 1) 120ms; }
  section .filigrane { transition: opacity 1800ms cubic-bezier(.25, .1, .25, 1); }
  section .tete ~ :not(.projets, .parcours, .canaux, .apropos) { transition: opacity 1100ms cubic-bezier(.25, .1, .25, 1) 300ms, transform 1300ms cubic-bezier(.2, .8, .2, 1) 300ms; }
  .cascade { transition: opacity 1100ms cubic-bezier(.25, .1, .25, 1), transform 1300ms cubic-bezier(.2, .8, .2, 1); transition-delay: calc(260ms + var(--i, 0) * 110ms); }
  .groupe.cascade, .recit .cascade { transition-delay: calc(260ms + var(--i, 0) * 110ms); }
  .anime section.attente .tete h2 { opacity: 0; transform: translateY(14px); clip-path: none; }
  .anime section.attente .filigrane { opacity: 0; translate: 0 0; }
  .anime section.attente .tete ~ :not(.projets, .parcours, .canaux, .apropos) { opacity: 0; transform: translateY(14px); }
  .anime section.attente .cascade { opacity: 0; transform: translateY(14px); }
  /* Le nom : fondu doux ligne par ligne, à l'ouverture et à chaque retour sur l'écran d'accueil */
  .ligne-nom { display: block; transition: opacity 1100ms cubic-bezier(.25, .1, .25, 1) 150ms, transform 1300ms cubic-bezier(.2, .8, .2, 1) 150ms;
    animation: nom-fondu 1300ms cubic-bezier(.2, .8, .2, 1) 200ms backwards; }
  .ligne-nom + .ligne-nom { transition-delay: 300ms; animation-delay: 360ms; }
  @keyframes nom-fondu { from { opacity: 0; transform: translateY(14px); } }
  .anime section.attente .ligne-nom { opacity: 0; transform: translateY(14px); }
</style>""")
open(os.path.join(MAQ, 'ecrans-fondu.html'),'w').write(s)
a=re.sub(r'<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport"[^>]*>\n','',s)
a=a.replace('<title>Azarias Sawadogo — écrans et fondu</title>','<title>Portfolio Azarias écrans fondu</title>\n<meta name="claude:viewport-fit-sides" content="cover">')
a=a.replace('</style>\n</head>\n<body>','</style>').replace('</body>\n</html>\n','')
a=a.replace('  nav { position: sticky;','  body::before { content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 10; background: var(--page); }\n  nav { position: sticky;',1)
a=a.replace('../src/assets/azarias.jpg','azarias.jpg').replace('../public/CV-Azarias-Sawadogo-2026.pdf','cv.pdf')
assert '<head>' not in a
open(os.path.join(APERCU, 'portfolio-ecrans-fondu.html'),'w').write(a)
print('ok')
