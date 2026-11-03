---
titre: Lakehouse
categorie: Ingénierie des données
resume: >-
  Un socle de données commun à plusieurs chantiers : décodage du protocole binaire de boîtiers GPS, ingestion
  orchestrée par Airflow, nettoyage avec Spark de fichiers PDF, images, CSV, JSON et Excel.
outils: [MinIO, Spark, Airflow, PySpark]
ordre: 2
schema:
  noeuds:
    - { texte: GPS, x: 12, y: 22, largeur: 74, hauteur: 28 }
    - { texte: Fichiers, x: 12, y: 70, largeur: 74, hauteur: 28 }
    - { texte: API, x: 12, y: 118, largeur: 74, hauteur: 28 }
    - { texte: Airflow, x: 118, y: 68, largeur: 70, hauteur: 32 }
    - { texte: MinIO, x: 206, y: 62, largeur: 70, hauteur: 44, principal: true }
    - { texte: Spark, x: 290, y: 40, largeur: 58, hauteur: 28 }
    - { texte: Tables, x: 290, y: 100, largeur: 58, hauteur: 28 }
  liens:
    - { trace: 'M86 36 C104 36 104 84 118 84' }
    - { trace: 'M86 84 H118' }
    - { trace: 'M86 132 C104 132 104 84 118 84' }
    - { trace: 'M188 84 H206' }
    - { trace: 'M276 84 H290', principal: true }
    - { trace: 'M319 68 V100' }
---

<!-- Étude de cas (à rédiger, étape 4 du plan) : contexte, problème, architecture, ce que j'ai fait, résultats. -->
