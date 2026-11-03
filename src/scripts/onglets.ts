/**
 * Onglets du Parcours (motif ARIA « tabs ») : clic, flèches gauche / droite, Début / Fin.
 * Les cartes de l'onglet choisi réapparaissent en cascade.
 */
import { suivre } from './analytics';

export function initOnglets(reduit: boolean): void {
  const onglets = [...document.querySelectorAll<HTMLButtonElement>('[role="tab"][data-onglet]')];
  const choisir = (choisi: HTMLButtonElement) => {
    onglets.forEach((o) => {
      const actif = o === choisi;
      const panneau = document.getElementById(o.getAttribute('aria-controls') ?? '');
      o.setAttribute('aria-selected', String(actif));
      o.tabIndex = actif ? 0 : -1;
      if (!panneau) return;
      panneau.hidden = !actif;
      if (actif && !reduit) {
        panneau.classList.remove('rejoue');
        void panneau.offsetWidth; // relance l'animation
        panneau.classList.add('rejoue');
      }
    });
    suivre('parcours-onglet', { onglet: choisi.dataset['onglet'] ?? '' });
  };
  onglets.forEach((o, i) => {
    o.addEventListener('click', () => {
      if (o.getAttribute('aria-selected') !== 'true') choisir(o);
    });
    o.addEventListener('keydown', (e) => {
      const cibles: Record<string, number> = {
        ArrowRight: (i + 1) % onglets.length,
        ArrowLeft: (i - 1 + onglets.length) % onglets.length,
        Home: 0,
        End: onglets.length - 1,
      };
      const cible = onglets[cibles[e.key] ?? -1];
      if (!cible) return;
      e.preventDefault();
      cible.focus();
      choisir(cible);
    });
  });
}
