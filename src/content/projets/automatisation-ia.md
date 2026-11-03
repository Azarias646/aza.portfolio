---
titre: Automatisation IA
categorie: Personnel
resume: >-
  Une équipe d’agents de développement autonomes pilotée depuis Discord, et un workflow qui repère les offres
  d’emploi publiées dans des groupes WhatsApp.
outils: [Hermes Agent, Claude Code, n8n, Python, Discord]
ordre: 5
schema:
  noeuds:
    - { texte: Discord, x: 14, y: 26, largeur: 80, hauteur: 30 }
    - { texte: Agents, x: 126, y: 20, largeur: 92, hauteur: 42, principal: true }
    - { texte: Code, x: 250, y: 26, largeur: 96, hauteur: 30 }
    - { texte: WhatsApp, x: 14, y: 112, largeur: 80, hauteur: 30 }
    - { texte: n8n, x: 126, y: 112, largeur: 92, hauteur: 30 }
    - { texte: Offres, x: 250, y: 112, largeur: 96, hauteur: 30 }
  liens:
    - { trace: 'M94 41 H126', principal: true }
    - { trace: 'M218 41 H250', principal: true }
    - { trace: 'M94 127 H126' }
    - { trace: 'M218 127 H250' }
---

<!-- Étude de cas (à rédiger, étape 4 du plan) : contexte, problème, architecture, ce que j'ai fait, résultats. -->
