# -*- coding: utf-8 -*-
import os
ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://lisbonprinthouse.com"

pages = []
for dirpath, dirnames, filenames in os.walk(ROOT):
  dirnames[:] = [d for d in dirnames if d not in (".git",)]
  for f in filenames:
    if f.endswith(".html"):
      full = os.path.join(dirpath, f)
      rel = os.path.relpath(full, ROOT).replace("\\", "/")
      pages.append(rel)

pages.sort()
urls = "".join(f"  <url><loc>{SITE}/{p}</loc></url>\n" for p in pages)
xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}</urlset>
"""
with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
  f.write(xml)
print(f"Sitemap written with {len(pages)} URLs.")
