#!/usr/bin/env python3
"""Capture the public Wix pages and inventory their content (migration only)."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'migration' / 'source'

def fetch(url):
    slug = urlparse(url).path.strip('/') or 'index'
    path = DEST / (slug + '.html')
    if not path.exists():
        with urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=90) as r:
            path.write_bytes(r.read())
    soup = BeautifulSoup(path.read_text(), 'html.parser')
    main = soup.find('main')
    blocks = [str(x) for x in main.select('[data-testid="richTextElement"]')]
    images = [{'src': x.get('src'), 'title': x.find_parent(class_='wixui-image').get('title', '') if x.find_parent(class_='wixui-image') else x.get('alt', '')} for x in main.select('img')]
    links = [{'text': a.get_text(' ',strip=True), 'href': a.get('href')} for a in main.select('a[href]')]
    return {'slug': slug, 'url': url, 'title': soup.title.get_text(), 'blocks': blocks, 'images': images, 'links': links}

urls = [e.text for e in ET.parse(DEST / 'pages-sitemap.xml').iter() if e.tag.endswith('loc')]
with ThreadPoolExecutor(max_workers=6) as pool:
    pages = list(pool.map(fetch, urls))
(ROOT/'migration'/'pages.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2))
for p in pages:
    print(p['slug'], len(p['blocks']), 'blocks,', len(p['links']), 'links, images:', [i['title'] for i in p['images']])
