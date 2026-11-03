/**
 * Navigation par écrans (§ 4.1 à 4.3 de maquette/COMPOSANTS.md).
 * Ordinateur : un écran à la fois ; molette, glissement, clavier, liens et reperes changent d'écran
 * par une poussée verticale, puis le contenu apparaît en fondu (retrait de `.attente`).
 * Téléphone (760 px et moins) : défilement normal, fondu à l'entrée de chaque section.
 */
import { chrono, suivre, tranche } from './analytics';

const DUREE = 560;
const COURBE = 'cubic-bezier(.65, 0, .35, 1)';
const SEUIL_MOLETTE = 24;
const SEUIL_DOIGT = 60;

export function initEcrans(reduit: boolean): void {
  const racine = document.documentElement;
  const ecrans = [...document.querySelectorAll<HTMLElement>('.ecran')];
  if (!ecrans.length) return;
  const reperes = [...document.querySelectorAll<HTMLButtonElement>('.points [data-ecran]')];
  const liensNav = [...document.querySelectorAll<HTMLAnchorElement>('.barre .liens a')];
  const mobile = matchMedia('(max-width: 760px)');
  mobile.addEventListener('change', () => location.reload());

  racine.classList.add('anime');
  let courant = 0;
  let verrou = false;

  // Analytics : chaque section vue une fois, et temps passé sur chaque section
  const vues = new Set<string>();
  const temps = chrono();
  const entrerSection = (i: number) => {
    const id = ecrans[i]?.id ?? '';
    if (!vues.has(id)) {
      vues.add(id);
      suivre('section-vue', { section: id });
    }
    temps.debut();
  };
  const quitterSection = (i: number) => {
    const duree = temps.fin();
    if (duree) suivre('section-temps', { section: ecrans[i]?.id ?? '', duree: tranche(duree) });
  };

  const marquer = () => {
    const id = ecrans[courant]?.id ?? '';
    reperes.forEach((b) => b.setAttribute('aria-current', String(b.dataset['ecran'] === id)));
    liensNav.forEach((a) => {
      const actif = a.hash === `#${id}`;
      a.classList.toggle('active', actif);
      if (actif) a.setAttribute('aria-current', 'location');
      else a.removeAttribute('aria-current');
    });
    try {
      history.replaceState(null, '', `#${id}`);
    } catch {
      // Adresse non modifiable (aperçu dans une iframe) : sans effet sur la navigation.
    }
  };

  const aller = (cible: number, instantane = false) => {
    const apres = ecrans[cible];
    if (!apres) return;
    if (mobile.matches) {
      apres.classList.remove('attente');
      apres.scrollIntoView({ behavior: reduit || instantane ? 'auto' : 'smooth', block: 'start' });
      return;
    }
    const avant = ecrans[courant];
    if (verrou || cible === courant || !avant) return;
    const sens = cible > courant ? 1 : -1;
    quitterSection(courant);
    courant = cible;
    marquer();
    entrerSection(courant);
    apres.scrollTop = sens > 0 ? 0 : apres.scrollHeight;
    apres.classList.add('attente');
    if (reduit || instantane) {
      avant.classList.remove('active');
      apres.classList.add('active');
      apres.classList.remove('attente');
      return;
    }
    verrou = true;
    apres.classList.add('entree');
    avant.animate([{ transform: 'translateY(0)' }, { transform: `translateY(${-100 * sens}%)` }], {
      duration: DUREE,
      easing: COURBE,
    });
    apres.animate([{ transform: `translateY(${100 * sens}%)` }, { transform: 'translateY(0)' }], {
      duration: DUREE,
      easing: COURBE,
    }).onfinish = () => {
      avant.classList.remove('active');
      avant.classList.add('attente');
      apres.classList.remove('entree');
      apres.classList.add('active');
      setTimeout(() => (verrou = false), 60);
    };
    setTimeout(() => apres.classList.remove('attente'), DUREE * 0.4);
  };

  const indexDe = (hash: string) => ecrans.findIndex((e) => `#${e.id}` === hash);

  // État de départ
  ecrans.forEach((e, i) => e.classList.toggle('attente', i > 0));
  ecrans[0]?.classList.add('active');
  const depart = indexDe(location.hash);
  if (depart > 0 && !mobile.matches) aller(depart, true);
  else {
    marquer();
    entrerSection(0);
  }

  if (mobile.matches) {
    ecrans.forEach((e) => e.classList.add('active'));
    const apparition = new IntersectionObserver(
      (entrees) =>
        entrees.forEach((e) => {
          if (!e.isIntersecting) return;
          e.target.classList.remove('attente');
          apparition.unobserve(e.target);
        }),
      { threshold: 0.12 },
    );
    const suivi = new IntersectionObserver(
      (entrees) =>
        entrees.forEach((e) => {
          const i = ecrans.indexOf(e.target as HTMLElement);
          if (!e.isIntersecting || i === courant) return;
          quitterSection(courant);
          courant = i;
          marquer();
          entrerSection(courant);
        }),
      { rootMargin: '-45% 0px -50% 0px' },
    );
    ecrans.forEach((e) => {
      apparition.observe(e);
      suivi.observe(e);
    });
    if (depart > 0) aller(depart, true);
  }

  addEventListener('hashchange', () => {
    const i = indexDe(location.hash);
    if (i >= 0) aller(i);
  });
  addEventListener('pagehide', () => quitterSection(courant));

  // Liens internes (menu, marque, boutons) et reperes
  document.querySelectorAll<HTMLAnchorElement>('a[href^="#"]').forEach((a) => {
    const i = indexDe(a.hash);
    if (i >= 0)
      a.addEventListener('click', (e) => {
        e.preventDefault();
        aller(i);
      });
  });
  reperes.forEach((b) => {
    const i = ecrans.findIndex((e) => e.id === b.dataset['ecran']);
    b.addEventListener('click', () => aller(i));
  });

  if (mobile.matches) return; // le reste ne sert qu'à la navigation plein écran

  const dialogueOuvert = () => document.querySelector('dialog[open]') !== null;
  const auBord = (e: HTMLElement, sens: number) =>
    sens > 0 ? e.scrollTop + e.clientHeight >= e.scrollHeight - 2 : e.scrollTop <= 1;

  // Molette : défile d'abord le contenu de l'écran, puis change d'écran une fois au bord
  let cumul = 0;
  let dernierDefilement = 0;
  ecrans.forEach((e) =>
    e.addEventListener('scroll', () => (dernierDefilement = performance.now()), { passive: true }),
  );
  addEventListener(
    'wheel',
    (e) => {
      if (dialogueOuvert()) return;
      const ecran = ecrans[courant];
      const sens = Math.sign(e.deltaY);
      if (!ecran || !sens) return;
      if (verrou) return e.preventDefault();
      if (!auBord(ecran, sens)) {
        cumul = 0;
        return;
      }
      e.preventDefault();
      if (performance.now() - dernierDefilement < 220) return;
      cumul += e.deltaY;
      if (Math.abs(cumul) > SEUIL_MOLETTE) {
        cumul = 0;
        aller(courant + sens);
      }
    },
    { passive: false },
  );

  // Glissement du doigt (tablette en grand format)
  let y0: number | null = null;
  addEventListener('touchstart', (e) => (y0 = e.touches[0]?.clientY ?? null), { passive: true });
  addEventListener(
    'touchend',
    (e) => {
      const y1 = e.changedTouches[0]?.clientY;
      const ecran = ecrans[courant];
      if (y0 === null || y1 === undefined || !ecran || dialogueOuvert()) return;
      const dy = y0 - y1;
      const sens = Math.sign(dy);
      y0 = null;
      if (Math.abs(dy) > SEUIL_DOIGT && auBord(ecran, sens)) aller(courant + sens);
    },
    { passive: true },
  );

  // Clavier
  addEventListener('keydown', (e) => {
    const actif = document.activeElement;
    if (
      dialogueOuvert() ||
      (e.key === ' ' && actif instanceof HTMLElement && actif.matches('input, textarea, button'))
    )
      return;
    const ecran = ecrans[courant];
    if (!ecran) return;
    const suivant = ['ArrowDown', 'PageDown', ' '].includes(e.key);
    const precedent = ['ArrowUp', 'PageUp'].includes(e.key);
    if ((suivant && auBord(ecran, 1)) || (precedent && auBord(ecran, -1))) {
      e.preventDefault();
      aller(courant + (suivant ? 1 : -1));
    } else if (e.key === 'Home') {
      e.preventDefault();
      aller(0);
    } else if (e.key === 'End') {
      e.preventDefault();
      aller(ecrans.length - 1);
    }
  });
}
