/** Point d'entrée des scripts du site (chargé une fois, en module, par Base.astro). */
import { initBoutons } from './boutons';
import { initEcrans } from './ecrans';
import { initFiches } from './fiches';
import { initPortrait } from './portrait';
import { initTheme } from './theme';

const reduit = matchMedia('(prefers-reduced-motion: reduce)').matches;

initTheme();
initEcrans(reduit);
initFiches(reduit);
initBoutons();
initPortrait(reduit);
