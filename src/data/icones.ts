/** Icônes bicolores (viewBox 0 0 24 24) : classes `clair` et `moyen` pour les tons (voir `.ico` dans global.css). */
export const icones = {
  accueil:
    '<path d="M3 11.2 12 3.5l9 7.7V20a1.5 1.5 0 0 1-1.5 1.5H4.5A1.5 1.5 0 0 1 3 20z"/><path class="clair" d="M9.5 21.5v-6.5h5v6.5z"/>',
  apropos:
    '<circle cx="12" cy="8" r="4.2" class="clair"/><path d="M4 20.5c0-4.2 3.6-7 8-7s8 2.8 8 7v.5H4z"/>',
  projets:
    '<path d="M12 2.5 3.5 7 12 11.5 20.5 7z" class="clair"/><path d="M3.5 8.3 11.3 12.5V21.5L3.5 17.2z"/><path d="M20.5 8.3 12.7 12.5V21.5L20.5 17.2z" class="moyen"/>',
  parcours: '<path d="M5 2.5h1.8v19H5z"/><path d="M6.8 3.5h11.7l-2.6 4.2 2.6 4.3H6.8z" class="clair"/>',
  contact:
    '<path d="M3 5.5A2.5 2.5 0 0 1 5.5 3h13A2.5 2.5 0 0 1 21 5.5v9a2.5 2.5 0 0 1-2.5 2.5H10l-4.5 4v-4h0A2.5 2.5 0 0 1 3 14.5z" class="clair"/><circle cx="8.5" cy="10" r="1.3"/><circle cx="12" cy="10" r="1.3"/><circle cx="15.5" cy="10" r="1.3"/>',
} as const;

export type NomIcone = keyof typeof icones;
