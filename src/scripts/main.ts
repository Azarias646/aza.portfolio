/** Point d'entrée des scripts du site (chargé une fois, en module, par Base.astro). */
import { initBarreMobile } from './barre-mobile';
import { initBoutons } from './boutons';
import { initCopier } from './copier';
import { initEcrans } from './ecrans';
import { initFiches } from './fiches';
import { initOnglets } from './onglets';
import { initOutils } from './outils';
import { initPortrait } from './portrait';
import { initTheme } from './theme';

const reduit = matchMedia('(prefers-reduced-motion: reduce)').matches;

initTheme();
initEcrans(reduit);
initBarreMobile();
initFiches(reduit);
initOutils(reduit);
initOnglets(reduit);
initCopier();
initBoutons();
initPortrait(reduit);
