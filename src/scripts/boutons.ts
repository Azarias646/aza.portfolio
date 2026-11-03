/** Boutons : le fond se remplit depuis le côté par lequel entre le curseur, et repart par celui où il sort. */
export function initBoutons(): void {
  document.querySelectorAll<HTMLElement>('.btn').forEach((b) => {
    const cote = (e: PointerEvent) => {
      const r = b.getBoundingClientRect();
      return e.clientX < r.left + r.width / 2 ? -1 : 1;
    };
    b.addEventListener('pointerenter', (e) => {
      if (e.pointerType === 'touch') return;
      b.classList.add('sans-transition');
      b.style.setProperty('--bx', `${cote(e) * 101}%`);
      void b.offsetWidth; // applique la position de départ avant de lancer la transition
      b.classList.remove('sans-transition');
      b.style.setProperty('--bx', '0%');
      b.classList.add('rempli');
    });
    b.addEventListener('pointerleave', (e) => {
      if (e.pointerType === 'touch') return;
      b.style.setProperty('--bx', `${cote(e) * 101}%`);
      b.classList.remove('rempli');
    });
  });
}
