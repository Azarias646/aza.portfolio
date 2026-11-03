import { defineCollection } from 'astro:content';
import { file, glob } from 'astro/loaders';
import { z } from 'astro/zod';
import { nomsLogos } from './data/logos';
import { nomsVignettes } from './data/vignettes';

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

/** Texte libre posé sur le schéma (sans bloc). */
const etiquette = z.object({ texte: z.string(), x: z.number(), y: z.number() });

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
      etiquettes: z.array(etiquette).default([]),
    }),
  }),
});

/** Outils de « À propos » : src/content/outils.yaml, un groupe par entrée (le nom de l'outil choisit son logo). */
const outils = defineCollection({
  loader: file('src/content/outils.yaml'),
  schema: z.object({
    id: z.enum(['Data', 'Systèmes', 'Développement', 'Renseignement en sources ouvertes']),
    ordre: z.number().int(),
    outils: z
      .array(
        z.object({
          nom: z.enum(nomsLogos),
          niveau: z.union([z.literal(1), z.literal(2), z.literal(3)]),
          description: z.string(),
        }),
      )
      .min(1),
  }),
});

/** Étapes du parcours : un fichier Markdown par étape dans src/content/parcours/. */
const parcours = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/parcours' }),
  schema: z.object({
    type: z.enum(['experience', 'cursus']),
    titre: z.string(),
    lieu: z.string().optional(),
    annees: z.string(),
    illustration: z.enum(nomsVignettes),
    ordre: z.number().int(),
    brouillon: z.boolean().default(false),
  }),
});

export const collections = { projets, outils, parcours };
