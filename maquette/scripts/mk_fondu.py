import os
MAQ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APERCU = os.environ.get("APERCU", os.path.join(MAQ, "apercu"))
os.makedirs(APERCU, exist_ok=True)
import re
s=open(os.path.join(MAQ, 'flat.html')).read()
def r(a,b):
    global s
    assert a in s, 'MISSING: '+a[:80]; s=s.replace(a,b)
r('<title>Azarias Sawadogo — flat</title>','<title>Azarias Sawadogo — fondu</title>')
r('</style>',"""
  /* ===== Variante fondu : défilement continu, les blocs apparaissent en fondu au rythme du défilement ===== */
  html, body { height: auto; overflow: visible; }
  body { display: block; }
  .diapos { position: static; overflow: visible; }
  .diapo { position: relative; inset: auto; overflow: visible; visibility: visible; display: block; padding-block: 112px; }
  #accueil { padding-block: 72px 112px; }
  nav { position: sticky; top: env(safe-area-inset-top, 0px); }
  .points { display: none; }
  .fondu { opacity: var(--o, 1); transform: translateY(calc((1 - var(--o, 1)) * 32px)); transition: opacity 1400ms cubic-bezier(.25, .1, .25, 1) var(--d, 0ms), transform 1600ms cubic-bezier(.2, .8, .2, 1) var(--d, 0ms); will-change: opacity, transform; }
</style>""")
# remplace la navigation par écrans par l'apparition en fondu
s=re.sub(r"  // Navigation par écrans : chaque geste de défilement amène la section suivante\n.*?document\.querySelector\('\.marque'\)\.addEventListener\('click', e => \{ e\.preventDefault\(\); aller\(0\); \}\);\n",
"""  // Apparition en fondu : chaque bloc se révèle lentement en entrant dans l'écran,
  // les blocs qui entrent ensemble apparaissent l'un après l'autre
  const blocs = [...document.querySelectorAll('.diapo:not(#accueil) .tete, .recit p, .groupe, .projet, .etape, .colonne, .courriel, .reseau, .contact footer')];
  if (!reduit && 'IntersectionObserver' in window) {
    let lot = [], minuterie = null;
    const io = new IntersectionObserver(entrees => {
      entrees.filter(e => e.isIntersecting).forEach(e => { lot.push(e.target); io.unobserve(e.target); });
      clearTimeout(minuterie);
      minuterie = setTimeout(() => {
        lot.sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top || a.getBoundingClientRect().left - b.getBoundingClientRect().left)
           .forEach((b, i) => { b.style.setProperty('--d', (i * 140) + 'ms'); b.style.setProperty('--o', 1); });
        lot = [];
      }, 30);
    }, { threshold: .15, rootMargin: '0px 0px -10% 0px' });
    blocs.forEach(b => { b.classList.add('fondu'); b.style.setProperty('--o', 0); io.observe(b); });
  }

  // Menu : surligne la section en cours de lecture
  const liensNav = [...document.querySelectorAll('.liens a')];
  const espion = new IntersectionObserver(entrees => entrees.forEach(e => {
    if (e.isIntersecting) liensNav.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + e.target.id));
  }), { rootMargin: '-45% 0px -50% 0px' });
  document.querySelectorAll('.diapo').forEach(d => espion.observe(d));
""", s, count=1, flags=re.S)
assert 'aller(' not in s, 'reste de la navigation par écrans'
open(os.path.join(MAQ, 'fondu.html'),'w').write(s)
a=re.sub(r'<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport"[^>]*>\n','',s)
a=a.replace('<title>Azarias Sawadogo — fondu</title>','<title>Portfolio Azarias fondu</title>\n<meta name="claude:viewport-fit-sides" content="cover">')
a=a.replace('</style>\n</head>\n<body>','</style>').replace('</body>\n</html>\n','')
a=a.replace('../src/assets/azarias.jpg','azarias.jpg').replace('../public/CV-Azarias-Sawadogo-2026.pdf','cv.pdf')
a=a.replace('  nav { position: sticky; top: env(safe-area-inset-top, 0px); }','  body::before { content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 10; background: var(--page); }\n  nav { position: sticky; top: env(safe-area-inset-top, 0px); }')
open(os.path.join(APERCU, 'portfolio-fondu.html'),'w').write(a)
print('ok')
