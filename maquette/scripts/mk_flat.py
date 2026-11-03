import os
MAQ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APERCU = os.environ.get("APERCU", os.path.join(MAQ, "apercu"))
os.makedirs(APERCU, exist_ok=True)
p=os.path.join(MAQ, 'index.html'); s=open(p).read()
def r(a,b):
    global s
    assert a in s, 'MISSING: '+a[:80]; s=s.replace(a,b)
r('<title>Azarias Sawadogo</title>','<title>Azarias Sawadogo — flat</title>')
flat = """
  /* ===== Variante flat : aplats de couleur, aucune ombre, aucun relief, formes nettes ===== */
  :root { --rayon-sm: 6px; --rayon-md: 8px; --rayon-lg: 10px; --rayon-xl: 12px; --halo-scene: transparent; }
  *, *::before, *::after { box-shadow: none !important; text-shadow: none !important; }
  .btn { border-radius: var(--rayon-md); }
  .btn.second { border: 0; background: var(--surface); }
  .btn.second:hover { background: var(--surface-2); }

  /* Le portrait : posé sur un aplat d'accent décalé, sans halo ; il s'incline toujours au pointeur */
  .scene::before { inset: 24px -24px -24px 24px; background: var(--accent); border-radius: var(--rayon-xl); }
  .portrait img { border-radius: var(--rayon-xl); }

  /* Chaque écran a son aplat */
  #apropos, #parcours { background: var(--fond); }
  .outil, .pile span, .carte, .reseau, .courriel { background: var(--surface); }
  .outil:hover, a.reseau:hover { background: var(--surface-2); }

  /* Filigranes pleins, sans contour */
  .filigrane { -webkit-text-stroke: 0; color: var(--surface); }
  #apropos .filigrane, #parcours .filigrane { color: var(--surface-2); }

  /* Contact : un grand aplat d'accent */
  #contact {
    background: var(--accent); color: var(--sur-accent);
    --page: #1d5a4e; --fond: #1d5a4e; --surface: #256b5e; --surface-2: #2e7d6c; --filet: #2e7d6c;
    --texte: #e6f4f0; --texte-attenue: #c4e3da; --texte-discret: #a9d4c8; --accent-texte: #e6f4f0;
  }
  #contact .filigrane { color: #22665a; }
  #contact .barre { color: #7ccbb7; }
  #contact .btn.principal { background: #e6f4f0; color: #1d5a4e; }
  #contact .btn.principal:hover { background: #ffffff; }
  #contact .copier { border-color: #e6f4f0; color: #e6f4f0; }
  #contact .copier:hover { background: #2e7d6c; }
  #contact .reseau .action { color: #e6f4f0; text-decoration: underline; text-underline-offset: 4px; }
  #contact footer { border-top-color: #2e7d6c; }

  /* Fenêtres et schémas en aplats */
  dialog.fiche, dialog.fiche-projet { border: 0; }
  .schema .n { stroke: none; fill: var(--surface-2); }
  .fp-schema { background: var(--fond); }

  /* Repères : carrés pleins */
  .points button::before { border-radius: 1px; }
"""
r('</style>', flat + '</style>')
# Transition flat : une poussée nette, sans réduction, ni assombrissement, ni coins arrondis
r("""      { transform: 'translateY(0) scale(1)', opacity: 1, filter: 'brightness(1)' },
      { transform: `translateY(${-18 * sens}%) scale(.94)`, opacity: .4, filter: 'brightness(.6)' }""",
  """      { transform: 'translateY(0)' },
      { transform: `translateY(${-100 * sens}%)` }""")
r("""      { transform: `translateY(${100 * sens}%)`, borderRadius: sens > 0 ? '26px 26px 0 0' : '0 0 26px 26px' },
      { transform: 'translateY(0)', borderRadius: '0' }""",
  """      { transform: `translateY(${100 * sens}%)` },
      { transform: 'translateY(0)' }""")
r("const duree = 950, courbe = 'cubic-bezier(.7, 0, .2, 1)';","const duree = 560, courbe = 'cubic-bezier(.65, 0, .35, 1)';")
r("setTimeout(() => { verrou = false; }, 250);","setTimeout(() => { verrou = false; }, 60);")
r("if (Math.abs(cumul) > 40) { cumul = 0; aller(courant + sens); }","if (Math.abs(cumul) > 24) { cumul = 0; aller(courant + sens); }")
r("if (performance.now() - dernierDefilement < 350) return;","if (performance.now() - dernierDefilement < 220) return;")
r("setTimeout(() => apres.classList.remove('attente'), duree * .55);","setTimeout(() => apres.classList.remove('attente'), duree * .4);")
open(os.path.join(MAQ, 'flat.html'),'w').write(s)
# aperçu
import re
a=re.sub(r'<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport"[^>]*>\n','',s)
a=a.replace('<title>Azarias Sawadogo — flat</title>','<title>Portfolio Azarias flat</title>\n<meta name="claude:viewport-fit-sides" content="cover">')
a=a.replace('</style>\n</head>\n<body>','</style>').replace('</body>\n</html>\n','')
a=a.replace('../src/assets/azarias.jpg','azarias.jpg').replace('../public/CV-Azarias-Sawadogo-2026.pdf','cv.pdf')
assert '<head>' not in a
open(os.path.join(APERCU, 'portfolio-flat.html'),'w').write(a)
print('ok')
