/** Le portrait s'incline doucement vers le pointeur (14° / 10° au plus). Souris uniquement. */
export function initPortrait(reduit: boolean): void {
  const portrait = document.getElementById('portrait');
  if (!portrait || reduit || !matchMedia('(pointer: fine)').matches) return;
  let image = 0;
  addEventListener('pointermove', (e) => {
    cancelAnimationFrame(image);
    image = requestAnimationFrame(() => {
      const r = portrait.getBoundingClientRect();
      const x = Math.max(-1, Math.min(1, (e.clientX - (r.left + r.width / 2)) / (innerWidth / 2)));
      const y = Math.max(-1, Math.min(1, (e.clientY - (r.top + r.height / 2)) / (innerHeight / 2)));
      portrait.style.transform = `rotateY(${x * 14}deg) rotateX(${-y * 10}deg)`;
    });
  });
}
