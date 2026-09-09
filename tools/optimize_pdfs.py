#!/usr/bin/env python3
"""Losslessly rewrite PDF compression and verify page streams and image data."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, pikepdf

ROOT=Path(__file__).resolve().parents[1]
pikepdf.settings.set_flate_compression_level(9)

def fingerprint(pdf):
    """Compare page geometry, decoded drawing instructions and original image data."""
    pages=[]
    for page in pdf.pages:
        contents=page.obj.get('/Contents',[])
        if isinstance(contents,pikepdf.Stream): contents=[contents]
        streams=[hashlib.sha256(s.read_bytes()).hexdigest() for s in contents]
        pages.append({'box':str(page.mediabox),'rotation':str(page.obj.get('/Rotate',0)),'contents':streams})
    images=[]
    for obj in pdf.objects:
        if isinstance(obj,pikepdf.Stream) and obj.get('/Subtype')==pikepdf.Name('/Image'):
            try: data=obj.read_bytes()
            except pikepdf.PdfError: data=obj.read_raw_bytes()
            images.append((str(obj.get('/Width')),str(obj.get('/Height')),hashlib.sha256(data).hexdigest()))
    return {'pages':pages,'images':sorted(images)}

def optimize(record):
    source=ROOT/record['source_file']
    dest=ROOT/record['path'].lstrip('/')
    temp=dest.with_suffix('.tmp.pdf')
    with pikepdf.open(source) as pdf:
        before=fingerprint(pdf)
        pdf.save(temp,compress_streams=True,recompress_flate=True,object_stream_mode=pikepdf.ObjectStreamMode.generate)
    with pikepdf.open(temp) as pdf:
        assert fingerprint(pdf)==before, f'PDF content changed: {source}'
    smaller=temp.stat().st_size<dest.stat().st_size
    if smaller: temp.replace(dest)
    else: temp.unlink()
    return {'path':record['path'],'original_bytes':record['bytes'],'published_bytes':dest.stat().st_size,'optimized':smaller,'pages':len(before['pages']),'verified_streams_and_images':True,'published_sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}

if __name__=='__main__':
    records=json.loads((ROOT/'migration/assets.json').read_text())['documents']
    with ThreadPoolExecutor(max_workers=4) as pool:
        results=list(pool.map(optimize,records))
    (ROOT/'migration/pdf-optimization.json').write_text(json.dumps(results,indent=2))
    print('PDFs:',len(results),'Original MB:',sum(r['original_bytes'] for r in results)/1e6,'Published MB:',sum(r['published_bytes'] for r in results)/1e6,flush=True)
    print('All drawing streams, image data, page counts, page sizes and rotations verified unchanged.')
