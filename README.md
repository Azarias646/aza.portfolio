# Portfolio — Azarias Sawadogo

Site personnel : développeur systèmes et bases de données, data engineer junior.
En ligne (bientôt) sur **https://azarias-sawadogo.me**.

- Plan, décisions et étapes : [`PLAN.md`](PLAN.md)
- Composants et design (référence de la maquette) : [`maquette/COMPOSANTS.md`](maquette/COMPOSANTS.md)

## Stack

[Astro](https://astro.build) (site statique), CSS natif, TypeScript strict, JavaScript natif sans dépendance.
Police Roboto Flex auto-hébergée, avec les mêmes axes que la maquette (taille optique `opsz`, largeur `wdth`, graisse `wght`). Mise en ligne sur Cloudflare Pages ; analytics Umami (auto-hébergé) et
Cloudflare Web Analytics.

## Commandes

Node.js 22.22 ou plus (voir `.nvmrc`).

| Commande               | Rôle                                                       |
| ---------------------- | ---------------------------------------------------------- |
| `npm ci`               | Installer les dépendances (versions figées)                |
| `npm run dev`          | Serveur local avec rechargement : http://localhost:4321    |
| `npm run build`        | Vérifier les types (`astro check`) puis construire `dist/` |
| `npm run preview`      | Servir `dist/` en local                                    |
| `npm run format`       | Formater le code (Prettier)                                |
| `npm run format:check` | Vérifier le formatage (utilisé par la CI)                  |

**CI GitHub (à activer)** : le fichier est prêt dans [`docs/ci-github-actions.yml`](docs/ci-github-actions.yml)
(formatage, types, construction à chaque push). Pour l'activer, le copier tel quel dans
`.github/workflows/ci.yml` depuis github.com (« Add file → Create new file »).

## Organisation

```
src/
├── content/projets/     un fichier Markdown par projet (carte et fiche ; voir ci-dessous)
├── content/parcours/    un fichier Markdown par étape du parcours
├── content/outils.yaml  outils d'« À propos » par groupe, avec description et niveau
├── content.config.ts    schéma des contenus : un champ manquant ou faux bloque la construction
├── data/                infos du site et réseaux (site.ts), logos, icônes, illustrations du parcours
├── components/          Accueil, PcNom, APropos, Projets, Schema, Parcours, Contact, Nav, Points…
├── layouts/Base.astro   <head> (SEO, partage, thème, analytics), barre, écrans
├── scripts/             navigation par écrans, thème, fiches, boutons, analytics
└── styles/              jetons (tokens.css), base (global.css), écrans (ecrans.css)
public/                  fichiers servis tels quels (CV, favicon, icônes, manifeste, robots.txt, og.png)
docs/og/                 sources de l'image d'aperçu et des icônes (voir docs/og/README.md)
outils/police.py         prépare public/polices/roboto-flex.woff2 (axes et caractères utiles seulement)
maquette/                maquette validée et sa documentation (référence, non publiée)
archive/v1/              ancien portfolio, conservé pour mémoire
```

## Ajouter, modifier ou retirer un projet

Chaque projet est un fichier `src/content/projets/<nom>.md` :

```markdown
---
titre: Lakehouse
categorie: Ingénierie des données # Professionnel, Ingénierie des données, Personnel ou En équipe
resume: Un socle de données commun…
outils: [MinIO, Spark, Airflow, PySpark] # noms définis dans src/data/logos.ts
ordre: 2 # position dans la liste
brouillon: false # true pour cacher le projet sans le supprimer
schema: # schéma de la fiche (viewBox 360 × 170)
  noeuds:
    - { texte: GPS, x: 12, y: 22, largeur: 74, hauteur: 28 }
    - { texte: MinIO, x: 206, y: 62, largeur: 70, hauteur: 44, principal: true }
  liens:
    - { trace: 'M86 36 C104 36 104 84 118 84' }
---
```

Pour **retirer** un projet : supprimer le fichier, ou mettre `brouillon: true`.
Le schéma accepte aussi des `etiquettes` (texte libre sans bloc : `{ texte, x, y }`) et des liens `pointille: true`.

## Parcours

Chaque étape est un fichier `src/content/parcours/<nom>.md` :

```markdown
---
type: cursus # experience ou cursus (l'onglet où elle apparaît)
titre: Master Intelligence Artificielle
lieu: Nom de l'établissement # facultatif
annees: '2026' # texte libre : '2026', 2025 — 2026…
illustration: ia # poste, data, mobile, ia, pipeline, mainframe ou diplome
ordre: 1
---
```

## Outils (« À propos »)

Dans `src/content/outils.yaml`, chaque groupe liste ses outils dans l'ordre d'affichage :
`{ nom: Python, niveau: 2, description: '…' }`, avec `niveau` 1 (Notions), 2 (Opérationnel) ou 3 (Avancé).
Le nom doit exister dans `src/data/logos.ts`, qui fournit le logo.
Après un push sur `main`, Cloudflare Pages reconstruit et publie le site.

## Analytics

Aucun cookie, donc aucun bandeau de consentement. Les scripts ne sont chargés qu'en production et seulement si
les variables sont définies (Cloudflare Pages → Settings → Variables) ; voir `.env.example` :

- `PUBLIC_UMAMI_SRC`, `PUBLIC_UMAMI_WEBSITE_ID` : Umami sur le homelab (`stats.azarias-sawadogo.me`) ;
- `PUBLIC_CF_BEACON_TOKEN` : Cloudflare Web Analytics, pour comparer.

Les clics sont mesurés par l'attribut `data-umami-event="…"` (et `data-umami-event-<détail>`) posé dans les
composants ; les sections vues et les durées sont envoyées par `src/scripts/analytics.ts`.
Liste complète des mesures : [`PLAN.md`](PLAN.md), § 5 bis.
