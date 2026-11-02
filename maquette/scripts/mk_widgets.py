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

# Boutons : remplissage directionnel au survol (le fond entre par le côté du curseur et sort par le côté opposé)
r("  // Copier l'adresse e-mail", """  // Boutons : le fond se remplit depuis le côté par lequel entre le curseur, et repart par celui où il sort
  document.querySelectorAll('.btn, .copier').forEach(b => {
    const cote = e => { const r = b.getBoundingClientRect(); return e.clientX < r.left + r.width / 2 ? -1 : 1; };
    b.addEventListener('pointerenter', e => {
      if (e.pointerType === 'touch') return;
      b.classList.add('sans-transition'); b.style.setProperty('--bx', (cote(e) * 101) + '%');
      void b.offsetWidth;
      b.classList.remove('sans-transition'); b.style.setProperty('--bx', '0%'); b.classList.add('rempli');
    });
    b.addEventListener('pointerleave', e => {
      if (e.pointerType === 'touch') return;
      b.style.setProperty('--bx', (cote(e) * 101) + '%'); b.classList.remove('rempli');
    });
  });

  // Copier l'adresse e-mail""")


# Contact : grande carte d'appel à l'action, puis un vrai pied de page (colonnes de liens, copyright, réseaux)
_m = re.search(r'<section id="contact" class="diapo contact">.*?</section>', s, flags=re.S)
_ancien = _m.group(0)
def _logo(dom):
    return re.search(r'href="[^"]*' + dom + r'[^"]*"[^>]*>\s*<span class="pastille">(<svg.*?</svg>)</span>', _ancien, flags=re.S).group(1)
_li, _gh, _wa = _logo('linkedin'), _logo('github.com'), _logo('wa.me')
_cv = re.search(r'<a href="([^"]*CV[^"]*)"', s).group(1)
_nav_liens = '\n        '.join(re.findall(r'<a href="#(?:apropos|projets|parcours)">.*?</a>', re.search(r'<div class="liens">.*?</div>', s, flags=re.S).group(0), flags=re.S))
_nouveau = f"""<section id="contact" class="diapo contact">
  <div class="wrap">
    <span class="filigrane filigrane-contact" aria-hidden="true">Contact</span>
    <div class="cta">
      <div class="tete"><h2><span class="barre" aria-hidden="true">/</span>Envie de collaborer ou d’échanger ?</h2></div>
      <div class="cta-courriel">
        <span class="adresse" id="adresse">azasawpro@gmail.com</span>
        <div class="icones-actions">
          <button class="icone-action" id="copier" type="button" aria-label="Copier l’adresse" title="Copier l’adresse">
            <svg class="i-copier" viewBox="0 0 24 24" aria-hidden="true"><rect x="8.5" y="8.5" width="12" height="12" rx="3"/><path d="M15.5 8.5V6a2.5 2.5 0 0 0-2.5-2.5H6A2.5 2.5 0 0 0 3.5 6v7A2.5 2.5 0 0 0 6 15.5h2.5"/></svg>
            <svg class="i-ok" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>
          </button>
          <a class="icone-action" href="mailto:azasawpro@gmail.com" aria-label="Écrire un e-mail" title="Écrire un e-mail">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg>
          </a>
        </div>
      </div>
    </div>
    <footer class="pied">
      <div class="pied-marque">
        <span class="marque">Azarias Sawadogo</span>
        <p class="petit">Développeur systèmes et bases de données · Data engineer junior</p>
      </div>
      <nav class="pied-col" aria-label="Plan du site">
        <h3>Navigation</h3>
        {_nav_liens}
      </nav>
      <div class="pied-col">
        <h3>Réseaux</h3>
        <a href="https://www.linkedin.com/in/azarias-sawadogo-90345a2a2/" target="_blank" rel="noopener">{_li}LinkedIn</a>
        <a href="https://github.com/Azarias646" target="_blank" rel="noopener">{_gh}GitHub</a>
        <a href="https://wa.me/22655194949" target="_blank" rel="noopener">{_wa}WhatsApp</a>
      </div>
      <div class="pied-col">
        <h3>Documents</h3>
        <a href="{_cv}" target="_blank" rel="noopener"><svg class="trait" viewBox="0 0 24 24" aria-hidden="true"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/></svg>Mon CV</a>
      </div>
      <div class="pied-bas">
        <span class="petit">© 2026 Azarias Sawadogo</span>
        <div class="sociaux">
          <a href="https://www.linkedin.com/in/azarias-sawadogo-90345a2a2/" target="_blank" rel="noopener" aria-label="LinkedIn">{_li}</a>
          <a href="https://github.com/Azarias646" target="_blank" rel="noopener" aria-label="GitHub">{_gh}</a>
          <a href="https://wa.me/22655194949" target="_blank" rel="noopener" aria-label="WhatsApp">{_wa}</a>
        </div>
      </div>
    </footer>
  </div>
</section>"""
s = s.replace(_ancien, _nouveau)
r("document.querySelectorAll('.projets, .parcours > div, .outils, .canaux, .recit')", "document.querySelectorAll('.projets, .parcours > div, .outils, .canaux, .recit, .pied, .etapes-grille')")


r("    const ok = () => { copier.textContent = 'Copiée'; setTimeout(() => copier.textContent = 'Copier', 1800); };",
  "    const ok = () => { copier.classList.add('copie'); copier.setAttribute('aria-label', 'Adresse copiée'); copier.title = 'Adresse copiée'; setTimeout(() => { copier.classList.remove('copie'); copier.setAttribute('aria-label', 'Copier l’adresse'); copier.title = 'Copier l’adresse'; }, 1800); };")


# Parcours : un panneau à onglets (Expérience / Cursus et certifications) et une grille de cartes à vignette
def _vignette(corps):
    return '<svg viewBox="0 0 160 84" aria-hidden="true">' + corps + '</svg>'
_v = {
 'poste': _vignette('<rect class="v2" x="14" y="12" width="56" height="6" rx="3"/><rect class="v3" x="14" y="22" width="36" height="4" rx="2"/><rect class="v1" x="14" y="34" width="40" height="38" rx="6"/><rect class="v1" x="60" y="34" width="40" height="38" rx="6"/><rect class="va" x="106" y="34" width="40" height="38" rx="6"/>'),
 'data': _vignette('<rect class="v2" x="14" y="12" width="48" height="6" rx="3"/><rect class="v1" x="14" y="58" width="16" height="14" rx="3"/><rect class="v1" x="36" y="46" width="16" height="26" rx="3"/><rect class="v1" x="58" y="38" width="16" height="34" rx="3"/><rect class="va" x="80" y="26" width="16" height="46" rx="3"/><path class="vl" d="M104 60 C116 56 120 36 146 30"/><circle class="vp" cx="146" cy="30" r="3.5"/>'),
 'mobile': _vignette('<rect class="v1" x="58" y="8" width="44" height="70" rx="9"/><rect class="v2" x="66" y="18" width="28" height="5" rx="2.5"/><rect class="va" x="66" y="28" width="28" height="18" rx="4"/><rect class="v3" x="66" y="52" width="20" height="4" rx="2"/><rect class="v3" x="66" y="60" width="26" height="4" rx="2"/><rect class="v2" x="24" y="24" width="24" height="5" rx="2.5"/><rect class="v3" x="24" y="34" width="18" height="4" rx="2"/><rect class="v2" x="112" y="24" width="24" height="5" rx="2.5"/><rect class="v3" x="112" y="34" width="18" height="4" rx="2"/>'),
 'ia': _vignette('<path class="vl" d="M40 22 L80 42 L120 22 M40 62 L80 42 L120 62 M40 22 L40 62 M120 22 L120 62"/><circle class="v1c" cx="40" cy="22" r="8"/><circle class="v1c" cx="40" cy="62" r="8"/><circle class="v1c" cx="120" cy="22" r="8"/><circle class="v1c" cx="120" cy="62" r="8"/><circle class="vp" cx="80" cy="42" r="11"/>'),
 'mainframe': _vignette('<rect class="v1" x="48" y="8" width="64" height="70" rx="6"/><rect class="v2" x="56" y="16" width="48" height="9" rx="2"/><rect class="v2" x="56" y="30" width="48" height="9" rx="2"/><rect class="v2" x="56" y="44" width="48" height="9" rx="2"/><circle class="vp" cx="98" cy="20.5" r="2.4"/><circle class="vp" cx="98" cy="34.5" r="2.4"/><circle class="v3c" cx="98" cy="48.5" r="2.4"/><rect class="v3" x="56" y="62" width="30" height="5" rx="2.5"/>'),
 'pipeline': _vignette('<ellipse class="v1" cx="30" cy="26" rx="14" ry="5"/><rect class="v1" x="16" y="26" width="28" height="30"/><ellipse class="v2" cx="30" cy="56" rx="14" ry="5"/><path class="vl" d="M50 41 H74"/><rect class="va" x="76" y="28" width="30" height="26" rx="6"/><path class="vl" d="M110 41 H128"/><rect class="v1" x="130" y="22" width="20" height="10" rx="3"/><rect class="v1" x="130" y="36" width="20" height="10" rx="3"/><rect class="v1" x="130" y="50" width="20" height="10" rx="3"/><circle class="vp" cx="74" cy="41" r="2.6"/>'),
 'diplome': _vignette('<rect class="v1" x="32" y="14" width="96" height="58" rx="6"/><rect class="v2" x="44" y="24" width="52" height="6" rx="3"/><rect class="v3" x="44" y="36" width="72" height="4" rx="2"/><rect class="v3" x="44" y="44" width="60" height="4" rx="2"/><circle class="vp" cx="108" cy="58" r="8"/><path class="va" d="M102 64 l-3 12 6-4 3 6 3-12z"/>'),
}
def _carte(vig, titre, sous, annee, actuel=False):
    badge = '<span class="badge">En cours</span>' if actuel else ''
    cls = 'etape-carte actuelle' if actuel else 'etape-carte'
    return f"""<article class="{cls}"><div class="vignette">{_v[vig]}</div><div class="etape-texte"><h4>{titre}{badge}</h4>{('<p class="petit">' + sous + '</p>') if sous else ''}<p class="petit annee-carte">{annee}</p></div></article>"""
_ico_exp = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 4.5h6a1.5 1.5 0 0 1 1.5 1.5v1.5h-9V6A1.5 1.5 0 0 1 9 4.5z"/><rect x="3" y="7.5" width="18" height="12.5" rx="2.5" class="clair"/><rect x="3" y="11.5" width="18" height="2"/></svg>'
_ico_cur = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4 1.5 9 12 14l10.5-5z" class="clair"/><path d="M6 11.5V16c0 1.7 2.7 3 6 3s6-1.3 6-3v-4.5L12 14.4z"/><path d="M21 9.6h1.4v5.4H21z"/></svg>'
_nouveau_p = f"""<div class="parcours-panneau">
      <div class="onglets" role="tablist" aria-label="Parcours">
        <button class="onglet" type="button" role="tab" id="onglet-exp" aria-controls="panneau-exp" aria-selected="true">{_ico_exp}<span>Expérience</span></button>
        <button class="onglet" type="button" role="tab" id="onglet-cur" aria-controls="panneau-cur" aria-selected="false" tabindex="-1">{_ico_cur}<span>Cursus et certifications</span></button>
      </div>
      <div class="onglets-zone">
      <div class="onglet-panneau" role="tabpanel" id="panneau-exp" aria-labelledby="onglet-exp">
        <h3 class="sous-titre">Expérience</h3>
        <div class="etapes-grille">
          {_carte('poste', 'Développeur systèmes et bases de données', 'Aïobi', '2026')}
          {_carte('data', 'Stagiaire Data / IA', 'Aïobi', '2025 — 2026')}
          {_carte('mobile', 'Stagiaire développeur mobile', 'Foulisa', '2025')}
        </div>
      </div>
      <div class="onglet-panneau" role="tabpanel" id="panneau-cur" aria-labelledby="onglet-cur" hidden>
        <h3 class="sous-titre">Cursus et certifications</h3>
        <div class="etapes-grille quatre">
          {_carte('ia', 'Master Intelligence Artificielle', '', '2026')}
          {_carte('pipeline', 'Certificat professionnel IBM Data Engineering', 'IBM · Coursera', '2026')}
          {_carte('mainframe', 'IBM Z Xplore — Fundamentals', 'Les bases des mainframes IBM Z', '2026')}
          {_carte('diplome', 'Licence Informatique de Gestion', 'Université de l’Unité Africaine (ex IAM)', '2022 — 2025')}
        </div>
      </div>
      </div>
    </div>"""
_pa = re.search(r'<div class="parcours">.*?\n    </div>\n  </div>\n</section>', s, flags=re.S)
assert _pa
s = s.replace(_pa.group(0), _nouveau_p + "\n  </div>\n</section>")
r("  // Copier l'adresse e-mail", """  // Parcours : onglets (clic, flèches gauche/droite) ; les cartes du panneau choisi réapparaissent en cascade
  const onglets = [...document.querySelectorAll('.onglet')];
  const choisir = o => {
    onglets.forEach(x => {
      const actif = x === o, panneau = document.getElementById(x.getAttribute('aria-controls'));
      x.setAttribute('aria-selected', actif); x.tabIndex = actif ? 0 : -1; panneau.hidden = !actif;
      if (actif && !reduit) {
        panneau.classList.add('rejoue'); void panneau.offsetWidth; panneau.classList.remove('rejoue');
      }
    });
  };
  onglets.forEach((o, i) => {
    o.addEventListener('click', () => choisir(o));
    o.addEventListener('keydown', e => {
      if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
      e.preventDefault(); const n = onglets[(i + (e.key === 'ArrowRight' ? 1 : onglets.length - 1)) % onglets.length]; n.focus(); choisir(n);
    });
  });

  // Copier l'adresse e-mail""")

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
  .outils .groupe:nth-child(3) { grid-column: 1 / 3; grid-row: 3; }
  .outils .groupe:nth-child(4) { grid-column: 3 / 5; grid-row: 3; }
  .outils .groupe:nth-child(3) .grille { grid-template-columns: repeat(auto-fill, minmax(118px, 1fr)); }
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

  /* Boutons : remplissage directionnel au survol */
  .btn, .copier, #contact .copier { position: relative; overflow: hidden; isolation: isolate; transition: color 320ms var(--courbe-sortie), transform var(--duree-rapide); }
  .btn::before, .copier::before {
    content: ''; position: absolute; inset: 0; z-index: -1; border-radius: inherit; background: var(--balayage);
    transform: translateX(var(--bx, -101%)); transition: transform 460ms cubic-bezier(.65, 0, .35, 1);
  }
  .btn.sans-transition::before, .copier.sans-transition::before { transition: none; }
  .btn.second, .copier, #contact .copier { background: transparent; border: 1px solid var(--texte-discret); color: var(--texte); --balayage: var(--texte); }
  .btn.second:hover, .copier:hover, #contact .copier:hover { background: transparent; }
  .btn.principal, #contact .btn.principal { --balayage: var(--accent-texte); }
  .btn.principal:hover, #contact .btn.principal:hover { background: var(--accent); }
  .btn.rempli, .copier.rempli { color: var(--page); transition: color 160ms linear 200ms, transform var(--duree-rapide); }

  /* Contact : carte d'appel à l'action + pied de page */
  .contact .wrap { display: grid; gap: 56px; }
  .cta {
    display: grid; grid-template-columns: minmax(0, 1.15fr) minmax(0, 1fr); gap: 40px; align-items: end;
    padding: 52px 48px; border-radius: var(--rayon-xl);
    background: var(--barre-fond);
    border: 1px solid var(--barre-bord);
    position: relative; overflow: hidden; isolation: isolate;
  }
  /* Halo vert qui dérive lentement et en permanence dans la carte */
  .cta::before {
    content: ''; position: absolute; z-index: -1; pointer-events: none;
    width: 78%; aspect-ratio: 1; top: -60%; right: -20%; border-radius: 50%;
    background: radial-gradient(closest-side, var(--cta-halo), transparent);
    animation: halo-derive 16s ease-in-out infinite;
  }
  @keyframes halo-derive {
    0%, 100% { transform: translate(0, 0) scale(1); }
    25% { transform: translate(-28%, 22%) scale(1.12); }
    50% { transform: translate(-62%, 8%) scale(.94); }
    75% { transform: translate(-30%, 34%) scale(1.06); }
  }
  /* Fond et bordure partagés par la barre de navigation, la carte d'appel et le pied de page */
  :root { --cta-halo: rgba(37, 120, 102, .75); --barre-fond: linear-gradient(180deg, #1d1d21 0%, #101012 100%); --barre-bord: rgba(255, 255, 255, .08); }
  :root[data-theme="light"] { --cta-halo: rgba(37, 120, 102, .45); --barre-fond: linear-gradient(180deg, #ffffff 0%, #f1f1f3 100%); --barre-bord: rgba(0, 0, 0, .07); }
  @media (prefers-color-scheme: light) { :root:not([data-theme="dark"]) { --cta-halo: rgba(37, 120, 102, .45); --barre-fond: linear-gradient(180deg, #ffffff 0%, #f1f1f3 100%); --barre-bord: rgba(0, 0, 0, .07); } }
  .contact .cta .tete { text-align: left; margin: 0; }
  .cta h2 { font-size: clamp(30px, 4vw, 48px); }
  .cta-courriel { display: flex; flex-wrap: wrap; align-items: center; gap: 6px 14px; min-width: 0; justify-content: flex-end; }
  .icones-actions { display: flex; gap: 4px; }
  .icone-action {
    width: 40px; height: 40px; display: grid; place-items: center; border: 0; border-radius: 50%;
    background: transparent; color: var(--texte-discret); cursor: pointer;
    transition: background var(--duree-rapide), color var(--duree-rapide), transform var(--duree-rapide);
  }
  .icone-action:hover { background: var(--surface-2); color: var(--texte); }
  .icone-action:active { transform: scale(.94); }
  .icone-action svg { width: 19px; height: 19px; fill: none; stroke: currentColor; stroke-width: 1.8; stroke-linecap: round; stroke-linejoin: round; grid-area: 1 / 1; transition: opacity var(--duree-standard), transform var(--duree-standard) var(--courbe-sortie); }
  .icone-action .i-ok { opacity: 0; transform: scale(.6); color: var(--accent-trait); }
  .icone-action.copie .i-copier { opacity: 0; transform: scale(.6); }
  .icone-action.copie .i-ok { opacity: 1; transform: none; }
  .contact footer.pied, #contact footer.pied { margin: 0; padding: 36px 40px 22px; border: 1px solid var(--barre-bord); border-radius: var(--rayon-xl); background: var(--barre-fond); display: grid; grid-template-columns: minmax(0, 1.6fr) repeat(3, minmax(0, 1fr)); gap: 32px 24px; }
  .pied-marque .marque { font-size: 18px; }
  .pied-marque p { margin-top: 8px; max-width: 32ch; }
  .pied-col { display: grid; gap: 10px; align-content: start; }
  .pied-col h3 { font-size: 13px; font-weight: 600; color: var(--texte); margin-bottom: 4px; }
  .pied-col a { display: inline-flex; align-items: center; gap: 10px; color: var(--texte-attenue); font-size: 14px; font-weight: 600; width: fit-content; transition: color var(--duree-rapide); }
  .pied-col .ico, .pied-col svg.logo, .pied-col svg.trait { width: 20px; height: 20px; flex: none; }
  .pied-col svg.logo { fill: #8d9096; padding: 1px; }
  .pied-col svg.trait { fill: none; stroke: #8d9096; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
  .pied-col a:hover svg.logo { fill: var(--accent-trait); }
  .pied-col a:hover svg.trait { stroke: var(--accent-trait); }
  .pied-col a:hover .ico .clair { fill: var(--accent-trait); }
  footer.pied nav { padding: 0; position: static; background: none; }
  footer.pied nav::after { content: none; }
  .pied-col a:hover { color: var(--texte); }
  .pied-bas { grid-column: 1 / -1; margin-top: 8px; display: flex; flex-wrap: wrap; gap: 16px; justify-content: space-between; align-items: center; padding-top: 20px; border-top: 1px solid var(--filet); }
  .sociaux { display: flex; gap: 4px; }
  .sociaux a { width: 40px; height: 40px; display: grid; place-items: center; border-radius: 50%; color: var(--texte-attenue); transition: background var(--duree-rapide), color var(--duree-rapide); }
  .sociaux a:hover { background: var(--surface-2); color: var(--texte); }
  .sociaux svg.logo { width: 18px; height: 18px; }
  @media (max-width: 760px) {
    .cta { grid-template-columns: 1fr; padding: 32px 24px; }
    .contact footer.pied, #contact footer.pied { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .pied-marque { grid-column: 1 / -1; }
  }

  /* Parcours : panneau à onglets, cartes à vignette */
  .parcours-panneau {
    padding: 22px; border-radius: var(--rayon-xl); background: var(--barre-fond); border: 1px solid var(--barre-bord);
    display: grid; gap: 22px; max-width: 980px;
  }
  .onglets { display: grid; grid-template-columns: 1fr 1fr; gap: 4px; padding: 5px; border-radius: 16px; background: var(--surface-2); }
  :root:not([data-theme="light"]) .onglets { background: rgba(255, 255, 255, .04); }
  .onglet {
    display: inline-flex; align-items: center; justify-content: center; gap: 10px; height: 46px; border: 0; border-radius: 12px;
    background: transparent; color: var(--texte-attenue); font: inherit; font-weight: 600; font-size: 15px; cursor: pointer;
    transition: background var(--duree-standard), color var(--duree-standard);
  }
  .onglet:hover { color: var(--texte); }
  .onglet[aria-selected="true"] { background: var(--carte); color: var(--texte); }
  .onglet[aria-selected="true"] .ico .clair { fill: var(--accent-trait); }
  .sous-titre { font-size: 16px; font-weight: 600; color: var(--texte); margin: 0 4px 12px; }
  .etapes-grille { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; }
  .etape-carte {
    display: grid; gap: 18px; align-content: start; padding: 14px 14px 20px; border-radius: 20px; background: var(--carte);
    border: 1px solid transparent; transition: border-color var(--duree-standard), transform var(--duree-rapide);
  }
  .vignette { display: grid; place-items: center; height: 104px; border-radius: 14px; background: var(--page); border: 1px solid var(--filet); }
  .vignette svg { width: 150px; max-width: 86%; height: auto; }
  .vignette .v1 { fill: var(--surface-2); }
  .vignette .v1c { fill: var(--surface-2); stroke: var(--filet); }
  .vignette .v2 { fill: color-mix(in srgb, var(--texte-discret) 55%, transparent); }
  .vignette .v3, .vignette .v3c { fill: color-mix(in srgb, var(--texte-discret) 30%, transparent); }
  .vignette .va { fill: var(--accent); }
  .vignette .vp { fill: var(--accent-trait); }
  .vignette .vl { fill: none; stroke: var(--texte-discret); stroke-width: 1.6; stroke-linecap: round; }
  .etape-texte { display: grid; gap: 4px; padding: 0 6px; }
  .etape-texte h4 { font-size: 16px; font-weight: 600; line-height: 1.3; display: flex; flex-wrap: wrap; align-items: center; gap: 8px; }
  .annee-carte { font-variation-settings: 'wdth' 88; font-variant-numeric: tabular-nums; color: var(--texte-discret); }
  .onglets-zone { display: grid; }
  .onglet-panneau { grid-area: 1 / 1; }
  .onglet-panneau[hidden] { display: block !important; visibility: hidden; }
  :root[data-theme="light"] .vignette .v1, :root[data-theme="light"] .vignette .v1c { fill: #dcdde1; }
  @media (prefers-color-scheme: light) { :root:not([data-theme="dark"]) .vignette .v1, :root:not([data-theme="dark"]) .vignette .v1c { fill: #dcdde1; } }
  .onglet-panneau.rejoue .etape-carte { animation: carte-entre 700ms var(--courbe-sortie) backwards; }
  .onglet-panneau.rejoue .etape-carte:nth-child(2) { animation-delay: 80ms; }
  .onglet-panneau.rejoue .etape-carte:nth-child(3) { animation-delay: 160ms; }
  .onglet-panneau.rejoue .etape-carte:nth-child(4) { animation-delay: 240ms; }
  @keyframes carte-entre { from { opacity: 0; transform: translateY(12px); } }
  .etapes-grille.quatre { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  @media (max-width: 900px) { .etapes-grille, .etapes-grille.quatre { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
  @media (max-width: 560px) { .etapes-grille, .etapes-grille.quatre { grid-template-columns: 1fr; } .onglet span { font-size: 13px; } }

  /* Largeur : contenu jusqu’à 1 520 px, marges latérales qui suivent l'écran (20 à 56 px) */
  :root { --goutte: clamp(20px, 4vw, 56px); }
  .wrap { max-width: 1520px; padding-left: max(var(--goutte), env(safe-area-inset-left, 0px)); padding-right: max(var(--goutte), env(safe-area-inset-right, 0px)); }
  nav .wrap::before { inset: 0 max(var(--goutte), env(safe-area-inset-right, 0px)) 0 max(var(--goutte), env(safe-area-inset-left, 0px)); }
  .parcours-panneau { max-width: none; }
  @media (max-width: 760px) { :root { --goutte: 16px; } }

  /* Repères : points ronds gris, l'actif grossit et prend le vert du site ;
     aucun nom affiché, sauf au survol (ou au focus clavier) : bulle à pointe */
  .points { gap: 6px; }
  .points button { position: relative; width: 30px; height: 30px; }
  .points button::before {
    width: 8px; height: 8px; border-radius: 50%; background: var(--texte-discret); opacity: .8;
    transition: width var(--duree-standard) var(--courbe-sortie), height var(--duree-standard) var(--courbe-sortie), background var(--duree-standard), opacity var(--duree-standard);
  }
  .points button:hover::before, .points button:focus-visible::before { opacity: 1; width: 10px; height: 10px; }
  .points button[aria-current="true"]::before { width: 11px; height: 11px; border-radius: 50%; background: var(--accent); opacity: .9; box-shadow: 0 0 0 4px color-mix(in srgb, var(--accent-trait) 13%, transparent); }
  /* Infobulle : juste le nom, en texte seul vert, dans la police de terminal de « whoami » */
  .points .etiquette {
    position: absolute; right: calc(100% + 6px); top: 50%; translate: 6px -50%; white-space: nowrap; pointer-events: none;
    font: 500 13px/1 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace; letter-spacing: .02em; color: var(--accent-trait);
    opacity: 0; visibility: hidden;
    transition: opacity var(--duree-standard), translate var(--duree-standard) var(--courbe-sortie), visibility 0s var(--duree-standard);
  }
  .points button:is(:hover, :focus-visible) .etiquette {
    opacity: 1; visibility: visible; translate: 0 -50%;
    transition: opacity var(--duree-standard), translate var(--duree-standard) var(--courbe-sortie), visibility 0s;
  }
  @media (max-width: 760px) { .points .etiquette { display: none; } }

  /* Filigranes : « Contact » dépasse derrière le haut de la carte ; « Réalisations », plus long, est réduit pour ne pas être coupé */
  .contact .wrap { position: relative; }
  .contact .cta { z-index: 1; }
  /* « Contact » : dans le flux, entièrement visible au-dessus de la carte ; la marge négative annule l'écart de la grille et le vide sous les lettres */
  .filigrane.filigrane-contact { position: relative; display: block; left: -.04em; right: auto; top: auto; text-align: left; transform: none; margin: 0 0 calc(-.24em - 44px); }
  #contact.diapo:not(#accueil) { padding-top: 56px; }
  /* Mêmes filigranes partout : même couleur, même taille (plafonnée pour que le mot le plus long, « Réalisations », tienne en largeur) */
  :root { --filigrane: #1a1a1e; }
  :root[data-theme="light"] { --filigrane: #f5f5f7; }
  @media (prefers-color-scheme: light) { :root:not([data-theme="dark"]) { --filigrane: #f5f5f7; } }
  .filigrane, #contact .filigrane, #apropos .filigrane, #parcours .filigrane { color: var(--filigrane); font-size: min(clamp(60px, 11vw, 150px), calc((100vw - 40px) / 5.8)); }
  /* Assez de place en haut de chaque écran pour que le filigrane ne soit jamais coupé, même quand le contenu dépasse la hauteur */
  .diapo:not(#accueil) { padding-top: 104px; }

  /* Un peu de folie : le nom s'affiche sur l'écran d'un ordinateur, en réponse à « whoami » */
  :root { --trait-pc: rgba(255, 255, 255, .13); --filet-pc: rgba(255, 255, 255, .08); --bord-pc: rgba(255, 255, 255, .03); --balayage-pc: rgba(255, 255, 255, .025); --points-pc: rgba(255, 255, 255, .14); --touche-cote: rgba(255, 255, 255, .03); --touche-dessus: rgba(255, 255, 255, .07); }
  :root[data-theme="light"] { --trait-pc: rgba(0, 0, 0, .22); --filet-pc: rgba(0, 0, 0, .15); --bord-pc: rgba(0, 0, 0, .035); --balayage-pc: rgba(0, 0, 0, .045); --points-pc: rgba(0, 0, 0, .2); --touche-cote: rgba(0, 0, 0, .09); --touche-dessus: rgba(255, 255, 255, .9); }
  @media (prefers-color-scheme: light) { :root:not([data-theme="dark"]) { --trait-pc: rgba(0, 0, 0, .22); --filet-pc: rgba(0, 0, 0, .15); --bord-pc: rgba(0, 0, 0, .035); --balayage-pc: rgba(0, 0, 0, .045); --points-pc: rgba(0, 0, 0, .2); --touche-cote: rgba(0, 0, 0, .09); --touche-dessus: rgba(255, 255, 255, .9); } }
  .ecran-nom {
    position: relative; display: inline-block; max-width: 100%;
    margin: 22px 0 124px; padding: 18px clamp(18px, 2.4vw, 30px) clamp(16px, 2vw, 26px);
    border-radius: 24px; border: 1.5px solid var(--trait-pc);
    background:
      repeating-linear-gradient(180deg, var(--balayage-pc) 0 1px, transparent 1px 4px),
      radial-gradient(120% 90% at 30% 20%, color-mix(in srgb, var(--accent-trait) 9%, transparent), transparent 70%);
    box-shadow: inset 0 0 0 9px var(--bord-pc), inset 0 0 0 10px var(--filet-pc);
    transition: opacity 1200ms var(--courbe-sortie) 100ms, border-color 1200ms var(--courbe-sortie);
  }
  .ecran-nom h1 { margin: 6px 0 0; }
  .invite-nom {
    font: 500 clamp(12px, 1.1vw, 14px)/1 ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
    color: var(--texte-discret); letter-spacing: .02em; padding-left: 2px;
  }
  .invite-nom span { color: var(--accent-trait); }
  .curseur-nom {
    display: inline-block; width: .09em; height: .74em; margin-left: .06em; vertical-align: -.02em;
    border-radius: 2px; background: var(--accent-trait); animation: curseur-nom 1.05s steps(1) infinite;
  }
  .bureau {
    position: absolute; left: 50%; top: 100%; width: min(440px, 92%); translate: -50% 0; overflow: visible;
    fill: none; stroke: var(--trait-pc); stroke-width: 1.5; stroke-linecap: round; stroke-linejoin: round;
  }
  .anime section.attente .ecran-nom { border-color: transparent; }
  .anime section.attente .invite-nom, .anime section.attente .bureau, .anime section.attente .tour { opacity: 0; }
  .invite-nom, .bureau, .tour { transition: opacity 900ms var(--courbe-sortie) 500ms; }
  @keyframes curseur-nom { 50% { opacity: 0; } }
  .bureau .boitier { fill: var(--bord-pc); }
  .bureau .touche { stroke: none; }
  .bureau .touche .cote { fill: var(--touche-cote); stroke: var(--filet-pc); stroke-width: .8; }
  .bureau .touche .dessus { fill: var(--touche-dessus); }
  .bureau .touche.esc .dessus { fill: color-mix(in srgb, var(--accent-trait) 30%, var(--touche-dessus)); }
  .bureau .led { stroke: none; fill: var(--filet-pc); }
  .bureau .led.allumee { fill: var(--accent-trait); opacity: .8; }
  .bureau .molette { stroke: none; fill: var(--accent-trait); opacity: .55; }
  .bureau .cable { stroke: var(--filet-pc); stroke-width: 1.2; }
  /* Tour : à droite de l'écran, posée au niveau du clavier */
  .tour {
    position: absolute; left: calc(100% + 20px); top: 26px; bottom: -86px; width: 66px;
    border-radius: 12px; border: 1.5px solid var(--trait-pc);
    display: flex; flex-direction: column; align-items: center; gap: 8px; padding: 16px 10px;
  }
  .tour .baie { width: 100%; height: 8px; border-radius: 3px; border: 1.5px solid var(--filet-pc); }
  .tour .grille-air { margin-top: auto; width: 70%; height: 38%; background: radial-gradient(circle, var(--points-pc) 1.2px, transparent 1.6px) 0 0 / 7px 7px; }
  @media (max-width: 1320px) { .tour { display: none; } }
  @media (max-width: 760px) { .ecran-nom { margin-bottom: 88px; } }
  @media (prefers-reduced-motion: reduce) { .curseur-nom { animation: none; } }
"""
r("b.onclick = () => aller(i); li.append(b); points.append(li);",
  "const etiquette = document.createElement('span'); etiquette.className = 'etiquette'; etiquette.setAttribute('aria-hidden', 'true'); etiquette.textContent = nomsEcrans[d.id];\n    b.removeAttribute('title'); b.append(etiquette);\n    b.onclick = () => aller(i); li.append(b); points.append(li);")
r('<h1><span class="ligne-nom">Azarias</span><span class="ligne-nom">Sawadogo</span></h1>', '<div class="ecran-nom"><p class="invite-nom" aria-hidden="true"><span>~</span> $ whoami</p>\n    <h1><span class="ligne-nom">Azarias</span><span class="ligne-nom">Sawadogo<i class="curseur-nom" aria-hidden="true"></i></span></h1>\n    <svg class="bureau" viewBox="0 0 440 98" aria-hidden="true" focusable="false"><path d="M202 0 L196 24 H244 L238 0"/><path d="M172 27 H268"/><rect class="boitier" x="30" y="36" width="326" height="58" rx="5"/><g class="touche esc"><rect class="cote" x="34.0" y="40.0" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="35.0" y="40.6" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="68.3" y="40.0" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="69.3" y="40.6" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="85.5" y="40.0" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="86.5" y="40.6" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="102.7" y="40.0" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="103.7" y="40.6" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="119.8" y="40.0" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="120.8" y="40.6" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="145.6" y="40.0" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="146.6" y="40.6" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="162.7" y="40.0" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="163.7" y="40.6" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="179.9" y="40.0" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="180.9" y="40.6" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="197.1" y="40.0" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="198.1" y="40.6" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="222.8" y="40.0" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="223.8" y="40.6" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="240.0" y="40.0" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="241.0" y="40.6" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="257.2" y="40.0" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="258.2" y="40.6" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="274.3" y="40.0" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="275.3" y="40.6" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="301.8" y="40.0" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="302.8" y="40.6" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="319.0" y="40.0" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="320.0" y="40.6" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="336.1" y="40.0" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="337.1" y="40.6" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="34.0" y="50.4" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="35.0" y="51.0" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="51.2" y="50.4" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="52.2" y="51.0" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="68.3" y="50.4" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="69.3" y="51.0" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="85.5" y="50.4" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="86.5" y="51.0" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="102.7" y="50.4" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="103.7" y="51.0" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="119.8" y="50.4" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="120.8" y="51.0" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="137.0" y="50.4" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="138.0" y="51.0" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="154.2" y="50.4" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="155.2" y="51.0" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="171.3" y="50.4" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="172.3" y="51.0" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="188.5" y="50.4" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="189.5" y="51.0" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="205.7" y="50.4" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="206.7" y="51.0" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="222.8" y="50.4" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="223.8" y="51.0" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="240.0" y="50.4" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="241.0" y="51.0" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="257.2" y="50.4" width="33.0" height="6.9" rx="1.4"/><rect class="dessus" x="258.2" y="51.0" width="31.0" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="301.8" y="50.4" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="302.8" y="51.0" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="319.0" y="50.4" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="320.0" y="51.0" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="336.1" y="50.4" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="337.1" y="51.0" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="34.0" y="58.6" width="24.4" height="6.9" rx="1.4"/><rect class="dessus" x="35.0" y="59.2" width="22.4" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="59.8" y="58.6" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="60.8" y="59.2" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="76.9" y="58.6" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="77.9" y="59.2" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="94.1" y="58.6" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="95.1" y="59.2" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="111.2" y="58.6" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="112.2" y="59.2" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="128.4" y="58.6" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="129.4" y="59.2" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="145.6" y="58.6" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="146.6" y="59.2" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="162.7" y="58.6" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="163.7" y="59.2" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="179.9" y="58.6" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="180.9" y="59.2" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="197.1" y="58.6" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="198.1" y="59.2" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="214.2" y="58.6" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="215.2" y="59.2" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="231.4" y="58.6" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="232.4" y="59.2" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="248.6" y="58.6" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="249.6" y="59.2" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="265.7" y="58.6" width="24.4" height="6.9" rx="1.4"/><rect class="dessus" x="266.7" y="59.2" width="22.4" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="301.8" y="58.6" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="302.8" y="59.2" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="319.0" y="58.6" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="320.0" y="59.2" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="336.1" y="58.6" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="337.1" y="59.2" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="34.0" y="66.8" width="28.7" height="6.9" rx="1.4"/><rect class="dessus" x="35.0" y="67.3" width="26.7" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="64.0" y="66.8" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="65.0" y="67.3" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="81.2" y="66.8" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="82.2" y="67.3" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="98.4" y="66.8" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="99.4" y="67.3" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="115.5" y="66.8" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="116.5" y="67.3" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="132.7" y="66.8" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="133.7" y="67.3" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="149.9" y="66.8" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="150.9" y="67.3" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="167.0" y="66.8" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="168.0" y="67.3" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="184.2" y="66.8" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="185.2" y="67.3" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="201.4" y="66.8" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="202.4" y="67.3" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="218.5" y="66.8" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="219.5" y="67.3" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="235.7" y="66.8" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="236.7" y="67.3" width="13.9" height="4.5" rx="1"/></g><g class="touche entree"><rect class="cote" x="252.9" y="66.8" width="37.3" height="6.9" rx="1.4"/><rect class="dessus" x="253.9" y="67.3" width="35.3" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="34.0" y="74.9" width="37.3" height="6.9" rx="1.4"/><rect class="dessus" x="35.0" y="75.5" width="35.3" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="72.6" y="74.9" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="73.6" y="75.5" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="89.8" y="74.9" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="90.8" y="75.5" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="107.0" y="74.9" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="108.0" y="75.5" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="124.1" y="74.9" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="125.1" y="75.5" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="141.3" y="74.9" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="142.3" y="75.5" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="158.5" y="74.9" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="159.5" y="75.5" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="175.6" y="74.9" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="176.6" y="75.5" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="192.8" y="74.9" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="193.8" y="75.5" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="210.0" y="74.9" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="211.0" y="75.5" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="227.1" y="74.9" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="228.1" y="75.5" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="244.3" y="74.9" width="45.9" height="6.9" rx="1.4"/><rect class="dessus" x="245.3" y="75.5" width="43.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="319.0" y="74.9" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="320.0" y="75.5" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="34.0" y="83.1" width="20.2" height="6.9" rx="1.4"/><rect class="dessus" x="35.0" y="83.7" width="18.2" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="55.5" y="83.1" width="20.2" height="6.9" rx="1.4"/><rect class="dessus" x="56.5" y="83.7" width="18.2" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="76.9" y="83.1" width="20.2" height="6.9" rx="1.4"/><rect class="dessus" x="77.9" y="83.7" width="18.2" height="4.5" rx="1"/></g><g class="touche espace"><rect class="cote" x="98.4" y="83.1" width="106.0" height="6.9" rx="1.4"/><rect class="dessus" x="99.4" y="83.7" width="104.0" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="205.7" y="83.1" width="20.2" height="6.9" rx="1.4"/><rect class="dessus" x="206.7" y="83.7" width="18.2" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="227.1" y="83.1" width="20.2" height="6.9" rx="1.4"/><rect class="dessus" x="228.1" y="83.7" width="18.2" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="248.6" y="83.1" width="20.2" height="6.9" rx="1.4"/><rect class="dessus" x="249.6" y="83.7" width="18.2" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="270.0" y="83.1" width="20.2" height="6.9" rx="1.4"/><rect class="dessus" x="271.0" y="83.7" width="18.2" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="301.8" y="83.1" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="302.8" y="83.7" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="319.0" y="83.1" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="320.0" y="83.7" width="13.9" height="4.5" rx="1"/></g><g class="touche"><rect class="cote" x="336.1" y="83.1" width="15.9" height="6.9" rx="1.4"/><rect class="dessus" x="337.1" y="83.7" width="13.9" height="4.5" rx="1"/></g><circle class="led allumee" cx="309.7" cy="48.7" r=".9"/><circle class="led" cx="326.9" cy="48.7" r=".9"/><circle class="led" cx="344.1" cy="48.7" r=".9"/><path class="boitier" d="M366 58 Q366 48 378 48 Q390 48 390 58 V80 Q390 94 378 94 Q366 94 366 80 Z"/><path d="M366 64 H390 M378 48 V64"/><rect class="molette" x="376" y="52" width="4" height="8" rx="2"/><path class="cable" d="M378 48 Q378 36 364 31 Q330 22 290 22"/></svg><div class="tour" aria-hidden="true"><i class="baie"></i><i class="baie"></i><i class="grille-air"></i></div></div>')
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
