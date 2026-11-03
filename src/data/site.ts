/** Informations générales du site, utilisées par la mise en page, le SEO et les composants. */
export const site = {
  nom: 'Azarias Sawadogo',
  prenom: 'Azarias',
  roles: ['Développeur systèmes et bases de données', 'Data engineer junior'],
  description:
    'Portfolio d’Azarias Sawadogo, développeur systèmes et bases de données et data engineer junior : ERP, lakehouse, homelab et automatisation.',
  langue: 'fr',
  email: 'azasawpro@gmail.com',
  cv: '/CV-Azarias-Sawadogo-2026.pdf',
  reseaux: [
    { nom: 'LinkedIn', url: 'https://www.linkedin.com/in/azarias-sawadogo-90345a2a2/' },
    { nom: 'GitHub', url: 'https://github.com/Azarias646' },
    { nom: 'WhatsApp', url: 'https://wa.me/22655194949' },
  ],
} as const;

/** Écrans du site, dans l'ordre. `nom` est affiché dans les repères et la barre d'onglets mobile. */
export const ecrans = [
  { id: 'accueil', nom: 'Moi' },
  { id: 'apropos', nom: 'À propos' },
  { id: 'projets', nom: 'Projets' },
  { id: 'parcours', nom: 'Parcours' },
  { id: 'contact', nom: 'Contact' },
] as const;

export type IdEcran = (typeof ecrans)[number]['id'];
