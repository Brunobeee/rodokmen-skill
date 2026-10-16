#!/usr/bin/env python3
# Ověření čtení (např. po pomocníkovi): výřez zápisu rozdělený na dvě poloviny 1900 px. Použití: overit.py <snímek.jpg> x0,y0,x1,y1 <prefix> [v]  (v = dělit vodorovně)
import sys,subprocess
f,box,pre=sys.argv[1:4]; mode=sys.argv[4] if len(sys.argv)>4 else 'h'
W,H=map(int,subprocess.run(['magick','identify','-format','%w %h',f],capture_output=True,text=True).stdout.split())
x0,y0,x1,y1=map(float,box.split(','))
if mode=='v': ym=(y0+y1)/2; parts=[(x0,y0,x1,ym+0.02),(x0,ym-0.02,x1,y1)]
else: xm=(x0+x1)/2; parts=[(x0,y0,xm+0.02,y1),(xm-0.02,y0,x1,y1)]
for i,(a,b,c,d) in enumerate(parts):
    o=f'{pre}_{i}.jpg'; subprocess.run(['magick',f,'-crop','%dx%d+%d+%d'%((c-a)*W,(d-b)*H,a*W,b*H),'+repage','-resize','1900x',o]); print(o)
