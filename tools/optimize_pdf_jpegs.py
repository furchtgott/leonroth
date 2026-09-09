#!/usr/bin/env python3
"""Optimize JPEG entropy coding inside PDFs without changing decoded pixels."""
from concurrent.futures import ThreadPoolExecutor,as_completed
from pathlib import Path
from PIL import Image
import pikepdf,hashlib,io,json,shutil,subprocess,tempfile

ROOT=Path(__file__).resolve().parents[1]
JPEGTRAN='/opt/homebrew/opt/mozjpeg/bin/jpegtran'

def optimize(path):
    before_bytes=path.stat().st_size;modified=0;checks=[]
    with pikepdf.open(path) as pdf:
        for obj in pdf.objects:
            if not isinstance(obj,pikepdf.Stream) or obj.get('/Subtype')!=pikepdf.Name('/Image'):continue
            filters=obj.get('/Filter')
            if isinstance(filters,pikepdf.Array):filters=list(filters)
            else:filters=[filters]
            if filters!=[pikepdf.Name('/DCTDecode')]:continue
            raw=obj.read_raw_bytes()
            result=subprocess.run([JPEGTRAN,'-copy','all','-optimize','-progressive'],input=raw,capture_output=True,check=True).stdout
            if len(result)>=len(raw):continue
            old=Image.open(io.BytesIO(raw));new=Image.open(io.BytesIO(result))
            assert old.size==new.size and old.mode==new.mode and old.tobytes()==new.tobytes(),f'JPEG pixel change: {path}'
            params=obj.get('/DecodeParms')
            obj.write(result,filter=pikepdf.Name('/DCTDecode'))
            if params is not None:obj['/DecodeParms']=params
            checks.append(hashlib.sha256(result).hexdigest());modified+=1
        page_count=len(pdf.pages)
        with tempfile.NamedTemporaryFile(suffix='.pdf',delete=False) as temp:dest=Path(temp.name)
        pdf.save(dest,compress_streams=True,object_stream_mode=pikepdf.ObjectStreamMode.preserve)
    with pikepdf.open(dest) as pdf:
        assert len(pdf.pages)==page_count
        saved={hashlib.sha256(obj.read_raw_bytes()).hexdigest() for obj in pdf.objects if isinstance(obj,pikepdf.Stream) and obj.get('/Subtype')==pikepdf.Name('/Image')}
        assert all(check in saved for check in checks),f'JPEG changed during save: {path}'
    if dest.stat().st_size<before_bytes:shutil.move(dest,path)
    else:dest.unlink()
    return {'path':'/'+str(path.relative_to(ROOT)),'before_bytes':before_bytes,'published_bytes':path.stat().st_size,'optimized_images':modified,'verified_pixels_equal':True,'published_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}

if __name__=='__main__':
    files=sorted((ROOT/'_files').rglob('*.pdf'))
    results=[]
    with ThreadPoolExecutor(max_workers=8) as pool:
        jobs=[pool.submit(optimize,p) for p in files]
        for job in as_completed(jobs):
            results.append(job.result())
            if len(results)%25==0:print('Verified',len(results),'of',len(files),'PDFs',flush=True)
    results.sort(key=lambda r:r['path'])
    (ROOT/'migration/pdf-jpegs.json').write_text(json.dumps(results,indent=2))
    print('Before MB:',sum(r['before_bytes'] for r in results)/1e6,'After MB:',sum(r['published_bytes'] for r in results)/1e6,'JPEGs optimized:',sum(r['optimized_images'] for r in results))
    print('Every modified JPEG verified pixel-identical, with no resizing or quality reduction.')
