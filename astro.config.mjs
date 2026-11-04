// @ts-check
import { defineConfig, envField } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://docs.astro.build/en/reference/configuration-reference/
export default defineConfig({
  site: 'https://azarias-sawadogo.me',
  trailingSlash: 'ignore',
  integrations: [sitemap({ filter: (page) => !page.includes('/404') })],
  build: {
    // Petites feuilles de style intégrées à la page : une requête de moins au premier affichage.
    inlineStylesheets: 'auto',
  },
  env: {
    // Analytics : vides en local, renseignées dans Cloudflare Pages (Settings → Variables).
    // Sans valeur, aucun script de mesure n'est chargé.
    schema: {
      PUBLIC_UMAMI_SRC: envField.string({ context: 'client', access: 'public', optional: true }),
      PUBLIC_UMAMI_WEBSITE_ID: envField.string({ context: 'client', access: 'public', optional: true }),
      PUBLIC_CF_BEACON_TOKEN: envField.string({ context: 'client', access: 'public', optional: true }),
    },
  },
});
