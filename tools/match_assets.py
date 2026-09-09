#!/usr/bin/env python3
"""Match public PDF bytes to the original Wix download; retain stable URLs."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.parse import urlparse
from collections import defaultdict
import hashlib, json, shutil, time

ROOT = Path(__file__).resolve().parents[1]
CACHE = Path('/private/tmp/leonroth-public-pdfs')
CACHE.mkdir(exist_ok=True)
pages = json.loads((ROOT/'migration/pages.json').read_text())
local = {}
for p in (ROOT/'Site Files').rglob('*'):
    if p.is_file() and p.suffix.lower() == '.pdf':
        local[hashlib.sha256(p.read_bytes()).hexdigest()] = p
refs = defaultdict(list)
for p in pages:
    for a in p['links']:
        if '/_files/ugd/' in a['href']:
            refs[a['href']].append({'page':p['slug'],'label':a['text']})

def match(url):
    path = CACHE / Path(urlparse(url).path).name
    if not path.exists():
        for attempt in range(3):
            try:
                with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=120) as r:
                    data = r.read()
                if not data.startswith(b'%PDF'): raise ValueError('Not a PDF')
                path.write_bytes(data)
                break
            except Exception:
                if attempt == 2: raise
                time.sleep(1)
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    original = local.get(digest)
    destination = ROOT / urlparse(url).path.lstrip('/')
    destination.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(original or path,destination)
    return {'url':url,'path':'/'+str(destination.relative_to(ROOT)), 'source_file':str(original.relative_to(ROOT)) if original else None,'sha256':digest,'bytes':path.stat().st_size,'references':refs[url]}

results, failures = [], []
with ThreadPoolExecutor(max_workers=8) as pool:
    jobs = {pool.submit(match,u):u for u in refs}
    for f in as_completed(jobs):
        try: results.append(f.result())
        except Exception as e: failures.append({'url':jobs[f],'error':str(e)})
        if (len(results)+len(failures))%25 == 0: print('Matched',len(results),'of',len(refs),flush=True)
results.sort(key=lambda r:r['path'])
report={'documents':results,'failures':failures,'unused_files':sorted(str(p.relative_to(ROOT)) for p in local.values() if str(p.relative_to(ROOT)) not in {r['source_file'] for r in results})}
(ROOT/'migration/assets.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print('Documents:',len(results),'Matched originals:',sum(bool(r['source_file']) for r in results),'MB:',sum(r['bytes'] for r in results)/1e6)
print('Unmatched:',[r for r in results if not r['source_file']])
print('Failures:',failures)
