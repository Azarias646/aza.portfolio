# Portfolio v2 — Plan

Branche : `new` · Maquette retenue : [`maquette/widgets.html`](maquette/widgets.html) · **Composants : [`maquette/COMPOSANTS.md`](maquette/COMPOSANTS.md)**

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

1. **Présentation** — « Développeur systèmes et bases de données · Data engineer junior », nom en grand, portrait N&B, accroche, boutons *Me contacter* et *Mon CV*.
2. **À propos** — un vrai texte de présentation + les outils avec leurs logos (Données, Systèmes, Développement, OSINT / GEOINT).
3. **Projets** — ERP de facturation et comptabilité, Lakehouse, Homelab, NutriFaso, Automatisation IA.
4. **Parcours** — années seulement : master IA (2026, en cours), poste actuel, IBM Z Xplore, stages, licence.
5. **Contact** — « Envie de collaborer ou d'échanger ? » : e-mail (avec bouton copier), LinkedIn, GitHub, WhatsApp.

## 3. Design

Tout le détail (jetons, composants, animations, accessibilité, écarts au design system) est dans [`maquette/COMPOSANTS.md`](maquette/COMPOSANTS.md).

En résumé : design system `aza-structure` 0.2.0 (vert `#1D5A4E`, Roboto Flex, neutres sans teinte) habillé en style « widgets » (cartes sombres arrondies, pastilles rondes, pilules, bento), navigation plein écran avec transition par poussée et contenu qui apparaît en fondu doux.

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
