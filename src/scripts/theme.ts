/**
 * Bouton de thème : automatique → sombre → clair. Le choix est gardé dans le navigateur.
 * Le thème est appliqué avant l'affichage par le petit script en ligne de Base.astro.
 */
import { suivre } from './analytics';

const modes = ['auto', 'dark', 'light'] as const;
type Mode = (typeof modes)[number];
const noms: Record<Mode, string> = { auto: 'automatique', dark: 'sombre', light: 'clair' };

export function initTheme(): void {
  const bouton = document.getElementById('theme');
  if (!bouton) return;
  const racine = document.documentElement;
  const lire = (): Mode => {
    const t = racine.dataset['theme'];
    return t === 'dark' || t === 'light' ? t : 'auto';
  };
  const libeller = (mode: Mode) => {
    bouton.setAttribute('aria-label', `Thème : ${noms[mode]}`);
    bouton.title = `Thème : ${noms[mode]}`;
  };
  libeller(lire());
  bouton.addEventListener('click', () => {
    const mode = modes[(modes.indexOf(lire()) + 1) % modes.length] ?? 'auto';
    if (mode === 'auto') delete racine.dataset['theme'];
    else racine.dataset['theme'] = mode;
    try {
      localStorage.setItem('theme', mode);
    } catch {
      // Stockage indisponible (navigation privée) : le choix vaut pour la page en cours.
    }
    libeller(mode);
    suivre('theme-changement', { theme: noms[mode] });
  });
}
