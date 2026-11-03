/** Copier l'adresse e-mail : coche verte pendant 1,8 s et message pour les lecteurs d'écran. */
export function initCopier(): void {
  const bouton = document.getElementById('copier');
  const adresse = document.getElementById('adresse');
  const statut = document.querySelector<HTMLElement>('[data-statut]');
  if (!bouton || !adresse) return;
  let minuterie = 0;
  const confirmer = () => {
    bouton.classList.add('copie');
    bouton.setAttribute('aria-label', 'Adresse copiée');
    bouton.title = 'Adresse copiée';
    if (statut) statut.textContent = 'Adresse copiée';
    clearTimeout(minuterie);
    minuterie = window.setTimeout(() => {
      bouton.classList.remove('copie');
      bouton.setAttribute('aria-label', 'Copier l’adresse');
      bouton.title = 'Copier l’adresse';
      if (statut) statut.textContent = '';
    }, 1800);
  };
  // Repli : sélectionner l'adresse pour une copie manuelle
  const selectionner = () => {
    const selection = getSelection();
    const plage = document.createRange();
    plage.selectNodeContents(adresse);
    selection?.removeAllRanges();
    selection?.addRange(plage);
  };
  bouton.addEventListener('click', () => {
    const texte = adresse.textContent?.trim() ?? '';
    if (navigator.clipboard) navigator.clipboard.writeText(texte).then(confirmer, selectionner);
    else selectionner();
  });
}
