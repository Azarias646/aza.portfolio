import os
MAQ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APERCU = os.environ.get("APERCU", os.path.join(MAQ, "apercu"))
os.makedirs(APERCU, exist_ok=True)
import re
s=open(os.path.join(MAQ, 'ecrans-fondu.html')).read()
def r(a,b):
    global s
    assert a in s, 'MISSING: '+a[:80]; s=s.replace(a,b)
r('<title>Azarias Sawadogo — écrans et fondu</title>','<title>Azarias Sawadogo — widgets</title>')

# Fenêtre d'un outil : jauge en demi-cercle à la place des trois barres
r('<div class="niveau-ligne"><span class="petit">Mon niveau</span><strong id="fiche-niveau"></strong></div>\n        <div class="crans" id="fiche-crans" aria-hidden="true"><i></i><i></i><i></i></div>',
  """<div class="jauge">
          <svg viewBox="0 0 220 142" aria-hidden="true">
            <path class="jauge-fond" d="M22 110 A88 88 0 0 1 198 110"/>
            <path class="jauge-valeur" id="jauge-valeur" d="M22 110 A88 88 0 0 1 198 110"/>
            <line class="jauge-aiguille" id="jauge-aiguille" x1="110" y1="110" x2="110" y2="42"/>
            <circle class="jauge-axe" cx="110" cy="110" r="7"/>
            <text class="jauge-borne" x="22" y="138">Notions</text>
            <text class="jauge-borne" x="198" y="138">Avancé</text>
          </svg>
          <div class="jauge-texte"><span class="petit">Mon niveau</span><strong id="fiche-niveau"></strong></div>
        </div>""")
r("    document.querySelectorAll('#fiche-crans i').forEach((c, i) => c.classList.toggle('plein', i < n));\n    fiche.showModal();",
  """    const part = n / 3, valeur = document.getElementById('jauge-valeur'), aiguille = document.getElementById('jauge-aiguille');
    valeur.style.transition = aiguille.style.transition = 'none';
    valeur.style.strokeDashoffset = 277; aiguille.style.transform = 'rotate(-90deg)';
    fiche.showModal();
    requestAnimationFrame(() => requestAnimationFrame(() => {
      valeur.style.transition = aiguille.style.transition = '';
      valeur.style.strokeDashoffset = 277 * (1 - part); aiguille.style.transform = `rotate(${-90 + 180 * part}deg)`;
    }));""")


# Barre de navigation flottante, icônes bicolores
r('<a href="#apropos">À propos</a>', '<a href="#apropos"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="4.2" class="clair"/><path d="M4 20.5c0-4.2 3.6-7 8-7s8 2.8 8 7v.5H4z"/></svg><span>À propos</span></a>')
r('<a href="#projets">Projets</a>', '<a href="#projets"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5 3.5 7 12 11.5 20.5 7z" class="clair"/><path d="M3.5 8.3 11.3 12.5V21.5L3.5 17.2z"/><path d="M20.5 8.3 12.7 12.5V21.5L20.5 17.2z" class="moyen"/></svg><span>Projets</span></a>')
r('<a href="#parcours">Parcours</a>', '<a href="#parcours"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 2.5h1.8v19H5z"/><path d="M6.8 3.5h11.7l-2.6 4.2 2.6 4.3H6.8z" class="clair"/></svg><span>Parcours</span></a>')
r('<a href="#contact">Contact</a>', '<a href="#contact"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5.5A2.5 2.5 0 0 1 5.5 3h13A2.5 2.5 0 0 1 21 5.5v9a2.5 2.5 0 0 1-2.5 2.5H10l-4.5 4v-4h0A2.5 2.5 0 0 1 3 14.5z" class="clair"/><circle cx="8.5" cy="10" r="1.3"/><circle cx="12" cy="10" r="1.3"/><circle cx="15.5" cy="10" r="1.3"/></svg><span>Contact</span></a>')
css = """
  /* ===== Variante widgets : cartes sombres très arrondies, accent vert du design system, pastilles rondes, pilules ===== */
  :root {
    --page: #0b0b0c; --fond: #0b0b0c; --surface: #1c1c20; --surface-2: #2a2a30; --filet: #2a2a30;
    --texte: #f2f3f3; --texte-attenue: #a3a6ab; --texte-discret: #8b8f95;
    --accent: #1d5a4e; --accent-survol: #256b5e; --accent-texte: #7ccbb7; --accent-trait: #7ccbb7; --sur-accent: #e6f4f0;
    --carte: linear-gradient(160deg, #24242a 0%, #18181c 100%);
    --rayon-sm: 10px; --rayon-md: 16px; --rayon-lg: 22px; --rayon-xl: 28px;
  }
  @media (prefers-color-scheme: light) {
    :root:not([data-theme="dark"]) {
      --page: #ededef; --fond: #ededef; --surface: #ffffff; --surface-2: #f1f1f3; --filet: #e2e2e6;
      --texte: #141516; --texte-attenue: #5a5f63; --texte-discret: #6b7075;
      --accent: #1d5a4e; --accent-survol: #256b5e; --accent-texte: #256b5e; --accent-trait: #2e7d6c; --sur-accent: #ffffff;
      --carte: linear-gradient(160deg, #ffffff 0%, #f6f6f8 100%);
    }
  }
  :root[data-theme="light"] {
    --page: #ededef; --fond: #ededef; --surface: #ffffff; --surface-2: #f1f1f3; --filet: #e2e2e6;
    --texte: #141516; --texte-attenue: #5a5f63; --texte-discret: #6b7075;
    --accent: #1d5a4e; --accent-survol: #256b5e; --accent-texte: #256b5e; --accent-trait: #2e7d6c; --sur-accent: #ffffff;
    --carte: linear-gradient(160deg, #ffffff 0%, #f6f6f8 100%);
  }

  /* Écrans : tous sur le même fond, ce sont les cartes qui portent la matière */
  #apropos, #parcours, #contact { background: var(--page); }
  #contact {
    color: var(--texte);
    --page: inherit; --surface: inherit; --surface-2: inherit; --filet: inherit;
    --texte: inherit; --texte-attenue: inherit; --texte-discret: inherit; --accent-texte: inherit; --fond: inherit;
  }
  #contact .filigrane, .filigrane { color: var(--surface); }
  #contact .barre, .barre { color: var(--accent-texte); }
  #contact footer { border-top-color: var(--filet); }

  /* Boutons : pilules ; principal en aplat vert */
  .btn, #contact .btn.principal { border-radius: var(--rayon-pilule); }
  .btn.principal, #contact .btn.principal { background: var(--accent); color: var(--sur-accent); }
  .btn.principal:hover, #contact .btn.principal:hover { background: var(--accent-survol); }
  .btn.second { background: var(--surface-2); }
  .copier, #contact .copier { border: 0; background: var(--surface-2); color: var(--texte); border-radius: var(--rayon-pilule); }

  /* Cartes */
  .recit, .groupe, .projet, .parcours > div, .courriel, .reseau, dialog.fiche, dialog.fiche-projet {
    background: var(--carte); border-radius: var(--rayon-xl);
  }
  .recit { padding: 28px; max-width: none; align-self: start; }
  .outils { gap: 12px; }
  .groupe { padding: 22px; }
  .groupe h3, .colonne { font-size: 17px; font-weight: 600; color: var(--texte); border: 0; padding-bottom: 6px; margin-bottom: 8px; }

  /* Outils : une liste à pastilles rondes vertes, comme « Task labels » */
  .grille { grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 4px; }
  .outil, .outil:hover { background: transparent; }
  .outil { padding: 6px 8px; border-radius: var(--rayon-pilule); gap: 12px; }
  .outil:hover { background: var(--surface-2); }
  .outil svg.logo, .outil.trace svg.logo {
    width: 34px; height: 34px; padding: 8px; border-radius: 50%; background: var(--accent); fill: var(--sur-accent); flex: none;
  }
  .outil.trace svg.logo { stroke: var(--sur-accent); fill: none; }

  /* À propos en bento : le récit en grand à gauche, les groupes d'outils autour */
  .apropos { grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; align-items: stretch; }
  .outils { display: contents; }
  .recit { grid-column: 1 / 3; grid-row: 1 / 3; align-self: stretch; align-content: start; }
  .outils .groupe:nth-child(1) { grid-column: 3 / 5; grid-row: 1; }
  .outils .groupe:nth-child(2) { grid-column: 3 / 5; grid-row: 2; }
  .outils .groupe:nth-child(3) { grid-column: 1 / 4; grid-row: 3; }
  .outils .groupe:nth-child(4) { grid-column: 4 / 5; grid-row: 3; }
  .outils .groupe:nth-child(4) .grille { grid-template-columns: 1fr; }
  .outils .groupe:nth-child(3) .grille { grid-template-columns: repeat(auto-fill, minmax(128px, 1fr)); }
  @media (max-width: 900px) {
    .apropos { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .recit, .outils .groupe:nth-child(n) { grid-column: 1 / -1; grid-row: auto; }
  }

  /* Étiquettes en pilules */
  .pile span, #fp-pile span { border-radius: var(--rayon-pilule); background: var(--surface-2); padding: 7px 14px 7px 10px; }

  /* Projets : une carte par projet, bouton rond vert */
  .projets { gap: 12px; }
  .projet, .projet:first-child { padding: 26px 28px; border: 0; }
  .projet:hover { background: var(--carte); outline: 1px solid var(--surface-2); }
  .projet:hover h3 { color: var(--texte); }
  .fleche { border: 0; background: var(--accent); color: var(--sur-accent); width: 48px; height: 48px; font-size: 20px; }
  .projet:hover .fleche { background: var(--accent-survol); }

  /* Parcours : deux cartes, années en chiffres gras */
  .parcours > div { padding: 24px 28px; }
  .etape, .etape:first-child { border: 0; border-top: 1px solid var(--filet); }
  .colonne + .etape { border-top: 0; }
  .etape .annee { color: var(--texte); font-weight: 700; font-size: 17px; }
  .parcours .etape { grid-template-columns: 136px minmax(0, 1fr); }
  .etape.actuelle .annee { color: var(--sur-accent); background: var(--accent); border-radius: var(--rayon-pilule); padding: 2px 10px; justify-self: start; font-size: 14px; white-space: nowrap; }

  /* Contact : cartes, pastilles rondes vertes */
  .pastille, .courriel .pastille, .canal .pastille { border-radius: 50%; background: var(--accent); color: var(--sur-accent); }
  .pastille svg.logo { fill: var(--sur-accent); }
  .reseau .action, #contact .reseau .action { color: var(--accent-texte); text-decoration: none; }
  .reseau:hover, a.reseau:hover { background: var(--carte); outline: 1px solid var(--surface-2); }

  /* Fenêtres */
  .fiche-tete .pastille { border-radius: 50%; }
  .crans i.plein { background: var(--accent); }
  .schema .n.a { fill: var(--accent); stroke: var(--accent); }
  .schema .n.a + text { fill: var(--sur-accent); }
  .fp-schema { background: var(--page); border-radius: var(--rayon-lg); }

  /* Fenêtre d'un outil : pastille verte, jauge en demi-cercle */
  .fiche-tete .pastille { width: 48px; height: 48px; border-radius: 50%; background: var(--accent); color: var(--sur-accent); }
  .fiche-tete .pastille svg { width: 24px; height: 24px; fill: var(--sur-accent); }
  .fiche-tete .pastille.trace svg { fill: none; stroke: var(--sur-accent); }
  .niveau { border-top: 0; padding-top: 0; }
  .jauge { position: relative; display: grid; justify-items: center; padding-top: 4px; }
  .jauge svg { width: min(260px, 100%); height: auto; overflow: visible; }
  .jauge-fond, .jauge-valeur { fill: none; stroke-width: 26; stroke-linecap: butt; }
  .jauge-fond { stroke: var(--surface-2); }
  .jauge-valeur { stroke: var(--accent); stroke-dasharray: 277; stroke-dashoffset: 277; transition: stroke-dashoffset 900ms var(--courbe-sortie) 120ms; }
  .jauge-aiguille { stroke: var(--texte); stroke-width: 5; stroke-linecap: round; transform-origin: 110px 110px; transform: rotate(-90deg); transition: transform 900ms var(--courbe-sortie) 120ms; }
  .jauge-axe { fill: var(--texte); }
  .jauge-texte { display: grid; justify-items: center; gap: 0; margin-top: 6px; }
  .jauge-texte strong { font-size: 20px; font-weight: 700; }
  .jauge-borne { fill: var(--texte-attenue); font: 500 11px var(--police); text-anchor: middle; }

  /* Schémas : blocs aussi arrondis que le reste */
  .schema rect { rx: 14px; ry: 14px; }

  /* Barre de navigation : flottante, dégradé sombre, fine bordure claire, halo de lumière en dessous */
  nav { background: transparent; border: 0; padding: 12px 0 6px; position: relative; z-index: 12; }
  nav .wrap { position: relative; height: auto; }
  nav .wrap::before {
    content: ''; position: absolute; inset: 0 max(24px, env(safe-area-inset-right, 0px)) 0 max(24px, env(safe-area-inset-left, 0px));
    border-radius: 18px; z-index: -1;
    background: linear-gradient(180deg, #1d1d21 0%, #101012 100%);
    border: 1px solid rgba(255, 255, 255, .08); border-bottom-color: rgba(255, 255, 255, .03);
  }
  nav::after {
    content: ''; position: absolute; left: 50%; top: calc(100% - 6px); width: min(900px, 90%); height: 120px; translate: -50% 0;
    background: radial-gradient(50% 100% at 50% 0%, rgba(255, 255, 255, .07), transparent 70%); pointer-events: none; z-index: -1;
  }
  nav .wrap { padding-block: 8px; }
  nav .wrap > .marque { padding-left: 22px; }
  nav .wrap > .theme { margin-right: 14px; }
  .liens { gap: 6px; }
  .liens a { display: inline-flex; align-items: center; gap: 10px; padding: 10px 16px; border-radius: 12px; font-weight: 600; font-size: 15px; color: var(--texte-attenue); }
  .liens a:hover { background: rgba(255, 255, 255, .05); color: var(--texte); }
  .liens a.active { color: var(--texte); background: rgba(255, 255, 255, .06); }
  .ico { width: 22px; height: 22px; flex: none; }
  .ico path, .ico circle { fill: #8d9096; }
  .ico .moyen { fill: #b8bbbf; }
  .ico .clair { fill: #d9dbdd; }
  .liens a.active .ico .clair { fill: var(--accent-trait); }
  @media (prefers-color-scheme: light) {
    :root:not([data-theme="dark"]) nav .wrap::before { background: linear-gradient(180deg, #ffffff 0%, #f1f1f3 100%); border-color: rgba(0, 0, 0, .07); }
    :root:not([data-theme="dark"]) nav::after { background: radial-gradient(50% 100% at 50% 0%, rgba(0, 0, 0, .06), transparent 70%); }
    :root:not([data-theme="dark"]) .liens a:hover, :root:not([data-theme="dark"]) .liens a.active { background: rgba(0, 0, 0, .05); }
    :root:not([data-theme="dark"]) .ico path, :root:not([data-theme="dark"]) .ico circle { fill: #7d8187; }
    :root:not([data-theme="dark"]) .ico .clair { fill: #b5b8bc; }
  }
  :root[data-theme="light"] nav .wrap::before { background: linear-gradient(180deg, #ffffff 0%, #f1f1f3 100%); border-color: rgba(0, 0, 0, .07); }
  :root[data-theme="light"] nav::after { background: radial-gradient(50% 100% at 50% 0%, rgba(0, 0, 0, .06), transparent 70%); }
  :root[data-theme="light"] .liens a:hover, :root[data-theme="light"] .liens a.active { background: rgba(0, 0, 0, .05); }
  :root[data-theme="light"] .ico path, :root[data-theme="light"] .ico circle { fill: #7d8187; }
  :root[data-theme="light"] .ico .clair { fill: #b5b8bc; }
  .diapo { z-index: 0; }
  .diapo.active { z-index: 1; }

  /* Repères */
  .points button[aria-current="true"]::before { border-radius: var(--rayon-pilule); background: var(--accent-trait); }
"""
r('</style>', css + '</style>')
open(os.path.join(MAQ, 'widgets.html'),'w').write(s)
a=re.sub(r'<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport"[^>]*>\n','',s)
a=a.replace('<title>Azarias Sawadogo — widgets</title>','<title>Portfolio Azarias widgets</title>\n<meta name="claude:viewport-fit-sides" content="cover">')
a=a.replace('</style>\n</head>\n<body>','</style>').replace('</body>\n</html>\n','')
a=a.replace('  nav { position: sticky;','  body::before { content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 10; background: var(--page); }\n  nav { position: sticky;',1)
a=a.replace('../media/azarias.jpg','azarias.jpg').replace('../document/CV-Azarias-Sawadogo-2026.pdf','cv.pdf')
assert '<head>' not in a
open(os.path.join(APERCU, 'portfolio-widgets.html'),'w').write(a)
print('ok')
