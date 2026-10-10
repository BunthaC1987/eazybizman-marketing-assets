#!/usr/bin/env python3
"""Render Eazybizman weekly post images exactly to the brand template (no image-gen credits).

Usage:  python tools/render_posts.py spec.json
spec.json = list of posts:
  {"file":"57_margin_problem_blunt.png","kind":"standard","eyebrow":"Sound familiar?","headline":"...","accent":"orange"|"white"}
  {"file":"...","kind":"beforeafter","eyebrow":"Before and after","headline":"...","before":"...","after":"..."}
  {"file":"...","kind":"cta","eyebrow":"Get started","headline":"...","button":"Run the free Margin Leak Check"}
Needs Pillow. Reuses the footer and the pipeline icon strip from existing images 21 and 29 in this repo.
"""
import json, sys, os
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
BOLD = ["C:/Windows/Fonts/LiberationSans-Bold.ttf","/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf","/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf","/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]
BG=(27,35,64); OR=(238,108,16); WH=(255,255,255); GR=(150,160,185)
def font(sz):
    for p in BOLD:
        if os.path.exists(p): return ImageFont.truetype(p, sz)
    raise SystemExit("No bold sans font found (install fonts-liberation)")
ref = Image.open(os.path.join(ROOT,"21_margin_problem_blunt.png")).convert("RGB")
footer = ref.crop((0,1050,1200,1200))
strip = Image.open(os.path.join(ROOT,"29_margin_pipeline_cta.png")).convert("RGB").crop((250,212,820,368))
def spaced(d,xy,t,f,fill,sp=3):
    x,y=xy
    for ch in t: d.text((x,y),ch,font=f,fill=fill); x+=d.textlength(ch,font=f)+sp
def wrap(d,t,f,w):
    out=[];ln=''
    for wd in t.split():
        c=(ln+' '+wd).strip()
        if d.textlength(c,font=f)<=w: ln=c
        else: out.append(ln); ln=wd
    out.append(ln); return out
def base(eyebrow,color):
    im=Image.new("RGB",(1200,1200),BG); d=ImageDraw.Draw(im)
    spaced(d,(80,80),eyebrow.upper(),font(26),color); d.rectangle([80,130,140,135],fill=color)
    im.paste(footer,(0,1050)); return im,d
def standard(p):
    color = OR if p.get("accent","orange")=="orange" else WH
    im,d=base(p["eyebrow"],color); f=font(66); L=wrap(d,p["headline"],f,900); y=(1050-len(L)*84)//2+10
    for l in L: d.text((80,y),l,font=f,fill=WH); y+=84
    return im
def beforeafter(p):
    im,d=base(p["eyebrow"],WH); f=font(66); y=240
    for l in wrap(d,p["headline"],f,1000): d.text((80,y),l,font=f,fill=WH); y+=84
    d.line([(600,460),(600,740)],fill=(36,52,84),width=2)
    spaced(d,(80,462),"BEFORE",font(24),GR); spaced(d,(620,462),"AFTER",font(24),OR)
    f2=font(38); y=510
    for l in wrap(d,p["before"],f2,470): d.text((80,y),l,font=f2,fill=WH); y+=50
    y=510
    for l in wrap(d,p["after"],f2,500): d.text((620,y),l,font=f2,fill=OR); y+=50
    return im
def cta(p):
    im,d=base(p["eyebrow"],OR); im.paste(strip,(250,212)); f=font(66); y=470
    for l in wrap(d,p["headline"],f,960): d.text((80,y),l,font=f,fill=WH); y+=84
    fb=font(34); w=int(d.textlength(p["button"],font=fb))+80; y+=24
    d.rounded_rectangle([80,y,80+w,y+76],radius=10,fill=OR); d.text((120,y+19),p["button"],font=fb,fill=WH)
    return im
K={"standard":standard,"beforeafter":beforeafter,"cta":cta}
for p in json.load(open(sys.argv[1],encoding="utf-8")):
    K[p["kind"]](p).save(os.path.join(ROOT,p["file"])); print("wrote",p["file"])
