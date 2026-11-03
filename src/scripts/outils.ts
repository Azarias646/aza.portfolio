/**
 * Fiche d'un outil (« À propos ») : une seule <dialog>, remplie à partir du bouton cliqué
 * (nom, description, niveau, logo). La jauge et l'aiguille s'animent à l'ouverture.
 */
const LONGUEUR_ARC = 277;

export function initOutils(reduit: boolean): void {
  const fiche = document.getElementById('fiche-outil');
  if (!(fiche instanceof HTMLDialogElement)) return;
  const champ = (nom: string) => fiche.querySelector<HTMLElement>(`[data-${nom}]`);
  const logo = champ('fiche-logo');
  const nom = champ('fiche-nom');
  const texte = champ('fiche-texte');
  const niveau = champ('fiche-niveau');
  const valeur = fiche.querySelector<SVGPathElement>('[data-jauge-valeur]');
  const aiguille = fiche.querySelector<SVGLineElement>('[data-jauge-aiguille]');
  if (!logo || !nom || !texte || !niveau || !valeur || !aiguille) return;

  const regler = (part: number, anime: boolean) => {
    valeur.style.transition = aiguille.style.transition = anime ? '' : 'none';
    valeur.style.strokeDashoffset = String(LONGUEUR_ARC * (1 - part));
    aiguille.style.transform = `rotate(${-90 + 180 * part}deg)`;
  };

  document.querySelectorAll<HTMLButtonElement>('[data-outil]').forEach((bouton) => {
    bouton.addEventListener('click', () => {
      const { outil = '', description = '', libelle = '' } = bouton.dataset;
      const part = Number(bouton.dataset['niveau'] ?? 0) / 3;
      nom.textContent = outil;
      texte.textContent = description;
      niveau.textContent = libelle;
      const svg = bouton.querySelector('svg');
      logo.replaceChildren(...(svg ? [svg.cloneNode(true)] : []));
      regler(0, false);
      fiche.showModal();
      if (reduit) regler(part, false);
      else requestAnimationFrame(() => requestAnimationFrame(() => regler(part, true)));
    });
  });
  fiche.querySelector('[data-fermer]')?.addEventListener('click', () => fiche.close());
  fiche.addEventListener('click', (e) => {
    if (e.target === fiche) fiche.close();
  });
}
