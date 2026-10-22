# -*- coding: utf-8 -*-
import html
from base import page, doc, md
import guide_content as G

R = 'Памятка 07 · Шрифты и анимации'
SPEC = [("Unbounded","900 22pt 'Unbounded'","Ветер"),("Dela Gothic One","400 22pt 'Dela Gothic One'","Шторм"),
 ("Onest","500 22pt 'Onest'","Тишина"),("Manrope","800 22pt 'Manrope'","Маяк"),
 ("Oswald","700 24pt 'Oswald'","ЖУРНАЛ"),("Playfair Display","italic 400 23pt 'Playfair Display'","Обложка"),
 ("Cormorant Garamond","italic 500 24pt 'Cormorant Garamond'","Шепот"),("Yeseva One","400 22pt 'Yeseva One'","Мелочи"),
 ("Marck Script","400 25pt 'Marck Script'","Роза"),("Caveat","700 25pt 'Caveat'","от руки"),
 ("Pangolin","400 22pt 'Pangolin'","Пломбир"),("Rubik Dirt","400 22pt 'Rubik Dirt'","Гараж"),
 ("Rubik Glitch","400 22pt 'Rubik Glitch'","Сбой"),("Press Start 2P","400 13pt 'Press Start 2P'","Игра"),
 ("JetBrains Mono","700 21pt 'JetBrains Mono'","Сигнал"),("IBM Plex Mono","400 19pt 'IBM Plex Mono'","Подпись")]

def build():
    spec = ''.join(f'<div style="border-top:.8pt solid var(--line);padding-top:2mm"><div style="font:{f};line-height:1.15;white-space:nowrap;overflow:hidden">{w}</div><div class="mono" style="font-size:6.8pt;opacity:.6;margin-top:1mm">{n}</div></div>' for n, f, w in SPEC[:12])
    pairs = ''.join(f'<tr><td>{a}</td><td>{html.escape(b)}</td></tr>' for a, b in G.PAIRS[:9])
    found = ''.join(f'<div style="margin-bottom:1.6mm"><a href="{u}"><b>{n}</b></a> <span class="muted">{html.escape(d)}</span></div>' for n, u, d in G.FOUNDRIES[:5])
    p1 = f'''<p class="kick">Памятка 07 из 08</p>
<h1 style="font-size:42pt">Шрифты и анимации</h1>
<p class="lead" style="margin-bottom:5mm;font-size:12pt">Шрифт делает половину стиля. Все шрифты ниже бесплатные, с кириллицей, лежат в папке assets/fonts и на Google Fonts.</p>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:3.5mm 5mm;margin-bottom:6mm">{spec}</div>
<div class="g2" style="gap:7mm">
 <div><h3>Пары под тренды</h3><table class="vs" style="font-size:8.4pt">{pairs}</table></div>
 <div><h3>Правила</h3>
  <ul style="margin:0 0 4mm;padding-left:4mm;font-size:9pt"><li>Не больше двух семейств: одно для заголовков, второе для текста</li><li>Проверяйте кириллицу на реальном тексте, у части рукописных шрифтов ее нет</li><li>Основной текст на телефоне от 16 px</li><li>Inter и системный шрифт на всём выдают ИИ-шаблон</li><li>Для коммерческого сайта проверьте лицензию: у Google Fonts это OFL, можно</li></ul>
  <h3>Российские словолитни</h3><div style="font-size:8.3pt;line-height:1.35">{found}</div></div>
</div>'''
    libs = ''.join(f'<tr><td><a href="{u}">{n}</a></td><td style="font-size:7.6pt;line-height:1.3">{html.escape(use)}</td><td class="mono" style="font-size:7pt">{lvl}</td></tr>' for n, u, d, lvl, use in G.LIBS)
    rb = ''.join(f'<div style="border-top:.6pt solid var(--line);padding:1.2mm 0;font-size:7.6pt;line-height:1.3"><a href="https://reactbits.dev/{p}"><b>{n}</b></a> <span class="muted">{html.escape(d)}</span></div>' for n, p, d in G.REACTBITS[:18])
    p2 = f'''<div class="g2" style="gap:6mm;grid-template-columns:1.3fr 1fr">
 <div><h2>Библиотеки</h2><table class="vs" style="font-size:8pt"><tr><th>Что</th><th>Для чего</th><th>Сложность</th></tr>{libs}</table>
  <div class="box lime" style="margin-top:5mm"><p class="kick" style="opacity:1">Правила моушена</p>
  <ul style="margin:0;padding-left:4mm;font-size:8.4pt"><li>2-3 осмысленные анимации на страницу: заголовок, кнопка, счетчик</li><li>Одна главная сцена лучше эффектов везде</li><li>Контент виден и без анимации</li><li>Уважайте настройку «уменьшить движение» (prefers-reduced-motion)</li><li>Проверяйте на слабом телефоне</li></ul></div></div>
 <div><h2>reactbits.dev</h2><p class="muted" style="font-size:8.5pt">Бесплатные анимированные компоненты. Скопируйте код или назовите эффект нейросети.</p>{rb}
  <pre class="prompt" style="margin-top:4mm">Добавь появление заголовка по буквам
как Split Text из reactbits и магнитную
кнопку как Magnet. Уважай
prefers-reduced-motion.</pre></div>
</div>'''
    return doc('Шрифты и анимации', [page(p1, R, 'Шрифты', 1, 2), page(p2, R, 'Анимации', 2, 2)])
