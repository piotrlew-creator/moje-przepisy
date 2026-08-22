#!/usr/bin/env python3
"""NIEUŻYWANE — zastąpione przez generate_site.py.

Stary generator trzymał gotowy HTML każdego przepisu wklejony jako string
i nie tworzył strony głównej, przez co lista dań rozjechała się z przepisami.
Dane przeniesiono do recipes.json.

Plik można bezpiecznie usunąć:  git rm generate_recipes.py
"""
import sys

print(__doc__)
print("Uruchom zamiast tego:  python generate_site.py")
sys.exit(1)
