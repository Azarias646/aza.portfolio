# Image d'aperçu (Open Graph)

`og.html` est la source de `public/og.png` (1200 × 630), l'image affichée quand le lien du site est partagé
(LinkedIn, WhatsApp…). Pour la régénérer après une modification, avec Playwright :

```bash
npx playwright screenshot --viewport-size=1200,630 docs/og/og.html public/og.png
```

(`npm run build` doit avoir été lancé au moins une fois : la police vient de `node_modules`.)
