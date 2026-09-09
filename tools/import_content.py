#!/usr/bin/env python3
"""One-time Wix rich-text import. Edit the resulting Markdown pages thereafter."""
from pathlib import Path
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from markdownify import markdownify
import json, re, shutil, yaml

ROOT = Path(__file__).resolve().parents[1]
pages = json.loads((ROOT/'migration/pages.json').read_text())
BOOKS = {'in-memoriam-ahad-ha-am','the-guide-for-the-perplexed','education-and-human-values','god-and-man-in-the-old-testament','shiv-a-prakim-al-angliya','judaism','descartes'}
BIBLIOGRAPHIES = {'books-by-leon-roth','essays-english','essays-hebrew','works-about-leon-roth'}
images = {'Leon Roth.png':'leon-roth.png','Leon Roth conference.jpg':'philosophy-congress-1956.jpg','Leon Roth ex libris.png':'leon-roth-ex-libris.png'}
(ROOT/'assets/images').mkdir(parents=True,exist_ok=True)
for old,new in images.items(): shutil.copyfile(ROOT/'Site Files'/old,ROOT/'assets/images'/new)

def clean(block):
    soup = BeautifulSoup(block.replace('\u200b','').replace('\xa0',' '),'html.parser')
    for span in soup.select('span'):
        style=span.get('style','')
        if 'font-style:italic' in style: span.name='em'
        elif 'font-weight:bold' in style or 'font-weight:700' in style: span.name='strong'
        else: span.unwrap()
    for a in list(soup.select('a')):
        if not a.get_text(strip=True): a.decompose()
    for p in list(soup.select('p')):
        if not p.get_text(strip=True): p.decompose()
    for h in soup.select('h1,h2,h3,h4,h5,h6'): h.name='h2'
    links={}
    for i,a in enumerate(soup.select('a[href]')):
        u=urlparse(a['href'])
        if u.netloc in ('www.leonroth.org','leonroth.org'):
            path=u.path or '/'
            if not Path(path).suffix: path=path.rstrip('/')+'/'
            token=f'MIGRATIONLINK{i}END'
            links[token]="{{ '"+path+"' | relative_url }}"
            a['href']=token
    for el in soup.find_all(): el.attrs={k:v for k,v in el.attrs.items() if k in ('href','lang','dir')}
    result=markdownify(str(soup),heading_style='ATX',bullets='-',escape_underscores=False).strip()
    for token,url in links.items(): result=result.replace(token,url)
    return re.sub(r'\n{3,}','\n\n',result)

for page in pages:
    slug=page['slug']
    if slug=='index': continue
    blocks=page['blocks']
    title_index=1 if slug=='resources' else 0
    title=BeautifulSoup(blocks[title_index],'html.parser').get_text(' ',strip=True)
    title=title.replace('\u200b','').strip()
    meta={'title':title,'permalink':'/'+slug+'/'}
    if slug in BOOKS:
        meta.update(collection_label='Books by Leon Roth',parent_url='/books-by-leon-roth/',back_label='Back to books by Leon Roth',page_class='book-page')
    elif slug in BIBLIOGRAPHIES:
        meta.update(collection_label='Resource library',parent_url='/resources/',page_class='bibliography-page')
    elif slug in ('about-us','academic-advisory-board'):
        meta['collection_label']='The Foundation'
    elif slug=='leon-roth': meta.update(collection_label='Life & thought',page_class='biography-page')
    elif slug=='2017-conference': meta['collection_label']='University of Toronto · May 15–17, 2017'
    caption_index=0 if slug=='resources' else 2 if slug in ('about-us','academic-advisory-board') else None
    body='\n\n'.join(clean(b) for i,b in enumerate(blocks) if i not in (title_index,caption_index))
    if page['images']:
        name=images[page['images'][0]['title']]
        caption=BeautifulSoup(blocks[caption_index],'html.parser').get_text(' ',strip=True) if caption_index is not None else 'Leon Roth, 1896–1963'
        alt={'leon-roth.png':'Portrait of Leon Roth','philosophy-congress-1956.jpg':'Delegates at the 1956 Philosophy Congress at Annamalai University','leon-roth-ex-libris.png':'Leon Roth’s ex libris, featuring Spinoza and Maimonides'}[name]
        from PIL import Image
        w,h=Image.open(ROOT/'assets/images'/name).size
        body='<figure class="archive-photo">\n  <img src="{{ \'/assets/images/'+name+'\' | relative_url }}" alt="'+alt+'" width="'+str(w)+'" height="'+str(h)+'">\n  <figcaption>'+caption+'</figcaption>\n</figure>\n\n'+body
    (ROOT/(slug+'.md')).write_text('---\n'+yaml.safe_dump(meta,allow_unicode=True,sort_keys=False,width=140)+'---\n\n'+body+'\n')
    print('Imported',slug)
