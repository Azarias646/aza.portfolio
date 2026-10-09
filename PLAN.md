# Portfolio v2 — Plan

Branche : `new` · Maquette : [`maquette/index.html`](maquette/index.html)

## 1. Ce qui change par rapport à la v1

| v1 (actuelle) | v2 (proposée) |
|---|---|
| Thème turquoise, fond image clair/sombre | Thème « éditorial » sombre, accent vert citron (bleu en mode clair) |
| Grille de logos de compétences | Compétences groupées par domaine (texte, plus lisible) |
| Carrousel jQuery + lightSlider pour les projets | Liste de projets numérotée, chaque projet → page « étude de cas » |
| jQuery + 2 plugins | HTML/CSS/JS natif, zéro dépendance |
| Pas de parcours | Section Parcours (DSI, IBM Z Xplore, licence, master) |
| Contact par icônes | Gros appel à l'action e-mail + liens sociaux |

## 2. Structure du site

1. **Hero** — nom en grand + portrait N&B, badge « DSI · Aïobi & BBS Holding », accroche data engineer & DSI, boutons *Projets* et *CV*.
2. **À propos** — grille « bento » : photo + bio, chiffres clés, compétences par domaine.
3. **Projets** — ERPNext multi-filiales, Lakehouse MinIO (GPS, Airflow, PySpark), Migration SAGE 100, AzaLab, NutriFaso, Agent Squad + explorations + archives (anciens projets Django/VBA).
4. **Parcours** — frise chronologique formation / expériences.
5. **Contact** — e-mail, GitHub, LinkedIn, WhatsApp.

## 3. Design

- **Typo** : Space Grotesk (titres/texte) + JetBrains Mono (détails « dev »).
- **Couleurs (sombre)** : fond `#0e0f0c`, texte `#edeae2`, gris `#9a978d`, accent `#c6f432`.
- **Couleurs (clair)** : fond `#f4f1ea`, texte `#141510`, accent `#3d5afe`.
- **Animations** : apparition au scroll, hover sur les projets, respect de `prefers-reduced-motion`.
- **Responsive** : mobile d'abord, grille bento qui passe en 2 colonnes.

## 4. Étapes

1. Valider la maquette (couleurs, sections, textes).
2. Monter la structure finale : `index.html`, `css/`, `js/`, `projets/<nom>.html`, `assets/` (images compressées en WebP).
3. Rédiger les études de cas des 4 projets + compléter le parcours.
4. SEO & partage : balises meta, Open Graph (aperçu LinkedIn/WhatsApp), favicon.
5. Accessibilité & perf : contrastes, alt des images, score Lighthouse > 90.
6. Déploiement sur GitHub Pages, puis remplacer la v1 (merge `new` → `main`).

## 5. À fournir

- Nom de l'école, années, stages/expériences pour le parcours.
- Captures d'écran des projets (ou je réutilise celles de `media/`).
- Choix : garder le vert citron ou une autre couleur d'accent ?
