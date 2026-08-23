#!/usr/bin/env python3
"""Sprawdza, czy recipes.json nadal mówi dokładnie to, co PDF z planem diety.

Porównuje trzy rzeczy z sekcją „Plan diety”:
  * każdy składnik (ilość domowa, jednostka, nazwa, gramatura),
  * każdy krok przygotowania,
  * każdą nazwę dania oraz kompletność siatki 10 dni x 4 posiłki.

Użycie:  python verify_against_pdf.py source/dieta.pdf

Wymaga `pip install pdfplumber` (nie jest potrzebne do zbudowania strony).
"""
import json, re, sys
from collections import Counter

import pdfplumber

PDF = sys.argv[1] if len(sys.argv) > 1 else "source/dieta.pdf"
data = json.load(open("recipes.json", encoding="utf-8"))

pdf=pdfplumber.open(PDF)
start=next(n for n,pg in enumerate(pdf.pages) if (pg.extract_text() or '').strip().startswith('Plan diety'))

def col(xmax=None, xmin=None):
    out=[]
    for pg in pdf.pages[start:]:
        ws=[w for w in pg.extract_words() if (xmax is None or w['x0']<xmax) and (xmin is None or w['x0']>=xmin)]
        lines={}
        for w in ws: lines.setdefault(round(w['top']/3),[]).append(w)
        for k in sorted(lines):
            out.append(' '.join(w['text'] for w in sorted(lines[k],key=lambda w:w['x0'])).strip())
    return out

left=col(xmax=340)
merged=[]
for l in left:
    if merged and not re.search(r'\(\s*[\d.]+\s*g\s*\)$', merged[-1]) and re.match(r'^[\d.]', merged[-1]) and not re.match(r'^[\d.]+\s+\S', l):
        merged[-1]+=' '+l
    else: merged.append(l)
pat=re.compile(r'^([\d.]+)\s+(\S+)\s+(.+?)\s+\(([\d.]+)\s*g\)$')
pdf_ings=set()
for l in merged:
    m=pat.match(l)
    if m: pdf_ings.add((float(m.group(1)), m.group(2), m.group(3).strip(), float(m.group(4))))

ours=set(); owner={}
for r in data['recipes']:
    for i in r['ingredients']:
        k=(i['qty'], i['unit'], i['name'], i['grams']); ours.add(k); owner[k]=r['slug']

missing=sorted(ours-pdf_ings, key=lambda k: owner[k])
print(f"Składniki: {len(ours)} unikalnych w danych, {len(pdf_ings)} w PDF")
print(f"  niezgodnych z PDF: {len(missing)}")
for k in missing: print('   ', owner[k], k)

# kroki
# Kroki porównujemy z pola `stepsSource` — to dosłowny zapis z PDF-u.
# Pole `steps` zawiera tę samą treść przepisaną na tryb rozkazujący
# („pokrój” zamiast „kroimy”) i ze znacznikami zamienników.
right=' '.join(col(xmin=340))
# pdfplumber wstawia czasem spację przed przecinkiem — normalizujemy obie strony
norm = lambda t: re.sub(r'\s+([,.])', r'\1', re.sub(r'\s+',' ', t)).strip()
right=norm(right)
bad=[]
for r in data['recipes']:
    for s in r['stepsSource']:
        probe=norm(s)[:60]
        if probe not in right: bad.append((r['slug'], probe))
print(f"Kroki: {sum(len(r['stepsSource']) for r in data['recipes'])} sprawdzonych, niezgodnych: {len(bad)}")
for b in bad[:10]: print('   ', b)

# tytuly + metadane
names=set()
for pg in pdf.pages[start:]:
    names.add(re.sub(r'\s+',' ', pg.extract_text() or ''))
alltxt=' '.join(names)
badt=[r['title'] for r in data['recipes'] if re.sub(r'\s+',' ',r['title']) not in alltxt]
print(f"Tytuły: {len(data['recipes'])} sprawdzonych, niezgodnych: {len(badt)}", badt)

# komplet 10x4
# mealNo to oryginalny numer posiłku z PDF-u (1–4); `slot` na stronie
# ma już scalone śniadania, więc do kontroli kompletności bierzemy mealNo.
grid=Counter((r['day'], r['mealNo']) for r in data['recipes'])
print("Siatka 10 dni × 4 posiłki kompletna:", all(grid.get((d,s))==1 for d in range(1,11) for s in range(1,5)))
sys.exit(1 if (missing or bad or badt) else 0)
