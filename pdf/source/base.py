# -*- coding: utf-8 -*-
"""Общая верстка PDF-памяток: A4, та же айдентика, что у презентации."""
import re, html

FONTS = '../../assets/fonts/fonts.css'

CSS = r"""
@page{size:A4;margin:0}
:root{--paper:#EFEFEB;--paper2:#E3E3DD;--ink:#121212;--ink2:#55554F;--line:#C9C9C1;
 --blue:#2335FF;--signal:#FF5A1F;--lime:#C6F432;--pink:#FF7BC2;--white:#fff;
 --fd:'Unbounded','Arial Black',sans-serif;--ft:'Onest','Manrope',Arial,sans-serif;--fm:'JetBrains Mono',monospace}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
html,body{margin:0;padding:0;background:#777}
body{font:400 10.2pt/1.42 var(--ft);color:var(--ink)}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;background:var(--paper);padding:16mm 15mm 18mm;
 page-break-after:always;break-after:page;display:flex;flex-direction:column}
.page:last-child{page-break-after:auto;break-after:auto}
.page::before{content:"";position:absolute;inset:0;background:url('../../assets/grain.png');opacity:.16;mix-blend-mode:multiply;pointer-events:none}
.page>*{position:relative}
.dark{background:var(--ink);color:var(--paper)}
.blue{background:var(--blue);color:#fff}
.lime{background:var(--lime)}
.run{display:flex;justify-content:space-between;font:500 7.4pt/1 var(--fm);letter-spacing:.07em;text-transform:uppercase;opacity:.6;margin-bottom:9mm}
.foot{position:absolute;left:15mm;right:15mm;bottom:9mm;display:flex;justify-content:space-between;font:400 7pt/1 var(--fm);opacity:.5}
.kick{font:500 8pt/1.2 var(--fm);letter-spacing:.08em;text-transform:uppercase;margin:0 0 4mm;opacity:.7}
h1{font:900 64pt/.84 var(--fd);letter-spacing:-.045em;margin:0 0 6mm}
h2{font:800 22pt/1 var(--fd);letter-spacing:-.03em;margin:0 0 4mm}
h3{font:700 12pt/1.15 var(--fd);letter-spacing:-.01em;margin:0 0 2mm}
p{margin:0 0 2.5mm}
.lead{font:400 13.5pt/1.32 var(--ft);max-width:150mm}
.muted{color:var(--ink2)}
.dark .muted,.blue .muted{color:inherit;opacity:.7}
.mono{font-family:var(--fm)}
a{color:inherit;text-decoration:underline;text-decoration-thickness:.5px;text-underline-offset:2px}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:6mm}
.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:5mm}
.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:4mm}
.box{padding:5mm;background:var(--white)}
.box.ink{background:var(--ink);color:var(--paper)}
.box.blue{background:var(--blue);color:#fff}
.box.lime{background:var(--lime)}
.box.p2{background:var(--paper2)}
.cell{border-top:1.4pt solid currentColor;padding-top:2.5mm}
.cell .k{font:500 7pt/1 var(--fm);text-transform:uppercase;letter-spacing:.06em;opacity:.6;display:block;margin-bottom:1.5mm}
.tag{display:inline-block;font:500 7pt/1 var(--fm);text-transform:uppercase;letter-spacing:.05em;padding:1.4mm 2.4mm;border:.8pt solid currentColor;border-radius:99px;margin:0 1mm 1mm 0}
.chip{display:inline-block;font:600 7pt/1 var(--fm);padding:1.3mm 2mm;background:var(--ink);color:var(--paper);text-transform:uppercase;letter-spacing:.05em}
.hand{font:700 16pt/1 'Caveat',cursive;color:var(--signal)}
/* таблица «нельзя / можно» */
.vs{width:100%;border-collapse:collapse;font-size:9pt;line-height:1.35}
.vs th{font:500 7pt/1 var(--fm);text-transform:uppercase;letter-spacing:.06em;text-align:left;padding:0 3mm 2mm 0;opacity:.6}
.vs td{border-top:.8pt solid var(--line);padding:2.1mm 3mm 2.1mm 0;vertical-align:top}
.vs td:first-child{width:46%}
.no,.yes{display:inline-block;width:3.6mm;height:3.6mm;border-radius:50%;margin-right:1.8mm;vertical-align:-.6mm;position:relative}
.no{background:var(--signal)}.yes{background:var(--blue)}
.no::before,.no::after{content:"";position:absolute;left:1.7mm;top:.7mm;width:.3mm;height:2.2mm;background:#fff;transform:rotate(45deg)}
.no::after{transform:rotate(-45deg)}
.yes::before{content:"";position:absolute;left:1.1mm;top:.6mm;width:1mm;height:1.8mm;border:solid #fff;border-width:0 .35mm .35mm 0;transform:rotate(45deg)}
/* чек-листы */
.cl{list-style:none;margin:0;padding:0}
.cl li{display:grid;grid-template-columns:5mm 1fr;gap:2.5mm;padding:1.7mm 0;border-top:.6pt solid var(--line);font-size:9.3pt;line-height:1.35;break-inside:avoid}
.cl li::before{content:"";width:3.8mm;height:3.8mm;border:1pt solid var(--ink);margin-top:.3mm;background:var(--white)}
.dark .cl li{border-color:#333}.dark .cl li::before{border-color:var(--paper);background:transparent}
.sec{break-inside:avoid;margin-bottom:5mm}
.sec h3{display:flex;gap:2.5mm;align-items:baseline}
.sec h3 b{font:700 8pt/1 var(--fm);color:var(--blue)}
/* промпт */
.prompt{background:var(--ink);color:#E9F5D5;font:400 7.9pt/1.5 var(--fm);padding:4.5mm 5mm;white-space:pre-wrap;margin:0}
.prompt em{font-style:normal;background:var(--lime);color:var(--ink);padding:0 1mm}
/* линейки для заполнения */
.lines{height:20mm;background:repeating-linear-gradient(transparent 0 6.4mm,var(--line) 6.4mm 6.7mm)}
.word{display:inline-block;padding:1.3mm 2.4mm;margin:0 1.4mm 1.6mm 0;background:var(--white);font-size:9pt;text-decoration:line-through;text-decoration-color:var(--signal);text-decoration-thickness:1.2pt}
.swatch{display:flex;flex-direction:column;gap:1mm;font:500 6.6pt/1.1 var(--fm)}
.swatch i{display:block;height:11mm;border:.5pt solid rgba(0,0,0,.15)}
ol.steps{list-style:none;margin:0;padding:0;counter-reset:s}
ol.steps li{counter-increment:s;display:grid;grid-template-columns:9mm 1fr;gap:3mm;padding:2.6mm 0;border-top:.8pt solid var(--line);break-inside:avoid}
ol.steps li::before{content:counter(s,decimal-leading-zero);font:800 12pt/1 var(--fd);color:var(--blue)}
ol.steps b{display:block;font:700 10.5pt/1.2 var(--ft);margin-bottom:.8mm}
.src{font:400 7pt/1.45 var(--fm);opacity:.75;columns:2;column-gap:6mm}
.src a{word-break:break-all}
.big-num{font:900 46pt/.85 var(--fd);letter-spacing:-.05em}
"""

LINK = re.compile(r'\[([^\]]+)\]\((https?://[^)]+)\)')
def md(s):
    """Мини-разметка: [текст](url), **жирный**, `код`."""
    s = html.escape(s, quote=False)
    s = LINK.sub(lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'`(.+?)`', r'<span class="mono">\1</span>', s)
    return s

def page(body, run_l, run_r, n, total, cls='', series='Сайты, что продают · Медиаком 2026', style=''):
    return f'''<section class="page {cls}" style="{style}">
<div class="run"><span>{run_l}</span><span>{run_r}</span></div>
{body}
<div class="foot"><span>{series}</span><span>{n} / {total}</span></div>
</section>'''

def doc(title, pages, extra_css=''):
    return f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><title>{html.escape(title)}</title>
<link rel="stylesheet" href="{FONTS}"><style>{CSS}{extra_css}</style></head><body>
{''.join(pages)}
</body></html>'''

def checklist(items):
    return '<ul class="cl">' + ''.join(f'<li><span>{md(i)}</span></li>' for i in items) + '</ul>'
