#!/usr/bin/env python3
"""Losslessly pack oversized indexed image palettes; verify every changed pixel."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, tempfile, shutil, zlib
import numpy as np
import pikepdf

ROOT=Path(__file__).resolve().parents[1]
pikepdf.settings.set_flate_compression_level(9)

def pixels(obj):
    im=pikepdf.PdfImage(obj).as_pil_image().convert('RGB')
    return (im.size,hashlib.sha256(im.tobytes()).hexdigest())

def compact(path):
    old=path.stat().st_size;count=0;checks=[]
    with pikepdf.open(path) as pdf:
        for obj in pdf.objects:
            if not isinstance(obj,pikepdf.Stream) or obj.get('/Subtype')!=pikepdf.Name('/Image'):continue
            if obj.get('/BitsPerComponent')!=8 or obj.get('/Decode') or obj.get('/Mask'):continue
            cs=obj.get('/ColorSpace')
            if not isinstance(cs,pikepdf.Array) or cs[0]!=pikepdf.Name('/Indexed'):continue
            channels={'/DeviceRGB':3,'/DeviceGray':1}.get(str(cs[1]))
            if not channels:continue
            data=obj.read_bytes();w=int(obj.Width);h=int(obj.Height)
            if len(data)!=w*h:continue
            a=np.frombuffer(data,dtype=np.uint8).reshape(h,w);unique=np.unique(a)
            n=len(unique)
            if not 1<n<=16:continue
            bits=1 if n<=2 else 2 if n<=4 else 4
            lut=np.zeros(256,dtype=np.uint8);lut[unique]=np.arange(n,dtype=np.uint8)
            indices=lut[a];per_byte=8//bits
            pad=(-w)%per_byte
            if pad:indices=np.pad(indices,((0,0),(0,pad)))
            packed=np.zeros((h,indices.shape[1]//per_byte),dtype=np.uint8)
            for i in range(per_byte):packed|=indices[:,i::per_byte] << (8-bits*(i+1))
            encoded=zlib.compress(packed.tobytes(),9)
            if len(encoded)>=len(obj.read_raw_bytes()):continue
            palette=cs[3].read_bytes() if isinstance(cs[3],pikepdf.Stream) else bytes(cs[3])
            new_palette=b''.join(palette[int(i)*channels:(int(i)+1)*channels] for i in unique)
            before=pixels(obj)
            obj.write(encoded,filter=pikepdf.Name('/FlateDecode'))
            obj['/BitsPerComponent']=bits
            obj['/ColorSpace']=pikepdf.Array([pikepdf.Name('/Indexed'),cs[1],n-1,pikepdf.String(new_palette)])
            if '/DecodeParms' in obj:del obj['/DecodeParms']
            assert pixels(obj)==before, f'Pixel mismatch in {path}'
            checks.append(before);count+=1
        with tempfile.NamedTemporaryFile(suffix='.pdf',delete=False) as temp:dest=Path(temp.name)
        pdf.save(dest,compress_streams=True,object_stream_mode=pikepdf.ObjectStreamMode.generate)
        page_count=len(pdf.pages)
    with pikepdf.open(dest) as pdf:
        assert len(pdf.pages)==page_count
        after=[pixels(obj) for obj in pdf.objects if isinstance(obj,pikepdf.Stream) and obj.get('/Subtype')==pikepdf.Name('/Image') and isinstance(obj.get('/ColorSpace'),pikepdf.Array) and obj.get('/BitsPerComponent',8)<8]
        for check in checks:assert check in after, f'Saved image mismatch in {path}'
    if count and dest.stat().st_size<old:shutil.move(dest,path)
    else:dest.unlink()
    return {'path':'/'+str(path.relative_to(ROOT)),'before_bytes':old,'published_bytes':path.stat().st_size,'packed_images':count,'verified_pixels_equal':True,'published_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}

if __name__=='__main__':
    files=sorted((ROOT/'_files').rglob('*.pdf'))
    with ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(compact,files))
    (ROOT/'migration/pdf-palettes.json').write_text(json.dumps(results,indent=2))
    print('Before MB:',sum(r['before_bytes'] for r in results)/1e6,'After MB:',sum(r['published_bytes'] for r in results)/1e6,'Images packed:',sum(r['packed_images'] for r in results))
    print('Every modified image verified pixel-identical before and after saving.')
