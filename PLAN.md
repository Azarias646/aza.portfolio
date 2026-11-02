# Portfolio v2 — Plan

Branche : `new` · **Maquette finale : [`maquette/widgets.html`](maquette/widgets.html)** (« Portfolio Azarias widgets ») · **Composants : [`maquette/COMPOSANTS.md`](maquette/COMPOSANTS.md)**

## 1. Ce qui change par rapport à la v1

| v1 (actuelle) | v2 (maquette widgets) |
|---|---|
| Thème turquoise, fond image clair/sombre | Design system `aza-structure` 0.2.0 (vert `#1D5A4E`) en style « widgets » : cartes sombres arrondies, pastilles rondes, pilules |
| Page qui défile | Navigation plein écran : un écran par section, transition par poussée, contenu qui apparaît en fondu |
| Grille de logos de compétences | Bento « À propos » : récit + outils par domaine, fiche de chaque outil avec jauge de niveau |
| Carrousel jQuery des projets | Cartes de projets ; au clic, fiche avec schéma de fonctionnement |
| Pas de parcours | Parcours en deux cartes : Expérience / Cursus et certifications |
| Contact par icônes | Carte d'appel à l'action (e-mail + icônes copier / écrire) et pied de page en colonnes |
| jQuery + 2 plugins | HTML/CSS/JS natif, zéro dépendance |

## 2. Structure du site

1. **Accueil (« Moi »)** — « Développeur systèmes et bases de données · Data engineer junior », nom en grand (fondu ligne par ligne) affiché sur l'écran d'un PC de bureau en traits fins (`~ $ whoami`, curseur, clavier, souris, tour), portrait N&B qui s'incline au pointeur, accroche, boutons *Me contacter* et *Mon CV*.
2. **À propos** — récit en trois paragraphes + outils avec logos en bento (Data, Systèmes, Développement, Renseignement en sources ouvertes).
3. **Projets** — ERP de facturation et comptabilité, Lakehouse, Homelab, NutriFaso, Automatisation IA.
4. **Parcours** — onglets Expérience (poste actuel, stages) et Cursus et certifications (master IA, certificat IBM Data Engineering sur Coursera, IBM Z Xplore, licence UUA), années seulement.
5. **Contact** — « Envie de collaborer ou d'échanger ? », e-mail avec icônes copier / écrire, puis pied de page (navigation, réseaux, CV).

## 3. Design

Tout le détail (jetons, composants, animations, accessibilité, écarts au design system) est dans [`maquette/COMPOSANTS.md`](maquette/COMPOSANTS.md).

En résumé : design system `aza-structure` 0.2.0 (vert `#1D5A4E`, Roboto Flex, neutres sans teinte) habillé en style « widgets » (cartes sombres arrondies, pastilles rondes, pilules, bento), navigation plein écran avec transition par poussée et contenu qui apparaît en fondu doux, repères d'écran à droite (nom au survol, en vert, police terminal), filigranes discrets derrière les titres.

## 4. Étapes

1. ~~Valider la maquette~~ — **fait** : la maquette widgets est la maquette finale (reste seulement à valider les niveaux de maîtrise des outils).
2. **Prochaine étape** — monter la structure finale à partir de la maquette widgets : `index.html`, `css/`, `js/`, `projets/<nom>.html`, `assets/` (images compressées en WebP).
3. Rédiger les études de cas des 4 projets + compléter le parcours.
4. SEO & partage : balises meta, Open Graph (aperçu LinkedIn/WhatsApp), favicon.
5. Accessibilité & perf : contrastes, alt des images, score Lighthouse > 90.
6. Déploiement sur GitHub Pages, puis remplacer la v1 (merge `new` → `main`).

## 5. Reste à décider

- Valider les niveaux de maîtrise des outils (tableau `fiches` de `maquette/index.html`).
- Nom de l'établissement du master IA (sous-titre du parcours).
- Valider la passe mobile (barre d'onglets en bas, défilement normal, voir § 4.3 de `maquette/COMPOSANTS.md`).
- Reporter les écarts assumés dans `aza-structure` (voir § 6 de `maquette/COMPOSANTS.md`).
