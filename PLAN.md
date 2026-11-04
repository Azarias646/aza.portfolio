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
| Mise en ligne | **Cloudflare (validé)** : Cloudflare Pages (gratuit) + domaine **`azarias-sawadogo.me`** (disponibilité vérifiée), acheté chez Cloudflare Registrar (seul coût, ~10–20 €/an) + DNS Cloudflare. HTTPS automatique, redirection `www`, reconstruction à chaque push sur `main`, aperçu de chaque branche. E-mail au nom du domaine possible via Cloudflare Email Routing (renvoi vers Gmail) |
| Analytics | **Fait partie de la mise en ligne** (actif dès le premier jour), sans cookies donc sans bandeau de consentement. **Principal : Umami (validé), auto-hébergé sur ton infra (homelab)** — Umami + PostgreSQL en Docker, exposé en `stats.azarias-sawadogo.me` par un tunnel Cloudflare (aucun port ouvert chez toi), script servi depuis ton domaine pour limiter les bloqueurs de pubs. **Secondaire : Cloudflare Web Analytics**, seulement pour comparer les chiffres |

## 5. Étapes

1. ~~Valider la maquette~~ — **fait** : la maquette widgets est la maquette finale, version téléphone comprise (passe mobile validée : défilement normal, barre d'onglets en bas, voir § 4.3 de `maquette/COMPOSANTS.md`). Niveaux de maîtrise des outils validés.
2. ~~Choisir la stack~~ — **fait** : Astro (voir § 4).
3. ~~Construire le site Astro~~ — **fait** : initialiser le projet Astro sur la branche `new` et reprendre la maquette widgets en composants, avec les projets et le parcours en fichiers Markdown. Les composants sont **marqués dès cette étape pour l'analytics** (attributs d'événement sur les boutons, liens et fiches), pour qu'aucun suivi ne soit à rajouter après coup.
   - **Tranche 1 (validée)** : base du projet (Astro, TypeScript strict, Prettier, CI GitHub), mise en page, barre de navigation, repères, thème, accueil avec le PC, écran Projets avec le projet ERP (fiche et schéma), version téléphone, analytics branché. Ancien site rangé dans `archive/v1/`.
   - **Tranche 2 (validée, testée sur iPhone 12)** : les cinq projets, À propos (bento, fiche des outils avec jauge), Parcours (onglets, cartes illustrées), Contact (carte d'appel, copie de l'e-mail) et pied de page. Outils en YAML, étapes du parcours en Markdown. Tous les événements d'analytics prévus sont posés.
   - À faire à part : copier `docs/ci-github-actions.yml` dans `.github/workflows/ci.yml` (la session n'a pas le droit de créer ce fichier).
4. ~~Études de cas~~ — **abandonné** : les projets restent comme dans la maquette (carte + fiche avec schéma), sans page dédiée.
5. SEO & partage : balises meta, Open Graph (aperçu LinkedIn/WhatsApp), favicon.
6. Accessibilité & perf : contrastes, alt des images, score Lighthouse > 90.
7. **Mise en ligne et analytics, en même temps :**
   - acheter le nom de domaine chez Cloudflare et y relier le projet Cloudflare Pages (HTTPS, redirection `www`) ;
   - installer Umami sur le homelab (Docker : Umami + PostgreSQL, tunnel Cloudflare vers `stats.azarias-sawadogo.me`), activer Cloudflare Web Analytics pour la comparaison, et vérifier sur l'aperçu de la branche que chaque événement remonte bien ;
   - publier : fusion `new` → `main`, qui remplace la v1 ;
   - une semaine après : premier point sur les chiffres, et comparaison avec Cloudflare Web Analytics.

## 5 bis. Analytics : ce qu'on mesure (validé)

Sans cookies, sans adresse IP conservée, sans contenu saisi. Chaque bouton porte un attribut `data-umami-event="…"` (+ `data-umami-event-<détail>`), posé dans les composants Astro.

**1. Automatique (Umami) :** visiteurs et visites, provenance (LinkedIn, GitHub, Google, WhatsApp, direct), pays et langue, appareil / navigateur / système, liens marqués `?utm_source=…` (cv, linkedin, candidature…).

**2. Événements essentiels (contact et intérêt)**

| Événement | Détail | Question |
|---|---|---|
| `cv-telechargement` | endroit (accueil, pied de page) | Combien téléchargent le CV ? |
| `contact-clic` | — | Le bouton « Me contacter » fonctionne-t-il ? |
| `email-copie` | — | Combien récupèrent l'e-mail ? |
| `email-ecrire` | — | Combien ouvrent leur messagerie ? |
| `reseau-clic` | linkedin / github / whatsapp + endroit | Quel réseau pour te joindre ? |
| `projet-ouverture` | projet | Quel projet intéresse le plus ? |

**3. Engagement**

| Événement | Détail | Question |
|---|---|---|
| `section-vue` | Moi / À propos / Projets / Parcours / Contact | Jusqu'où vont-ils, où décrochent-ils ? |
| `outil-ouverture` | outil | Quelles compétences vérifient-ils ? |
| `parcours-onglet` | Expérience / Cursus | Expérience ou diplômes ? |

**4. Compléments (inclus)**

| Événement | Détail | Question |
|---|---|---|
| `theme-changement` | clair / sombre / auto | Quel thème préfèrent-ils ? |
| `section-temps` | section + durée par tranche (< 5 s, 5–15 s, 15–60 s, > 60 s), envoyé en quittant la section | Où passent-ils du temps ? |
| `projet-temps` | projet + durée par tranche, envoyé à la fermeture de la fiche | Lisent-ils vraiment la fiche et le schéma ? |

**Indicateurs suivis chaque mois :** taux de contact ((`email-copie` + `email-ecrire` + `reseau-clic` whatsapp) / visiteurs), téléchargements du CV, projet le plus ouvert, provenance des visiteurs qui contactent, décrochage par section.

**Plus loin (projet data) :** export quotidien des données Umami vers le lakehouse (MinIO, Airflow, Spark) et page « le site en chiffres ».

## 6. Reste à décider

- À compléter plus tard, sans bloquer : nom exact du master IA et établissement (fichier `src/content/parcours/master-ia.md`, champs `titre` et `lieu`).
- Reporter les écarts assumés dans `aza-structure` (voir § 6 de `maquette/COMPOSANTS.md`).
