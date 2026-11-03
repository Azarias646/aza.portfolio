/**
 * Analytics (PLAN.md § 5 bis). Umami compte seul les pages vues et les clics sur les éléments
 * qui portent `data-umami-event` ; ce module envoie les événements calculés (sections, durées, thème).
 * Si Umami n'est pas chargé (développement, bloqueur de pubs), les appels ne font rien.
 */
type Donnees = Record<string, string | number>;

declare global {
  interface Window {
    umami?: { track: (evenement: string, donnees?: Donnees) => void };
  }
}

export function suivre(evenement: string, donnees?: Donnees): void {
  try {
    window.umami?.track(evenement, donnees);
  } catch {
    // La mesure ne doit jamais casser le site.
  }
}

/** Range une durée en tranches lisibles dans les rapports. */
export function tranche(ms: number): string {
  const s = ms / 1000;
  if (s < 5) return '< 5 s';
  if (s < 15) return '5–15 s';
  if (s < 60) return '15–60 s';
  return '> 60 s';
}

/**
 * Suit le temps passé sur un élément (section, fiche) : `debut` puis `fin`.
 * Le compteur se met en pause quand l'onglet est caché.
 */
export function chrono() {
  let depuis = 0;
  let cumul = 0;
  let actif = false;
  const pause = () => {
    if (actif && depuis) cumul += performance.now() - depuis;
    depuis = 0;
  };
  const reprise = () => {
    if (actif) depuis = performance.now();
  };
  document.addEventListener('visibilitychange', () => (document.hidden ? pause() : reprise()));
  return {
    debut() {
      actif = true;
      cumul = 0;
      depuis = performance.now();
    },
    /** Arrête et renvoie la durée en ms (0 si le chrono ne tournait pas). */
    fin(): number {
      if (!actif) return 0;
      pause();
      actif = false;
      return cumul;
    },
  };
}
