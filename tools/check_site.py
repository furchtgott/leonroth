#!/usr/bin/env python3
"""Check the built site, all local links, preserved routes and Pages size limits."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import argparse, json, sys

class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.links=[];self.ids=set();self.h1=0;self.images=[];self.text=[]
    def handle_data(self,data):self.text.append(data)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.add(a['id'])
        if tag=='h1':self.h1+=1
        if tag=='img':self.images.append(a)
        for key in ('href','src'):
            if a.get(key):self.links.append(a[key])

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--site',default='_site')
    parser.add_argument('--baseurl',default='/leonroth')
    args=parser.parse_args();root=Path(args.site).resolve();base=args.baseurl.rstrip('/')
    errors=[];pages={};link_count=0
    for file in root.rglob('*.html'):
        page=Page();page.feed(file.read_text());pages[file]=page
        if '**' in ''.join(page.text):errors.append(f'{file.relative_to(root)}: unrendered Markdown emphasis')
        if page.h1!=1:errors.append(f'{file.relative_to(root)}: expected one h1, got {page.h1}')
        for img in page.images:
            if not img.get('alt'):errors.append(f'{file.relative_to(root)}: missing image alt')
    for file,page in pages.items():
        for href in page.links:
            url=urlsplit(href)
            if url.scheme or url.netloc:
                if 'wixstatic.com' in href or 'parastorage.com' in href:errors.append(f'Wix asset dependency: {href}')
                continue
            path=unquote(url.path)
            if not path:target=file
            elif path.startswith('/'):
                if base and not path.startswith(base+'/'):errors.append(f'Link missing baseurl: {href}');continue
                target=root/path[len(base):].lstrip('/')
            else:target=file.parent/path
            if target.is_dir():target=target/'index.html'
            elif not target.exists() and not target.suffix:target=target/'index.html'
            link_count+=1
            if not target.is_file():errors.append(f'{file.relative_to(root)}: broken {href}');continue
            if url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f'{file.relative_to(root)}: missing anchor {href}')
    source=json.loads(Path('migration/pages.json').read_text())
    for page in source:
        path=root/('index.html' if page['slug']=='index' else page['slug']+'/index.html')
        if not path.is_file():errors.append('Missing original route: '+page['slug'])
    assets=json.loads(Path('migration/assets.json').read_text())
    for doc in assets['documents']:
        path=root/doc['path'].lstrip('/')
        if not path.is_file() or path.read_bytes()[:4]!=b'%PDF':errors.append('Missing/invalid PDF: '+doc['path'])
    files=[p for p in root.rglob('*') if p.is_file()]
    total=sum(p.stat().st_size for p in files)
    if total>=1_000_000_000:errors.append(f'Published site exceeds conservative 1 GB limit: {total:,} bytes')
    for file in files:
        if file.stat().st_size>=100_000_000:errors.append('File exceeds GitHub limit: '+str(file))
    forbidden=['Site Files','migration','tools','vendor','Gemfile','Gemfile.lock','README.md','MIGRATION.md']
    for name in forbidden:
        if (root/name).exists():errors.append('Private/build input in published output: '+name)
    report={'html_pages':len(pages),'original_routes':len(source),'checked_local_links':link_count,'preserved_pdf_urls':len(assets['documents']),'published_bytes':total,'errors':errors}
    print(json.dumps(report,indent=2))
    if errors:sys.exit(1)

if __name__=='__main__':main()
