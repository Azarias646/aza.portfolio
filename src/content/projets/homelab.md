---
titre: Homelab
categorie: Personnel
resume: >-
  Mon infrastructure auto-hébergée : supervision des machines, accès distant sécurisé et reverse proxy pour
  publier les services.
outils: [Docker, Tailscale, Caddy, Linux]
ordre: 3
schema:
  noeuds:
    - { texte: Serveur, x: 130, y: 62, largeur: 100, hauteur: 46, principal: true }
    - { texte: Supervision, x: 14, y: 20, largeur: 82, hauteur: 28 }
    - { texte: Sauvegardes, x: 14, y: 122, largeur: 82, hauteur: 28 }
    - { texte: Proxy, x: 264, y: 20, largeur: 82, hauteur: 28 }
    - { texte: Services, x: 264, y: 122, largeur: 82, hauteur: 28 }
  liens:
    - { trace: 'M96 34 C116 34 116 74 130 74' }
    - { trace: 'M96 136 C116 136 116 96 130 96' }
    - { trace: 'M230 74 C246 74 246 34 264 34', principal: true }
    - { trace: 'M230 96 C246 96 246 136 264 136' }
    - { trace: 'M180 62 V16 M150 16 H210', pointille: true }
  etiquettes:
    - { texte: Accès distant, x: 180, y: 12 }
---

<!-- Étude de cas (à rédiger, étape 4 du plan) : contexte, problème, architecture, ce que j'ai fait, résultats. -->
