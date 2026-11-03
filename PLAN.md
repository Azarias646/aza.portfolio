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

## 4. Stack (validée)

**Astro**, avec la possibilité d'ajouter plus tard des composants d'autres frameworks (Vue, etc.) seulement là où ce serait utile (« îlots »). Comparée à Vue seul, Vue + Nuxt, Astro + composants Vue et HTML simple ; choisie pour la légèreté, le référencement, la facilité de mise à jour et la reprise directe de la maquette.

| Rôle | Choix |
|---|---|
| Générateur | Astro (sortie HTML statique) |
| Contenu | Content collections en Markdown : un fichier par projet (`src/content/projets/`) et par étape du parcours (`src/content/parcours/`), avec vérification des champs. Ajouter / modifier / retirer = un fichier (`brouillon: true` pour cacher) |
| Style | CSS natif repris de la maquette (jetons, composants) |
| Polices | Roboto Flex auto-hébergée ; monospace système pour l'effet terminal |
| Images | `astro:assets` (WebP/AVIF à la bonne taille) |
| JavaScript | Natif, sans jQuery (navigation par écrans, version mobile, fenêtres, thème) |
| SEO | Sitemap + balises Open Graph |
| Qualité | Prettier + Lighthouse CI (objectif > 90) |
| Mise en ligne | GitHub Pages via GitHub Actions (reconstruction à chaque push sur `main`) |
| Analytics | Souhaité ; outil à choisir plus tard (piste : Umami auto-hébergé, sans cookies). S'ajoute par un script, sans impact sur la stack |

## 5. Étapes

1. ~~Valider la maquette~~ — **fait** : la maquette widgets est la maquette finale, version téléphone comprise (passe mobile validée : défilement normal, barre d'onglets en bas, voir § 4.3 de `maquette/COMPOSANTS.md`). Reste seulement à valider les niveaux de maîtrise des outils.
2. ~~Choisir la stack~~ — **fait** : Astro (voir § 4).
3. **Prochaine étape** — initialiser le projet Astro sur la branche `new` et reprendre la maquette widgets en composants, avec les projets et le parcours en fichiers Markdown.
4. Rédiger les études de cas des 4 projets + compléter le parcours.
5. SEO & partage : balises meta, Open Graph (aperçu LinkedIn/WhatsApp), favicon.
6. Accessibilité & perf : contrastes, alt des images, score Lighthouse > 90.
7. Déploiement sur GitHub Pages, puis remplacer la v1 (merge `new` → `main`).

## 6. Reste à décider

- Valider les niveaux de maîtrise des outils (tableau `fiches` de `maquette/index.html`).
- Nom de l'établissement du master IA (sous-titre du parcours).
- Outil d'analytics (hébergement : homelab ou service en ligne ; nom de domaine éventuel) et liste des événements à mesurer.
- Reporter les écarts assumés dans `aza-structure` (voir § 6 de `maquette/COMPOSANTS.md`).
