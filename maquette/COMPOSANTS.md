# Composants du portfolio

Référence des composants de la maquette **widgets** (`maquette/widgets.html`), la version retenue à ce stade.
Toutes les valeurs ci-dessous sont celles du code. Si le code change, ce document change avec lui.

- Design system de base : [`Azarias646/aza-structure`](https://github.com/Azarias646/aza-structure), dossier `design-system/` (v0.2.0).
- Écarts assumés par rapport à ce design system : voir [§ 6](#6-écarts-au-design-system).

---

## 1. Fichiers et génération

Les maquettes sont générées en couches. Chaque fichier part du précédent et ajoute ses règles en fin de `<style>` ou remplace des morceaux précis du HTML et du script.

```
index.html          base : contenu, jetons aza-structure, écrans plein écran
 └─ flat.html        aplats, aucune ombre, transition « poussée » rapide        (scripts/mk_flat.py)
     ├─ fondu.html   défilement continu, blocs en fondu à l'entrée              (scripts/mk_fondu.py)
     └─ ecrans-fondu.html  plein écran + fondu doux du contenu et du nom         (scripts/mk_ecrans.py)
         └─ widgets.html   cartes, pastilles, pilules, bento, jauge, navbar      (scripts/mk_widgets.py)
```

**Règle :** on ne modifie à la main que `index.html` et les scripts. Les autres fichiers se régénèrent :

```bash
cd aza.portfolio
for f in mk_apercu mk_flat mk_fondu mk_ecrans mk_widgets; do python3 maquette/scripts/$f.py; done
```

Chaque script écrit aussi une copie « aperçu » (chemins d'images relatifs, prête à publier) dans `maquette/apercu/` (ignoré par git), ou dans le dossier donné par la variable `APERCU`.

Les logos des outils viennent de [Simple Icons](https://simpleicons.org) (licence CC0), intégrés en SVG dans le HTML. OSINT, GEOINT et Hermes Agent n'ont pas de logo officiel : icônes simples dessinées au trait.

---

## 2. Jetons

Les composants n'utilisent que ces variables, jamais une couleur écrite en dur (sauf la barre de navigation, § 3.1).

| Jeton | Sombre | Clair | Rôle |
|---|---|---|---|
| `--page` / `--fond` | `#0b0b0c` | `#ededef` | Fond des écrans |
| `--surface` | `#1c1c20` | `#ffffff` | Fond des petits éléments, mot en filigrane |
| `--surface-2` | `#2a2a30` | `#f1f1f3` | Pilules, survol, fond de jauge |
| `--filet` | `#2a2a30` | `#e2e2e6` | Séparateurs |
| `--carte` | dégradé 160° `#24242a` → `#18181c` | dégradé 160° `#ffffff` → `#f6f6f8` | Fond de toutes les cartes |
| `--texte` | `#f2f3f3` | `#141516` | Texte principal |
| `--texte-attenue` | `#a3a6ab` | `#5a5f63` | Texte secondaire, libellés |
| `--texte-discret` | `#8b8f95` | `#6b7075` | Mentions |
| `--accent` | `#1d5a4e` | `#1d5a4e` | Aplat vert : bouton principal, pastilles, jauge |
| `--accent-survol` | `#256b5e` | `#256b5e` | Aplat vert survolé |
| `--accent-texte` | `#7ccbb7` | `#256b5e` | Texte et « / » en vert |
| `--accent-trait` | `#7ccbb7` | `#2e7d6c` | Traits, repère actif, focus |
| `--sur-accent` | `#e6f4f0` | `#ffffff` | Texte et logo posés sur l'aplat vert |

| Rayon | Valeur | Usage |
|---|---|---|
| `--rayon-sm` | 10 px | Petits éléments |
| `--rayon-md` | 16 px | Éléments moyens |
| `--rayon-lg` | 22 px | Zone du schéma |
| `--rayon-xl` | 28 px | Cartes, fenêtres |
| `--rayon-pilule` | 999 px | Boutons, pilules, pastilles |

| Mouvement | Valeur |
|---|---|
| `--duree-rapide` | 120 ms (survol, appui) |
| `--duree-standard` | 220 ms (ouverture d'une fenêtre) |
| `--courbe-sortie` | `cubic-bezier(.2, .8, .2, 1)` |

**Police :** Roboto Flex (repli Manrope). Titres élargis avec `font-variation-settings: 'wdth' 125`. Dans la maquette, chargée depuis Google Fonts. Dans la version finale, elle sera hébergée avec le site.

**Thème :** il suit le réglage du système (`prefers-color-scheme`). Le bouton de thème force `data-theme="dark"` ou `"light"` sur `<html>`, et le choix est mémorisé dans `localStorage` (clé `theme`).

---

## 3. Composants

### 3.1 Barre de navigation — `nav`

Barre flottante en haut de l'écran.

- **Structure :** `nav > .wrap > (.marque, .liens > a × 4, .theme)`. Chaque lien contient `svg.ico` + `<span>` libellé.
- **Fond :** pseudo-élément `nav .wrap::before`, coins 18 px, dégradé 180° `#1d1d21` → `#101012`, bordure 1 px `rgba(255,255,255,.08)` (bas à `.03`). En clair : `#ffffff` → `#f1f1f3`, bordure `rgba(0,0,0,.07)`.
- **Halo :** `nav::after`, dégradé radial blanc à 7 % sous la barre (noir à 6 % en clair).
- **Liens :** gras 600, 15 px, padding 10 × 16 px, coins 12 px, couleur `--texte-attenue`. Survol : fond blanc à 5 %, texte `--texte`.
- **Lien actif** (`a.active`, posé par le script selon l'écran affiché) : fond blanc à 6 %, texte `--texte`, partie claire de l'icône en `--accent-trait`.
- **Icônes `svg.ico` :** 22 px, en deux tons. Formes en `#8d9096`, `.moyen` en `#b8bbbf`, `.clair` en `#d9dbdd`. À propos : silhouette. Projets : cube. Parcours : drapeau. Contact : bulle.
- **Mobile (< 760 px) :** liens masqués. Restent le nom et le bouton de thème.

### 3.2 Bouton de thème — `button.theme`

- Icône seule de 18 px dans un carré de 36 px, sans fond. Couleur `--texte-discret`, `--texte` au survol.
- Trois états en boucle : automatique (demi-disque), sombre (lune), clair (soleil).
- `aria-label` et `title` donnent l'état : « Thème : automatique / sombre / clair ».

### 3.3 Repères d'écran — `ol.points`

- Colonne fixe à droite, centrée verticalement. Un `button` de 28 × 28 px par écran.
- Point de 6 × 6 px en `--texte-discret`. L'écran affiché porte `aria-current="true"` et son repère s'allonge à 20 px en `--accent-trait` (220 ms).
- Chaque bouton a un `aria-label` (« Accueil », « À propos »…). Un clic va à l'écran.

### 3.4 Boutons — `.btn`

| Variante | Classe | Style |
|---|---|---|
| Principal | `.btn.principal` | Pilule, aplat `--accent`, texte `--sur-accent` ; au survol, remplissage `--accent-texte`, texte `--page` |
| Secondaire | `.btn.second` | Pilule en contour 1 px `--texte-discret`, fond transparent, texte `--texte` ; au survol, remplissage `--texte`, texte `--page` |

- Hauteur 48 px, padding 0 × 24 px, gras 600. Icône éventuelle 16 px au trait.
- Appui : `scale(.98)` en 120 ms.
- **Un seul bouton principal par zone.**
- **Survol : remplissage directionnel** (*direction-aware hover*).
  - Le fond (`::before`, couleur `--balayage`) entre par le côté où arrive le curseur et repart par le côté où il sort. Glissement de 460 ms, `cubic-bezier(.65, 0, .35, 1)`.
  - Le texte change de couleur en 160 ms, avec 200 ms de retard : il bascule quand le fond le recouvre à moitié.
  - Le script lit le côté d'entrée et de sortie (`pointerenter` / `pointerleave`) et le passe dans la variable `--bx`. La classe `.rempli` marque l'état survolé.
  - Pas d'effet au toucher (écran tactile).

### 3.5 Carte

- Fond `--carte` (dégradé), coins `--rayon-xl` (28 px), aucune bordure, aucune ombre.
- Utilisée par : `.recit`, `.groupe`, `.projet`, `.parcours > div`, `.courriel`, `.reseau`, `dialog.fiche`, `dialog.fiche-projet`.
- Survol (cartes cliquables `.projet`, `a.reseau`) : contour 1 px `--surface-2`.

### 3.6 Pastille — `.pastille`, `.outil svg.logo`

- Rond plein `--accent`, logo en `--sur-accent`.

| Contexte | Rond | Logo |
|---|---|---|
| Liste d'outils (À propos) | 34 px (marge 8 px) | 18 px |
| Contact (réseaux) | 44 px | 20 px |
| Contact (e-mail) | 52 px | 20 px |
| Fenêtre d'un outil | 48 px | 24 px |

- Logo au trait (OSINT, GEOINT) : classe `.trace`, contour au lieu du remplissage.

### 3.7 Pilule (étiquette) — `.pile span`

- Logo 14 px + nom. Padding 7 × 14 px, coins 999 px, fond `--surface-2`, texte 12,5 px.
- Sert à lister les outils d'un projet (carte et fenêtre).

### 3.8 Liste d'outils — `.groupe`, `button.outil`

- Une carte par groupe : titre `h3` (17 px, 600), puis une grille `auto-fill` de colonnes de 150 px minimum (128 px pour Développement).
- Chaque outil est un `button` : pastille + nom, fond transparent, coins 999 px. Survol : fond `--surface-2`, logo agrandi à 108 %.
- **Clic :** ouvre la fiche de l'outil (§ 3.10).
- Groupes : Data, Systèmes, Développement, Renseignement en sources ouvertes.

### 3.9 Bento « À propos » — `.apropos`

Grille de 4 colonnes, écart 12 px. `.outils` est en `display: contents`, pour que ses groupes se placent directement dans la grille.

| Élément | Colonnes | Rangée |
|---|---|---|
| Récit (`.recit`) | 1–2 | 1–2 |
| Data | 3–4 | 1 |
| Systèmes | 3–4 | 2 |
| Développement | 1–3 | 3 |
| Renseignement | 4 | 3 (outils en une colonne) |

- Sous 900 px : 2 colonnes, chaque carte sur toute la largeur. Sous 760 px : une colonne.

### 3.10 Fiche d'un outil — `dialog#fiche`

- `<dialog>` modal, largeur max 440 px, carte. S'ouvre avec `showModal()`. Se ferme par ×, Échap ou un clic à côté. Le focus va à la fenêtre elle-même (`autofocus`).
- **En-tête :** pastille de 48 px (§ 3.6), nom (20 px, gras), bouton fermer 36 px.
- **Texte :** une phrase qui décrit l'outil (tableau `fiches` dans le script).
- **Jauge en demi-cercle** (`.jauge`, SVG `viewBox 0 0 220 142`) :
  - arc de rayon 88, épaisseur 26 ; fond `--surface-2`, valeur `--accent` (`stroke-dasharray: 277`) ;
  - aiguille de 5 px en `--texte`, axe de 7 px de rayon ;
  - bornes « Notions » et « Avancé » écrites sous chaque extrémité (11 px, `--texte-attenue`) ;
  - le niveau en clair dessous (20 px, gras) ;
  - 3 niveaux : Notions = 1/3, Opérationnel = 2/3, Avancé = 3/3. À l'ouverture, l'arc se remplit et l'aiguille tourne en 900 ms.
- Ouverture : fondu et légère montée en 220 ms.

### 3.11 Carte projet — `a.projet`

- Carte (§ 3.5), padding 26 × 28 px, sur une colonne avec 12 px d'écart.
- Contenu : type (12,5 px, `--texte-attenue`), titre (22–30 px, `wdth` 112), description (72 caractères max par ligne), pilules d'outils.
- Bouton rond `.fleche` « + » de 48 px, aplat `--accent`. Il signale qu'un clic ouvre la fiche.
- Le schéma du projet est rangé dans un `<template class="schema-src">` dans la carte : il n'est pas affiché dans la liste.
- **Clic :** ouvre la fiche du projet (§ 3.12). **Aucun aperçu au survol** (choix validé).

### 3.12 Fiche d'un projet et schéma — `dialog#fiche-projet`, `svg.schema`

- `<dialog>` modal, largeur max 720 px, carte. Contient : type, titre, schéma, description, pilules.
- **Schéma** (`viewBox 0 0 360 170`) :
  - blocs `rect.n` : coins 14 px, fond `--surface-2` ;
  - bloc principal `rect.n.a` : fond `--accent`, texte `--sur-accent` ;
  - liens `path.l` (1,2 px, `--texte-discret`), lien principal `path.l.a` (1,6 px, `--accent-trait`), liens en pointillé `.pointille`.
- **Animation :** les liens se tracent à l'ouverture (`stroke-dashoffset` de 400 à 0, 1,1 s).
- Zone du schéma : fond `--page`, coins 22 px.

### 3.13 Parcours — `.parcours`, `.etape`

- Deux cartes côte à côte : « Expérience » et « Cursus et certifications » (titre `.colonne`, 17 px, 600).
- Chaque `.etape` est une grille 136 px + reste : année (17 px, gras), puis intitulé `h4` et lieu.
- Étapes séparées par un filet 1 px.
- Étape en cours (`.etape.actuelle`) : année dans une pilule `--accent`, texte `--sur-accent`, sur une seule ligne.
- Mobile : une seule colonne ; l'année passe au-dessus de l'intitulé.

### 3.14 Contact — `.cta`, `footer.pied`

L'écran Contact a deux blocs, traités comme la barre de navigation : même fond dégradé (`--barre-fond`), même bordure fine (`--barre-bord`), mêmes icônes.

| Jeton | Sombre | Clair |
|---|---|---|
| `--barre-fond` | dégradé 180° `#1d1d21` → `#101012` | dégradé 180° `#ffffff` → `#f1f1f3` |
| `--barre-bord` | `rgba(255,255,255,.08)` | `rgba(0,0,0,.07)` |
| `--cta-halo` | `rgba(29,90,78,.55)` | `rgba(29,90,78,.16)` |

- **Carte d'appel à l'action (`.cta`)** :
  - coins 28 px, padding 52 × 48 px ;
  - halo vert (`--cta-halo`) en haut à droite, par-dessus `--barre-fond` ;
  - deux colonnes : à gauche, le titre « / Envie de collaborer ou d'échanger ? » (30–48 px) ; à droite, l'adresse e-mail en grand (sélectionnable), suivie de deux icônes d'action discrètes ;
  - **pas de libellé ni de surbrillance** sur l'e-mail (choix validés) ;
  - **icônes d'action (`.icone-action`)** : ronds de 40 px sans fond, icône au trait de 19 px en `--texte-discret`. Au survol, fond `--surface-2` et icône `--texte`. À l'appui, `scale(.94)` ;
    - **Copier** (`#copier`, deux carrés) : utilise `navigator.clipboard`, ou sélectionne l'adresse si ce n'est pas possible. L'icône devient une coche verte (`--accent-trait`) pendant 1,8 s, et l'`aria-label` passe à « Adresse copiée » ;
    - **Écrire** (flèche ↗) : lien `mailto:`. `aria-label` « Écrire un e-mail ».
- **Pied de page (`footer.pied`)** :
  - carte aux coins 28 px, padding 36 × 40 px ;
  - grille de 4 colonnes : nom et rôle | Navigation | Réseaux | Documents ;
  - **Navigation :** mêmes liens et mêmes icônes bicolores que la barre (À propos, Projets, Parcours) ;
  - **Réseaux :** LinkedIn, GitHub, WhatsApp avec leur logo 20 px gris ;
  - **Documents :** Mon CV, avec une icône de document au trait ;
  - liens : 14 px, gras 600, `--texte-attenue`. Au survol : `--texte`, et l'icône passe en `--accent-trait` ;
  - **ligne du bas** (`.pied-bas`), sous un filet : « © 2026 Azarias Sawadogo · Logos : Simple Icons » à gauche, icônes des réseaux à droite (ronds de 40 px, logo 18 px, `aria-label`).
- **Mobile (< 760 px) :** la carte passe sur une colonne. Le pied passe sur 2 colonnes, le nom sur toute la largeur.
- Les liens internes du pied (`#apropos`…) changent d'écran comme ceux de la barre. Les liens externes ouvrent un nouvel onglet.

### 3.15 Titre de section — `.tete`

- `h2` (32–48 px, `wdth` 125) précédé d'une barre `/` en `--accent-texte` (`.barre`).
- Derrière, un **mot en filigrane** `.filigrane` (72–210 px, plein, couleur `--surface`). Mots : Profil, Réalisations, Parcours, Contact.

### 3.16 Portrait — `.scene`, `figure.portrait`

- Photo en noir et blanc, coins 12 px, posée sur un rectangle `--accent` décalé de 24 px en bas à droite.
- **S'incline vers le pointeur** : 8° au plus à l'horizontale, 6° à la verticale. Désactivé sur écran tactile et quand les animations sont réduites.

---

## 4. Navigation et animations

### 4.1 Écrans plein écran — `main.diapos > section.diapo`

- 5 écrans superposés : accueil, À propos, Projets, Parcours, Contact. Un seul est visible (`.active`).
- Un écran plus haut que la fenêtre défile à l'intérieur. On ne change d'écran qu'une fois arrivé en bas (ou en haut).
- **Commandes :**
  - molette ou trackpad (cumul de 24 px) ;
  - glissement du doigt (60 px) ;
  - ↓, Page suivante et Espace pour avancer ; ↑ et Page précédente pour reculer ; Début et Fin ;
  - liens du menu, repères, boutons internes ;
  - adresse `#apropos`, `#projets`… (au chargement et à chaque changement d'adresse).
- **Transition (poussée verticale) :** l'écran actuel monte de 100 % pendant que le suivant arrive d'en bas. 560 ms, `cubic-bezier(.65, 0, .35, 1)`. Sens inverse pour remonter.
- Pendant la transition, les gestes sont ignorés. Ils sont acceptés 60 ms après la fin.

### 4.2 Apparition du contenu

- Un écran qui n'est pas affiché porte la classe `.attente` : son contenu est masqué (transparent, 14 px plus bas).
- Pendant la transition (à 40 % de la durée), `.attente` est retirée et le contenu apparaît en fondu doux :
  - titre : 1,1 s (fondu), 1,3 s (montée), décalé de 120 ms ;
  - filigrane : 1,8 s ;
  - éléments en cascade (`.cascade`, rang `--i` posé par le script) : décalés de 260 ms + 110 ms par rang.
- **Nom (accueil) :** chaque ligne (`.ligne-nom`) apparaît en fondu, à l'ouverture du site et à chaque retour sur l'accueil (« Sawadogo » 160 ms après « Azarias »).

### 4.3 Accessibilité

- `prefers-reduced-motion: reduce` coupe toutes les animations et transitions. Le changement d'écran devient instantané.
- Focus clavier visible : contour 2 px `--accent-trait`.
- Fenêtres : vrais `<dialog>`, fermeture à Échap, `aria-labelledby` sur le titre.
- Icônes décoratives en `aria-hidden="true"`. Boutons sans texte avec `aria-label`.

---

## 5. Contenu et données

- Niveaux de maîtrise : tableau `fiches` dans le script de `index.html` (texte + niveau 1 à 3). **Les niveaux sont des propositions à valider.**
- Schémas des projets : un SVG par projet, dans le `<template class="schema-src">` de chaque carte projet de `index.html`. Classes : `n` (bloc), `n a` (bloc principal), `l` (lien), `l a` (lien principal), `pointille`.

---

## 6. Écarts au design system

| Règle aza-structure | Portfolio | Raison |
|---|---|---|
| Composants plats | Cartes avec léger dégradé, halo sous la navbar | Style widgets choisi |
| Aucune section qui glisse ; un seul moment orchestré par écran | Transition entre écrans + apparition en cascade | Demandé |
| Échelle de rayons 6/8/12/18/26 | 10/16/22/28 | Style widgets, plus arrondi |
| Couleurs uniquement par jetons | Navbar, carte d'appel et pied de page : dégradé et icônes grises propres (`--barre-fond`, `--barre-bord`, gris d'icônes en dur) | Reproduit les références |

Si ces choix sont confirmés, il faudra les reporter dans `aza-structure` (nouvelle version du design system) plutôt que de les laisser comme exceptions.
