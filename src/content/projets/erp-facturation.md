---
titre: ERP de facturation et comptabilité
categorie: Professionnel
resume: >-
  Un ERP partagé par plusieurs filiales : facturation, comptabilité par société, formats de documents,
  rapports et tableau de bord comptable. Chaque modification est d’abord testée sur une copie de la production.
outils: [Django, PostgreSQL, Docker, Jinja]
ordre: 1
schema:
  noeuds:
    - { texte: Filiale A, x: 16, y: 18, largeur: 92, hauteur: 30 }
    - { texte: Filiale B, x: 16, y: 70, largeur: 92, hauteur: 30 }
    - { texte: Filiale C, x: 16, y: 122, largeur: 92, hauteur: 30 }
    - { texte: ERP, x: 156, y: 64, largeur: 72, hauteur: 42, principal: true }
    - { texte: Factures, x: 262, y: 24, largeur: 84, hauteur: 32 }
    - { texte: Comptabilité, x: 262, y: 114, largeur: 84, hauteur: 32 }
  liens:
    - { trace: 'M108 33 C140 33 140 85 156 85' }
    - { trace: 'M108 85 H156' }
    - { trace: 'M108 137 C140 137 140 85 156 85' }
    - { trace: 'M228 78 C246 78 246 40 262 40', principal: true }
    - { trace: 'M228 92 C246 92 246 130 262 130', principal: true }
---

<!-- Étude de cas (à rédiger, étape 4 du plan) : contexte, problème, architecture, ce que j'ai fait, résultats. -->
