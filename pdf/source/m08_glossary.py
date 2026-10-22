# -*- coding: utf-8 -*-
import html
from base import page, doc
import guide_content as G

R = 'Памятка 08 · Словарь'
EXTRA = [("152-ФЗ", "закон о персональных данных: политика, согласие, хранение данных россиян в РФ."),
         ("Лендинг", "одностраничный сайт под одно целевое действие, обычно под рекламу."),
         ("Референс", "пример чужой работы, на который ориентируются по стилю.")]

def build():
    items = sorted(G.GLOSSARY + EXTRA, key=lambda x: x[0].lower())
    half = (len(items) + 1) // 2
    def col(lst):
        return ''.join(f'<div style="border-top:.8pt solid var(--line);padding:2.2mm 0;break-inside:avoid"><b style="font:700 10pt/1.2 var(--fd)">{html.escape(t)}</b><div style="font-size:9pt;line-height:1.38;margin-top:.8mm">{html.escape(d[0].upper()+d[1:])}</div></div>' for t, d in lst)
    p1 = f'''<p class="kick">Памятка 08 из 08</p>
<h1 style="font-size:54pt">Словарь</h1>
<p class="lead" style="margin-bottom:5mm">{len(items)} слов, которые вы услышите от разработчиков, дизайнеров и нейросетей.</p>
<div class="g2" style="gap:8mm">{'<div>'+col(items[:10])+'</div><div>'+col(items[10:20])+'</div>'}</div>'''
    p2 = f'''<div class="g2" style="gap:8mm">{'<div>'+col(items[20:28])+'</div><div>'+col(items[28:])+'</div>'}</div>
<div class="box lime" style="margin-top:auto"><p style="margin:0;font:700 11pt/1.3 var(--ft)">Не знаете слово? Спросите нейросеть: «Объясни, что такое CDN, как маркетологу, на примере кофейни». Это самый быстрый учитель.</p></div>'''
    return doc('Словарь', [page(p1, R, 'Термины', 1, 2), page(p2, R, 'Термины', 2, 2)])
