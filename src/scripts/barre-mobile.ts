/**
 * Téléphone : la barre d'onglets du bas se cache quand on descend et réapparaît dès qu'on remonte.
 * Elle reste visible en haut et en bas de la page, et quand un élément de la barre a le focus.
 */
const SEUIL = 8; // px de défilement avant de changer d'état

export function initBarreMobile(): void {
  const mobile = matchMedia('(max-width: 760px)');
  if (!mobile.matches) return;
  const racine = document.documentElement;
  const barre = document.querySelector('.barre .liens');
  let precedent = scrollY;
  let image = 0;
  const mettreAJour = () => {
    const y = scrollY;
    const ecart = y - precedent;
    const enBas = y + innerHeight >= document.documentElement.scrollHeight - 4;
    if (y < 80 || enBas || barre?.contains(document.activeElement)) racine.classList.remove('barre-cachee');
    else if (ecart > SEUIL) racine.classList.add('barre-cachee');
    else if (ecart < -SEUIL) racine.classList.remove('barre-cachee');
    if (Math.abs(ecart) > SEUIL) precedent = y;
  };
  addEventListener(
    'scroll',
    () => {
      cancelAnimationFrame(image);
      image = requestAnimationFrame(mettreAJour);
    },
    { passive: true },
  );
  barre?.addEventListener('focusin', () => racine.classList.remove('barre-cachee'));
}
