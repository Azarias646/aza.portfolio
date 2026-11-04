"""
Prépare la police du site : Roboto Flex réduite à ce qui sert.
- axes gardés : opsz (taille optique), wdth (largeur), wght (graisse) ; slnt fixé à 0 (pas d'italique) ;
- caractères : latin de base, latin-1 (accents français) et la ponctuation typographique utilisée.
Source : @fontsource-variable/roboto-flex (licence SIL OFL). Sortie : public/polices/roboto-flex.woff2.
Usage : pip install fonttools brotli && python3 outils/police.py
"""
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

RACINE = Path(__file__).resolve().parent.parent
SOURCE = RACINE / 'node_modules/@fontsource-variable/roboto-flex/files/roboto-flex-latin-standard-normal.woff2'
SORTIE = RACINE / 'public/polices/roboto-flex.woff2'
CARACTERES = 'U+0020-007E,U+00A0-00FF,U+0152-0153,U+2013-2014,U+2018-201E,U+2022,U+2026,U+202F,U+20AC,U+2192'

police = TTFont(SOURCE)
options = subset.Options()
options.flavor = 'woff2'
options.hinting = False  # les écrans actuels n'en ont pas besoin ; gros gain de poids
options.layout_features = ['kern', 'liga', 'calt', 'tnum', 'lnum', 'case']
options.name_IDs = ['*']
sous_ensemble = subset.Subsetter(options)
sous_ensemble.populate(unicodes=subset.parse_unicodes(CARACTERES))
sous_ensemble.subset(police)
police = instancer.instantiateVariableFont(police, {'slnt': 0})
SORTIE.parent.mkdir(parents=True, exist_ok=True)
police.flavor = 'woff2'
police.save(SORTIE)
print(f'{SORTIE.relative_to(RACINE)} : {SORTIE.stat().st_size // 1024} Ko, axes', [a.axisTag for a in police['fvar'].axes])
