# -*- coding: utf-8 -*-
"""Сборка PDF-памяток: python3 build.py [номер ...]. HTML пишется рядом, PDF в папку pdf/."""
import sys, os, importlib
from playwright.sync_api import sync_playwright
from pypdf import PdfWriter, PdfReader

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(OUT, '..', 'guide', 'source'))

MEMOS = [
 ('m01_antiai', '01-anti-ii.pdf'),
 ('m02_checklist', '02-cheklist-lendinga.pdf'),
 ('m03_evening', '03-lending-za-vecher.pdf'),
 ('m04_trends', '04-trendy-2026.pdf'),
 ('m05_seo', '05-skorost-i-seo.pdf'),
 ('m06_launch', '06-zapusk-v-rossii.pdf'),
 ('m07_fonts', '07-shrifty-i-animacii.pdf'),
 ('m08_glossary', '08-slovar.pdf'),
]

def main(only):
    with sync_playwright() as p:
        b = p.chromium.launch()
        for mod, pdf in MEMOS:
            if only and mod[1:3] not in only: continue
            if not os.path.exists(os.path.join(HERE, mod + '.py')): continue
            m = importlib.import_module(mod)
            h = os.path.join(HERE, mod + '.html')
            open(h, 'w').write(m.build())
            pg = b.new_page()
            pg.goto('file://' + h); pg.wait_for_timeout(700)
            ov = pg.evaluate('''[...document.querySelectorAll('.page')].map((p,i)=>{const r=p.getBoundingClientRect();let m=0;p.querySelectorAll('*').forEach(e=>{if(e.closest('.foot'))return;const b=e.getBoundingClientRect().bottom-r.top;if(b>m)m=b});return [i+1,Math.round(m/r.height*1000)/10]}).filter(x=>x[1]>94)''')
            if ov: print('  OVERFLOW?', pdf, ov)
            pg.pdf(path=os.path.join(OUT, pdf), format='A4', print_background=True, prefer_css_page_size=True)
            pg.close(); print('ok', pdf)
        b.close()
    # общий сборник
    w = PdfWriter()
    for _, pdf in MEMOS:
        f = os.path.join(OUT, pdf)
        if os.path.exists(f):
            for pgx in PdfReader(f).pages: w.add_page(pgx)
    w.add_metadata({'/Title': 'Сайты, что продают: все памятки', '/Author': 'Даниил Комаров'})
    w.write(os.path.join(OUT, '00-vse-pamyatki.pdf'))

if __name__ == '__main__':
    main(sys.argv[1:])
