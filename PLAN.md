# Portfolio v2 — Plan

Branche : `new` · Maquette : [`maquette/index.html`](maquette/index.html)

## 1. Ce qui change par rapport à la v1

| v1 (actuelle) | v2 (proposée) |
|---|---|
| Thème turquoise, fond image clair/sombre | Design system `aza-structure` 0.2.0 : neutres sans teinte, un seul accent vert turquoise |
| Grille de logos de compétences | Compétences groupées par domaine (texte, plus lisible) |
| Carrousel jQuery + lightSlider pour les projets | Liste de projets numérotée, chaque projet → page « étude de cas » |
| jQuery + 2 plugins | HTML/CSS/JS natif, zéro dépendance |
| Pas de parcours | Section Parcours (DSI, stages Aïobi & Foulisa, licence UUA, IBM Z Xplore, master) |
| Contact par icônes | Gros appel à l'action e-mail + liens sociaux |

## 2. Structure du site

1. **Hero** — nom en grand + portrait N&B, badge « DSI · Aïobi & BBS Holding », accroche data engineer & DSI, boutons *Projets* et *CV*.
2. **À propos** — grille « bento » : photo + bio, chiffres clés, compétences par domaine.
3. **Projets** — ERPNext multi-filiales, Lakehouse MinIO (GPS, Airflow, PySpark), Migration SAGE 100, AzaLab, NutriFaso, Agent Squad + explorations + archives (anciens projets Django/VBA).
4. **Parcours** — frise chronologique formation / expériences.
5. **Contact** — e-mail, GitHub, LinkedIn, WhatsApp.

## 3. Design — `Azarias646/aza-structure` (design-system/, v0.2.0)

- **Thèmes** : sombre en référence, clair toujours disponible ; suit le système, choix manuel possible.
- **Couleurs** : uniquement les rôles des jetons (`page`, `surface`, `filet`, `texte`, `accent`…), neutres sans teinte, un seul accent (`#1D5A4E` / `#7CCBB7` en sombre).
- **Typo** : Roboto Flex (Manrope en repli), auto-hébergées. Titres de vitrine élargis (`wdth` 125), chiffres clés condensés (`wdth` 88, `tabular-nums`). Pas de police mono, pas de capitales.
- **Formes** : rayons 6 / 8 / 12 / 18 / 26 px, pilule pour l'action principale.
- **Lumière** : halo de scène derrière le portrait, une seule carte éclairée par la lueur d'accent ; composants plats.
- **Mouvement** : un seul moment à l'ouverture (arrivée du portrait, 600 ms), portrait qui s'incline au pointeur, enfoncement à l'appui ; aucune apparition au scroll ; mouvement réduit respecté.

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
