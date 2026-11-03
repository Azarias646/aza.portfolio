import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';
import { nomsLogos } from './data/logos';

/** Un bloc du schéma de fonctionnement (coordonnées dans un viewBox de 360 × 170). */
const noeud = z.object({
  texte: z.string(),
  x: z.number(),
  y: z.number(),
  largeur: z.number().positive(),
  hauteur: z.number().positive(),
  principal: z.boolean().default(false),
});

/** Un lien du schéma : tracé SVG (attribut `d`). */
const lien = z.object({
  trace: z.string(),
  principal: z.boolean().default(false),
  pointille: z.boolean().default(false),
});

/**
 * Projets : un fichier Markdown par projet dans `src/content/projets/`.
 * Le corps du fichier (facultatif) deviendra la page d'étude de cas.
 */
const projets = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/projets' }),
  schema: z.object({
    titre: z.string(),
    categorie: z.enum(['Professionnel', 'Ingénierie des données', 'Personnel', 'En équipe']),
    resume: z.string(),
    outils: z.array(z.enum(nomsLogos)).min(1),
    ordre: z.number().int(),
    brouillon: z.boolean().default(false),
    schema: z.object({
      noeuds: z.array(noeud).min(1),
      liens: z.array(lien).default([]),
    }),
  }),
});

export const collections = { projets };
