# -*- coding: utf-8 -*-
import re, html
from base import page, doc, md
import guide_content as G

R = 'Памятка 04 · Тренды 2026'
# оформление страницы под каждый тренд
LOOK = {
 'oversize': dict(bg='#F1F0EB', fg='#111111', acc='#FF4D00', panel='#111111', pfg='#F1F0EB', disp="900 74pt/.8 'Dela Gothic One'", title='ТУМАН', site='01', sitename='ТУМАН', pair='Dela Gothic One + Onest'),
 'editorial': dict(bg='#F4F1EA', fg='#1B1B1B', acc='#8C1C13', panel='#1B1B1B', pfg='#F4F1EA', disp="italic 500 64pt/.9 'Cormorant Garamond'", title='Editorial 2.0', site='02', sitename='СДВИГ', pair='Cormorant Garamond + Onest + IBM Plex Mono'),
 'swiss': dict(bg='#FFFFFF', fg='#0A0A0A', acc='#E30613', panel='#0A0A0A', pfg='#FFFFFF', disp="700 54pt/.9 'Onest'", title='Модульная сетка', site='02', sitename='СДВИГ, кнопка «показать сетку»', pair='Onest 700 + Onest 400 + JetBrains Mono', grid=True),
 'bento': dict(bg='#EDEDE8', fg='#151515', acc='#2E5BFF', panel='#151515', pfg='#EDEDE8', disp="800 66pt/.88 'Manrope'", title='Bento box', site='03', sitename='МАЯК', pair='Manrope 800 + Manrope 400 + JetBrains Mono'),
 'rococo': dict(bg='#1F3B2D', fg='#F6F1EA', acc='#E8C9C1', panel='#F6F1EA', pfg='#1F3B2D', disp="400 70pt/1 'Marck Script'", title='New Rococo', site='04', sitename='Мох и Роза', pair='Marck Script + Cormorant Garamond'),
 'ascii': dict(bg='#0B0C0A', fg='#D6FFD1', acc='#39FF14', panel='#D6FFD1', pfg='#0B0C0A', disp="700 58pt/.95 'JetBrains Mono'", title='ASCII ART', site='05', sitename='СИГНАЛ', pair='JetBrains Mono + IBM Plex Mono'),
 'grunge': dict(bg='#E9E4D8', fg='#0D0D0D', acc='#FF2E88', panel='#0D0D0D', pfg='#C6FF00', disp="400 70pt/.9 'Rubik Dirt'", title='PUNK GRUNGE', site='06', sitename='ГАРАЖ', pair='Rubik Dirt + Press Start 2P + Oswald'),
 'naive': dict(bg='#FFF8E7', fg='#1E1E1E', acc='#FF5A36', panel='#2BB673', pfg='#1E1E1E', disp="400 70pt/.95 'Pangolin'", title='Naive', site='07', sitename='Пломбир с Седанки', pair='Pangolin или Caveat + Rubik'),
 'trinket': dict(bg='#EFEAE0', fg='#1A1A1A', acc='#D9402B', panel='#1A1A1A', pfg='#EFEAE0', disp="italic 900 66pt/.9 'Playfair Display'", title='Trinket', site='08', sitename='Мелочи', pair='Playfair Display + IBM Plex Mono + Onest'),
}
ORDER = ['oversize', 'editorial', 'swiss', 'bento', 'rococo', 'ascii', 'grunge', 'naive', 'trinket']

def palette(prompt):
    cols = re.findall(r'([^,:;.\n]{0,24}?)\s*#([0-9A-Fa-f]{6})', prompt)
    out = []
    for name, hx in cols:
        name = name.strip(' :,').split(' ')[-1] if name.strip() else ''
        out.append((name, '#' + hx.upper()))
    return out[:6]

def build():
    total = len(ORDER) + 1
    def tfont(k):
        m = re.match(r"(.*?)\d+pt/[\d.]+ ('.*')", LOOK[k]['disp'])
        return f"{m.group(1)}17pt/1 {m.group(2)}"
    tiles = ''.join(f'''<div style="background:{LOOK[k]['bg']};color:{LOOK[k]['fg']};padding:3.5mm;display:flex;flex-direction:column;justify-content:space-between;min-height:31mm;border:.5pt solid rgba(0,0,0,.1)">
 <span style="font:500 6.5pt var(--fm);opacity:.6">{i+1:02d}</span><span style="font:{tfont(k)};color:{LOOK[k]['acc'] if k not in ('rococo','naive') else LOOK[k]['fg']}">{LOOK[k]['title']}</span></div>''' for i, k in enumerate(ORDER))
    cover = f'''<p class="kick">Памятка 04 из 09</p>
<h1 style="font-size:70pt">Тренды 2026</h1>
<p class="lead" style="margin-bottom:8mm">Девять визуальных направлений для лендингов. На каждой странице: что это, признаки, где работает и где нет, палитра, шрифты, пример из набора и блок стиля для промпта.</p>
<div class="g3" style="gap:4mm">{tiles}</div>
<div class="box ink" style="margin-top:auto"><p class="kick" style="color:var(--lime);opacity:1">Как пользоваться</p>
<p style="margin:0">Выберите один тренд под бизнес и аудиторию. Скопируйте его блок стиля в конец промпта для Lovable, Google AI Studio или Claude, после описания бизнеса и структуры. Над всеми трендами стоит анти-ИИ: свои фото, реальные цифры, приём только с причиной.</p></div>'''
    pages = [page(cover, R, 'Обзор', 1, total)]
    trends = {t['id']: t for t in G.TRENDS}
    for n, k in enumerate(ORDER):
        t, L = trends[k], LOOK[k]
        pr = G.PROMPTS[k]
        sw = ''.join(f'<div class="swatch"><i style="background:{hx}"></i><span>{hx}</span></div>' for _, hx in palette(pr))
        signs = ''.join(f'<li style="margin-bottom:1.4mm">{md(s)}</li>' for s in t['signs'])
        refs = ''.join(f'<div><a href="{u}">{html.escape(nm)}</a></div>' for nm, u in t['refs'][:4])
        grid = ''
        if L.get('grid'):
            grid = '<div style="position:absolute;inset:0 15mm;display:grid;grid-template-columns:repeat(12,1fr);gap:3mm;pointer-events:none">' + ''.join('<i style="border-left:.4pt solid #E3061333;border-right:.4pt solid #E3061333"></i>' for _ in range(12)) + '</div>'
        body = f'''{grid}
<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:6mm;margin-bottom:5mm">
 <div><p class="kick" style="color:{L['acc']};opacity:1">{n+1:02d} · {html.escape(t['short'])}</p>
 <div style="font:{L['disp']};letter-spacing:-.02em;color:{L['fg']}">{L['title']}</div></div>
</div>
<div class="g2" style="gap:7mm;grid-template-columns:1.15fr 1fr">
 <div>
  <p style="font-size:10.5pt;line-height:1.45">{md(t['what'])}</p>
  <p class="kick" style="margin-top:4mm;margin-bottom:2mm">Признаки</p>
  <ul style="margin:0;padding-left:4mm;font-size:9.3pt">{signs}</ul>
  <div class="g2" style="gap:4mm;margin-top:4mm">
   <div style="border-top:1.4pt solid {L['acc']};padding-top:2mm"><span class="k mono" style="font-size:7pt;opacity:.7;text-transform:uppercase">Где работает</span><p style="font-size:8.8pt;margin-top:1.5mm">{md(t['use'])}</p></div>
   <div style="border-top:1.4pt solid currentColor;padding-top:2mm"><span class="k mono" style="font-size:7pt;opacity:.7;text-transform:uppercase">Где не стоит</span><p style="font-size:8.8pt;margin-top:1.5mm">{md(t['dont'])}</p></div>
  </div>
 </div>
 <div>
  <div style="aspect-ratio:16/10;overflow:hidden;border:.5pt solid rgba(127,127,127,.4);margin-bottom:1.5mm"><img src="../../assets/thumbs/{L['site']}.webp" style="width:100%;height:100%;object-fit:cover;object-position:top" alt=""></div>
  <p class="mono" style="font-size:7pt;opacity:.7;margin-bottom:4mm">ПРИМЕР В НАБОРЕ: sites/{L['site']} · {html.escape(L['sitename'])}</p>
  <p class="kick" style="margin-bottom:2mm">Палитра</p>
  <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:2mm;margin-bottom:4mm">{sw}</div>
  <p class="kick" style="margin-bottom:1.5mm">Шрифты</p><p style="font-size:9.5pt"><b>{html.escape(L['pair'])}</b></p>
  <p class="kick" style="margin:3mm 0 1.5mm">Референсы</p><div style="font:400 7.6pt/1.5 var(--fm)">{refs}</div>
 </div>
</div>
<div style="margin-top:auto"><p class="kick" style="margin-bottom:2mm">Блок стиля для промпта</p>
<pre class="prompt" style="background:{L['panel']};color:{L['pfg']};font-size:7.5pt">{html.escape(pr)}</pre></div>'''
        pages.append(page(body, R, t['name'], n + 2, total, style=f'background:{L["bg"]};color:{L["fg"]}'))
    return doc('Тренды 2026', pages)
