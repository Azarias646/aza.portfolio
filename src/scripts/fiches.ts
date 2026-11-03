/**
 * Fenêtres (<dialog>) des projets : ouverture depuis la carte, fermeture par le bouton,
 * Échap ou un clic à côté ; le schéma se trace à l'ouverture ; durée de lecture mesurée.
 */
import { chrono, suivre, tranche } from './analytics';

export function initFiches(reduit: boolean): void {
  document.querySelectorAll<HTMLButtonElement>('[data-fiche]').forEach((bouton) => {
    const fiche = document.getElementById(bouton.dataset['fiche'] ?? '');
    if (!(fiche instanceof HTMLDialogElement)) return;
    const temps = chrono();

    bouton.addEventListener('click', () => {
      const schema = fiche.querySelector('.schema');
      if (schema && !reduit) {
        schema.classList.add('trace');
        requestAnimationFrame(() => requestAnimationFrame(() => schema.classList.remove('trace')));
      }
      fiche.showModal();
      temps.debut();
    });
    fiche.querySelector('[data-fermer]')?.addEventListener('click', () => fiche.close());
    fiche.addEventListener('click', (e) => {
      if (e.target === fiche) fiche.close();
    });
    fiche.addEventListener('close', () => {
      const duree = temps.fin();
      if (duree) suivre('projet-temps', { projet: fiche.dataset['projet'] ?? '', duree: tranche(duree) });
    });
  });
}
