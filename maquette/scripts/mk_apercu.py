import os
MAQ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APERCU = os.environ.get("APERCU", os.path.join(MAQ, "apercu"))
os.makedirs(APERCU, exist_ok=True)
import re
s=open(os.path.join(MAQ, 'index.html')).read()
s=re.sub(r'<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport"[^>]*>\n','',s)
s=s.replace('<title>Azarias Sawadogo</title>','<title>Portfolio Azarias Sawadogo</title>\n<meta name="claude:viewport-fit-sides" content="cover">')
s=s.replace('</style>\n</head>\n<body>','</style>').replace('</body>\n</html>\n','')
s=s.replace('  nav { position: sticky;','  body::before { content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 10; background: var(--page); }\n  nav { position: sticky;')
s=s.replace('../src/assets/azarias.jpg','azarias.jpg').replace('../public/CV-Azarias-Sawadogo-2026.pdf','cv.pdf')
assert '<head>' not in s and 'azarias.jpg' in s
open(os.path.join(APERCU, 'portfolio-v2.html'),'w').write(s)
print('ok')
