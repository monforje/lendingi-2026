# -*- coding: utf-8 -*-
import re, html, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from guide_content import *

def esc(s): return html.escape(s, quote=True)
def inl(s):
    s = esc(s)
    s = re.sub(r'\[([^\]]+)\]\((https?://[^)\s]+)\)', lambda m: f'<a href="{m.group(2)}" target="_blank" rel="noopener">{m.group(1)}</a>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    return s
def a(t,u): return f'<a href="{esc(u)}" target="_blank" rel="noopener">{esc(t)}</a>'
def host(u): return re.sub(r'^https?://(www\.)?','',u).split('/')[0]

SECTIONS = [("trends","Тренды 2026"),("galleries","Галереи"),("motion","Анимации"),("fonts","Шрифты"),
            ("assets","Фото и ассеты"),("antiai","Анти-ИИ чек-лист"),("evening","Лендинг за вечер"),
            ("prompts","Промпты по стилям"),("checklists","Чек-листы"),("glossary","Словарь")]

links=set()
def L(u): links.add(u); return u

H=[]
def sec_head(i,id_,title,lead):
    return f'<section id="{id_}" class="sec"><header class="sec-head"><span class="sec-num">{i:02d}</span><h2>{esc(title)}</h2><p class="lead">{inl(lead)}</p></header>'

# 1 trends
s=sec_head(1,"trends","Тренды 2026 и где смотреть живые примеры","Десять направлений, которые стоит знать маркетологу. Для каждого: что это, признаки, где уместно и где нет, и проверенные ссылки на живые примеры.")
s+='<nav class="chips" aria-label="Тренды">'+''.join(f'<a href="#t-{t["id"]}">{esc(t["name"])}</a>' for t in TRENDS)+'</nav>'
for n,t in enumerate(TRENDS,1):
    refs=''.join(f'<li>{a(r[0],L(r[1]))}<span class="host">{esc(host(r[1]))}</span></li>' for r in t["refs"])
    signs=''.join(f'<li>{inl(x)}</li>' for x in t["signs"])
    s+=f'''<article class="trend" id="t-{t["id"]}">
<div class="trend-top"><span class="tnum">1.{n}</span><h3>{esc(t["name"])}</h3><span class="tshort">{esc(t["short"])}</span></div>
<p>{inl(t["what"])}</p>
<div class="trend-grid">
<div><h4>Признаки</h4><ul class="dots">{signs}</ul></div>
<div><h4 class="ok">Когда использовать</h4><p>{inl(t["use"])}</p><h4 class="no">Когда не использовать</h4><p>{inl(t["dont"])}</p></div>
</div>
<div class="refs"><h4>Референсы</h4><ul>{refs}</ul></div>
<a class="to-prompt" href="#p-{t["id"]}">Промпт стиля для этого тренда</a>
</article>'''
H.append(s+'</section>')

# 2 galleries
s=sec_head(2,"galleries","Галереи и источники вдохновения","Куда идти за референсами. Собирайте 3-5 примеров в одну доску на Are.na, Cosmos или Savee и показывайте нейросети и подрядчику.")
s+='<dl class="rows">'+''.join(f'<div class="row"><dt>{a(g[0],L(g[1]))}</dt><dd>{inl(g[2])}</dd></div>' for g in GALLERIES)+'</dl>'
H.append(s+'</section>')

# 3 motion
s=sec_head(3,"motion","Анимации и микроанимации","Правило: 2-3 осмысленные анимации на лендинг. Анимация должна подсказывать, куда смотреть, а не развлекать.")
s+='<h3 class="sub">Библиотеки</h3><div class="libs">'
for l in LIBS:
    s+=f'<div class="lib"><div class="lib-top"><h4>{a(l[0],L(l[1]))}</h4><span class="lvl">{esc(l[3])}</span></div><p>{inl(l[2])}</p><p class="muted"><b>Для чего:</b> {inl(l[4])}</p></div>'
s+='</div>'
L("https://webflow.com/blog/gsap-becomes-free"); L("https://gsap.com/blog/3-13/")
s+=f'<p class="note">Факт про GSAP подтвержден: {a("блог Webflow","https://webflow.com/blog/gsap-becomes-free")} и {a("релиз GSAP 3.13","https://gsap.com/blog/3-13/")}. Все бывшие плагины Club GSAP (SplitText, MorphSVG, ScrollSmoother и др.) бесплатны, лицензия покрывает коммерческое использование.</p>'
s+=f'<h3 class="sub">React Bits: {len(REACTBITS)} компонентов для лендингов</h3><p>{a("reactbits.dev",L("https://reactbits.dev/"))}: бесплатная коллекция, разделы Text Animations, Animations, Components, Backgrounds и Micro Interactions. Названия ниже сверены с каталогом. Как использовать в Lovable: «Добавь эффект Split Text из reactbits.dev на заголовок hero».</p>'
s+='<ol class="rb">'+''.join(f'<li><span class="rb-name">{a(r[0],L("https://reactbits.dev/"+r[1]))}</span><span class="rb-cat">{esc(r[1].split("/")[0])}</span><span class="rb-what">{esc(r[2])}</span></li>' for r in REACTBITS)+'</ol>'
H.append(s+'</section>')

# 4 fonts
s=sec_head(4,"fonts","Шрифты с кириллицей для сильной типографики","Хорошая типографика дает 80% «дорогого» вида. Выбирайте 1-2 шрифта и проверяйте кириллицу на реальном тексте: буквы Ж, Ф, Щ, Ы и ё.")
s+='<h3 class="sub">Бесплатные (Google Fonts, лицензия OFL)</h3><div class="fonts">'
for f in FONTS_FREE:
    s+=f'<div class="font"><span class="specimen" style="font-family:\'{esc(f[0])}\'">Ёж</span><div>{a(f[0],L(f[1]))}<p>{esc(f[2])}</p></div></div>'
s+='</div>'
L("https://www.typewolf.com/google-fonts")
s+=f'<p class="muted">Фильтр по кириллице: в каталоге Google Fonts выберите Language: Cyrillic. Подборка бесплатных шрифтов с разбором: {a("Typewolf: Google Fonts","https://www.typewolf.com/google-fonts")}.</p>'
s+='<h3 class="sub">Российские и русскоязычные словолитни (платные)</h3><dl class="rows">'+''.join(f'<div class="row"><dt>{a(f[0],L(f[1]))}</dt><dd>{esc(f[2])}</dd></div>' for f in FOUNDRIES)+'</dl>'
L("https://openfontlicense.org/")
s+=f'''<h3 class="sub">Как проверить лицензию</h3><ol class="steps-s">
<li>Google Fonts: все шрифты под {a("SIL Open Font License",'https://openfontlicense.org/')} или Apache, можно в коммерции, на сайте и в печати. Нельзя продавать сам шрифт.</li>
<li>Платные словолитни: лицензии делятся на desktop (макеты, печать), web (подключение на сайт, часто по числу просмотров), app и logo. Для сайта нужна именно web-лицензия.</li>
<li>Скачали «бесплатно» с файлообменника: это не лицензия. Риск претензии и штрафа ложится на владельца сайта.</li>
<li>Логотип на платном шрифте: уточните, разрешает ли лицензия использование в товарном знаке.</li>
<li>Сохраните чек или скрин лицензии в папке проекта.</li></ol>'''
s+='<h3 class="sub">Пары шрифтов для каждого тренда</h3><dl class="rows pairs">'+''.join(f'<div class="row"><dt>{esc(p[0])}</dt><dd>{esc(p[1])}</dd></div>' for p in PAIRS)+'</dl>'
H.append(s+'</section>')

# 5 assets
s=sec_head(5,"assets","Фото, иллюстрации и ассеты без нейросетевого лоска","Главный анти-ИИ прием: свой контент. Если своего нет, берите архивы и свободные библиотеки и всегда проверяйте лицензию у конкретного изображения.")
s+='<h3 class="sub">Фото и архивы</h3><dl class="rows">'+''.join(f'<div class="row"><dt>{a(p[0],L(p[1]))}</dt><dd>{inl(p[2])}</dd></div>' for p in PHOTO)+'</dl>'
s+='<h3 class="sub">Текстуры, 3D, иконки, логотипы</h3><dl class="rows">'+''.join(f'<div class="row"><dt>{a(p[0],L(p[1]))}</dt><dd>{inl(p[2])}</dd></div>' for p in ASSETS3D)+'</dl>'
s+='<h3 class="sub">Как сделать визуал «анти-ИИ»</h3><ol class="steps-s">'+''.join(f'<li>{inl(x)}</li>' for x in ANTIAI_VISUAL)+'</ol>'
H.append(s+'</section>')

# 6 anti-ai
s=sec_head(6,"antiai","Анти-ИИ чек-лист",f"{len(ANTIAI_CHECK)} признаков сайта, собранного нейросетью без вкуса, и что делать вместо каждого. Отмечайте найденное на своем сайте.")
s+='<ol class="aic">'+''.join(f'<li><label><input type="checkbox" data-k="ai{i}"><span class="bad">{esc(b)}</span></label><span class="fix">{esc(f)}</span></li>' for i,(b,f) in enumerate(ANTIAI_CHECK))+'</ol>'
H.append(s+'</section>')

# 7 evening
s=sec_head(7,"evening","Памятка «Лендинг за вечер»","От идеи до работающего сайта с заявками и аналитикой за 3-4 часа.")
for u in re.findall(r'\((https?://[^)\s]+)\)', ''.join(e[1] for e in EVENING)): L(u)
s+='<ol class="evening">'+''.join(f'<li><h4>{esc(e[0])}</h4><p>{inl(e[1])}</p></li>' for e in EVENING)+'</ol>'
H.append(s+'</section>')

# 8 prompts
s=sec_head(8,"prompts","Промпты по стилям","Готовые блоки стиля для Lovable, Google AI Studio, Claude или ChatGPT Sites. "+PALETTE_NOTE+" Шрифты, HEX и запреты можно менять под бренд.")
s+='''<details class="tpl"><summary>Шаблон всего промпта</summary><pre>Сделай одностраничный лендинг на русском языке для [бизнес, город].
Аудитория: [кто]. Оффер: [что, за сколько, к какому сроку].
Блоки: hero с оффером и одной кнопкой, проблема, решение, цены, отзывы, FAQ, форма заявки (имя, телефон, отдельный чекбокс согласия на обработку персональных данных со ссылкой на политику), футер с контактами.
Мобильная версия в приоритете, без горизонтального скролла.
[ВСТАВЬ БЛОК СТИЛЯ НИЖЕ]</pre></details>'''
names={t["id"]:t["name"] for t in TRENDS}
for t in TRENDS:
    p=PROMPTS[t["id"]]
    s+=f'<div class="prompt" id="p-{t["id"]}"><div class="prompt-top"><h3>{esc(names[t["id"]])}</h3><button class="copy" type="button">Скопировать</button></div><pre tabindex="0">{esc(p)}</pre></div>'
H.append(s+'</section>')

# 9 checklists
s=sec_head(9,"checklists","Чек-листы","Галочки сохраняются в этом браузере. Кнопка «Сбросить» очищает раздел.")
s+='<div class="cls">'
for k,(title,items) in CHECKLISTS.items():
    s+=f'<div class="cl" data-cl="{k}"><div class="cl-top"><h3>{esc(title)}</h3><span class="cnt"></span></div><ul>'+''.join(f'<li><label><input type="checkbox" data-k="{k}{i}"><span>{inl(x)}</span></label></li>' for i,x in enumerate(items))+'</ul><button class="reset" type="button">Сбросить</button></div>'
s+='</div>'
L("https://www.consultant.ru/document/cons_doc_LAW_61801/"); L("https://web.dev/articles/vitals")
s+=f'<p class="muted">Первоисточники: {a("152-ФЗ «О персональных данных» на КонсультантПлюс","https://www.consultant.ru/document/cons_doc_LAW_61801/")}, {a("Core Web Vitals на web.dev","https://web.dev/articles/vitals")}. Чек-лист по 152-ФЗ это памятка, а не юридическая консультация.</p>'
H.append(s+'</section>')

# 10 glossary
s=sec_head(10,"glossary","Словарь терминов",f"{len(GLOSSARY)} слов, которые звучат на созвонах с разработчиками и в интерфейсах ИИ-конструкторов.")
s+='<dl class="gloss">'+''.join(f'<div><dt>{esc(g[0])}</dt><dd>{esc(g[1])}</dd></div>' for g in GLOSSARY)+'</dl>'
H.append(s+'</section>')

toc=''.join(f'<li><a href="#{i}"><span>{n:02d}</span>{esc(t)}</a></li>' for n,(i,t) in enumerate(SECTIONS,1))

CSS=r'''
:root{--bg:#F4F2EC;--paper:#FBFAF6;--ink:#1A1916;--ink2:#55524A;--line:#DAD6CC;--acc:#C2381E;--acc2:#1F4FD8;--ok:#2F6B3A;--code:#EFECE4;--mark:#FFE9A8;}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#151513;--paper:#1D1D1A;--ink:#ECE8DE;--ink2:#A39F94;--line:#34322D;--acc:#FF7A5C;--acc2:#8CA8FF;--ok:#7CC489;--code:#24231F;--mark:#4A3F17;}}
:root[data-theme="dark"]{--bg:#151513;--paper:#1D1D1A;--ink:#ECE8DE;--ink2:#A39F94;--line:#34322D;--acc:#FF7A5C;--acc2:#8CA8FF;--ok:#7CC489;--code:#24231F;--mark:#4A3F17;}
*{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 'Onest',system-ui,sans-serif;overflow-x:hidden}
a{color:var(--ink);text-decoration-color:var(--acc);text-underline-offset:3px;text-decoration-thickness:1.5px}
a:hover{color:var(--acc)}
code{font-family:'JetBrains Mono',monospace;font-size:.85em;background:var(--code);padding:1px 5px;border-radius:3px}
.wrap0{max-width:1280px;margin:0 auto;padding:0 16px}@media(min-width:1000px){.wrap0{padding:0 40px}}
.wrap{max-width:1280px;margin:0 auto;padding:0 16px;display:block}
@media(min-width:1000px){.wrap{display:grid;grid-template-columns:240px minmax(0,1fr);gap:56px;padding:0 40px}}
/* masthead */
.mast{padding:40px 0 32px;border-bottom:1px solid var(--ink)}
.kicker{font:500 12px/1.4 'JetBrains Mono',monospace;letter-spacing:.08em;text-transform:uppercase;color:var(--ink2);display:flex;flex-wrap:wrap;gap:6px 18px}
.mast h1{font-family:'Unbounded',sans-serif;font-weight:900;font-size:clamp(40px,8.4vw,112px);line-height:.92;letter-spacing:-.035em;margin:18px 0 0}
.mast h1 em{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:500;letter-spacing:-.01em;color:var(--acc)}
.mast .intro{max-width:640px;font-size:19px;margin:22px 0 0;color:var(--ink2)}
.mast .scrib{font-family:'Caveat',cursive;font-size:26px;color:var(--acc);transform:rotate(-2deg);display:inline-block;margin-top:10px}
/* toc */
.toc{position:relative}
.toc-inner{padding:28px 0 8px}
@media(min-width:1000px){.toc-inner{position:sticky;top:0;max-height:100vh;overflow:auto;padding:40px 0}}
.toc h2{font:600 12px 'JetBrains Mono',monospace;letter-spacing:.1em;text-transform:uppercase;color:var(--ink2);margin:0 0 10px}
.toc ol{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:0 16px}
@media(min-width:1000px){.toc ol{grid-template-columns:1fr}}
.toc a{display:flex;gap:10px;padding:7px 0;border-bottom:1px solid var(--line);text-decoration:none;font-size:15px;line-height:1.3}
.toc a span{font:12px/1.6 'JetBrains Mono',monospace;color:var(--ink2);min-width:20px}
.toc a.on{color:var(--acc)} .toc a.on span{color:var(--acc)}
.toc .meta{font:12px/1.5 'JetBrains Mono',monospace;color:var(--ink2);margin-top:18px}
.theme{margin-top:14px;font:12px 'JetBrains Mono',monospace;background:none;border:1px solid var(--line);color:var(--ink);padding:6px 10px;cursor:pointer;border-radius:2px}
main{min-width:0}
/* sections */
.sec{padding:56px 0 24px;border-bottom:1px solid var(--line)}
.sec-head{margin-bottom:28px}
.sec-num{font:700 13px 'JetBrains Mono',monospace;color:var(--acc);letter-spacing:.06em}
.sec h2{font-family:'Unbounded',sans-serif;font-weight:700;font-size:clamp(28px,4.2vw,48px);line-height:1.02;letter-spacing:-.025em;margin:6px 0 12px;max-width:900px}
.lead{font-size:19px;color:var(--ink2);max-width:720px;margin:0}
h3.sub{font-family:'Unbounded',sans-serif;font-size:20px;font-weight:700;letter-spacing:-.01em;margin:40px 0 14px}
h4{font:600 12px/1.4 'JetBrains Mono',monospace;letter-spacing:.08em;text-transform:uppercase;color:var(--ink2);margin:0 0 8px}
h4.ok{color:var(--ok)} h4.no{color:var(--acc);margin-top:16px}
.muted{color:var(--ink2);font-size:15px}
.note{border-left:3px solid var(--acc);padding:4px 0 4px 16px;margin:24px 0;font-size:16px}
/* chips */
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 28px}
.chips a{font-size:14px;text-decoration:none;border:1px solid var(--line);padding:5px 11px;border-radius:999px;background:var(--paper)}
.chips a:hover{border-color:var(--acc)}
/* trend */
.trend{background:var(--paper);border:1px solid var(--line);padding:24px 20px;margin:0 0 20px;scroll-margin-top:16px}
@media(min-width:700px){.trend{padding:32px 36px}}
.trend-top{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 14px;margin-bottom:8px}
.tnum{font:700 13px 'JetBrains Mono',monospace;color:var(--acc)}
.trend h3{font-family:'Unbounded',sans-serif;font-size:clamp(22px,2.6vw,30px);font-weight:700;letter-spacing:-.02em;margin:0;line-height:1.1}
.tshort{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:22px;color:var(--ink2)}
.trend>p{max-width:760px;margin:6px 0 20px}
.trend-grid{display:grid;gap:20px;border-top:1px solid var(--line);padding-top:18px}
@media(min-width:760px){.trend-grid{grid-template-columns:1fr 1fr;gap:36px}}
.trend-grid p{margin:0;font-size:16px}
ul.dots{margin:0;padding:0;list-style:none;font-size:16px}
ul.dots li{padding-left:18px;position:relative;margin:0 0 5px}
ul.dots li::before{content:"";position:absolute;left:2px;top:.62em;width:7px;height:7px;background:var(--acc);border-radius:50%}
.refs{margin-top:20px;border-top:1px solid var(--line);padding-top:16px}
.refs ul{list-style:none;margin:0;padding:0;display:grid;gap:6px}
@media(min-width:760px){.refs ul{grid-template-columns:1fr 1fr;column-gap:36px}}
.refs li{font-size:15px;line-height:1.4;display:flex;flex-direction:column}
.host{font:11px 'JetBrains Mono',monospace;color:var(--ink2)}
.to-prompt{display:inline-block;margin-top:18px;font:600 13px 'JetBrains Mono',monospace;color:var(--acc)}
/* rows */
.rows{margin:0;border-top:1px solid var(--ink)}
.row{display:grid;gap:2px 24px;padding:12px 0;border-bottom:1px solid var(--line)}
@media(min-width:700px){.row{grid-template-columns:220px 1fr}}
.row dt{font-weight:600}
.row dd{margin:0;color:var(--ink2);font-size:16px}
/* libs */
.libs{display:grid;gap:12px}
@media(min-width:760px){.libs{grid-template-columns:1fr 1fr}}
.lib{background:var(--paper);border:1px solid var(--line);padding:18px 20px}
.lib-top{display:flex;justify-content:space-between;gap:10px;align-items:baseline}
.lib h4{font:700 17px 'Onest',sans-serif;letter-spacing:0;text-transform:none;color:var(--ink);margin:0 0 6px}
.lvl{font:11px 'JetBrains Mono',monospace;color:var(--ink2);white-space:nowrap;border:1px solid var(--line);padding:2px 6px}
.lib p{margin:0 0 6px;font-size:15px}
/* reactbits */
ol.rb{list-style:none;margin:0;padding:0;border-top:1px solid var(--ink);counter-reset:rb}
ol.rb li{counter-increment:rb;display:grid;grid-template-columns:34px 1fr;gap:0 10px;padding:10px 0;border-bottom:1px solid var(--line)}
ol.rb li::before{content:counter(rb,decimal-leading-zero);font:12px/1.9 'JetBrains Mono',monospace;color:var(--ink2);grid-row:span 2}
@media(min-width:760px){ol.rb li{grid-template-columns:34px 190px 130px 1fr}ol.rb li::before{grid-row:auto}}
.rb-name{font-weight:600}
.rb-cat{font:11px/2 'JetBrains Mono',monospace;color:var(--ink2)}
.rb-what{color:var(--ink2);font-size:15px;grid-column:2/-1}
@media(min-width:760px){.rb-what{grid-column:auto}}
/* fonts */
.fonts{display:grid;gap:10px}
@media(min-width:600px){.fonts{grid-template-columns:1fr 1fr}}
@media(min-width:1200px){.fonts{grid-template-columns:1fr 1fr 1fr}}
.font{display:flex;gap:14px;align-items:center;background:var(--paper);border:1px solid var(--line);padding:12px 14px}
.specimen{font-size:30px;line-height:1;width:64px;flex:none;white-space:nowrap;overflow:hidden;text-align:center}
.font a{font-weight:600}
.font p{margin:2px 0 0;font-size:14px;color:var(--ink2);line-height:1.35}
ol.steps-s{padding-left:22px;margin:0}
ol.steps-s li{margin:0 0 10px;padding-left:4px}
ol.steps-s li::marker{font-family:'JetBrains Mono',monospace;color:var(--acc);font-size:14px}
/* anti-ai */
ol.aic{list-style:none;margin:0;padding:0;counter-reset:a}
ol.aic li{counter-increment:a;display:grid;gap:4px 28px;padding:14px 0;border-bottom:1px solid var(--line)}
@media(min-width:760px){ol.aic li{grid-template-columns:1fr 1fr}}
ol.aic label{display:flex;gap:12px;cursor:pointer;font-weight:600}
ol.aic label::before{content:counter(a,decimal-leading-zero);font:12px/1.9 'JetBrains Mono',monospace;color:var(--ink2);order:-2}
ol.aic .fix{color:var(--ink2);font-size:16px;padding-left:46px}
@media(min-width:760px){ol.aic .fix{padding-left:0}}
ol.aic input:checked+.bad{text-decoration:line-through;text-decoration-color:var(--acc);text-decoration-thickness:2px}
input[type=checkbox]{appearance:none;-webkit-appearance:none;flex:none;width:20px;height:20px;border:1.5px solid var(--ink);border-radius:2px;margin:3px 0 0;background:var(--paper);display:grid;place-content:center;cursor:pointer;order:-1}
input[type=checkbox]::after{content:"";width:11px;height:6px;border-left:2.5px solid var(--acc);border-bottom:2.5px solid var(--acc);transform:rotate(-45deg) translate(1px,-1px) scale(0);transition:transform .15s}
input[type=checkbox]:checked::after{transform:rotate(-45deg) translate(1px,-1px) scale(1)}
input[type=checkbox]:focus-visible{outline:2px solid var(--acc2);outline-offset:2px}
/* evening */
ol.evening{list-style:none;margin:0;padding:0;counter-reset:e;border-left:1px solid var(--ink);margin-left:14px}
ol.evening li{counter-increment:e;position:relative;padding:0 0 22px 30px}
ol.evening li::before{content:counter(e);position:absolute;left:-15px;top:0;width:30px;height:30px;border-radius:50%;background:var(--bg);border:1px solid var(--ink);font:700 13px/28px 'JetBrains Mono',monospace;text-align:center}
ol.evening h4{font:700 18px/1.3 'Onest',sans-serif;text-transform:none;letter-spacing:0;color:var(--ink);margin:2px 0 4px}
ol.evening p{margin:0;font-size:16px;max-width:760px}
/* prompts */
.tpl{background:var(--paper);border:1px dashed var(--ink2);padding:12px 16px;margin-bottom:20px}
.tpl summary{cursor:pointer;font-weight:600}
pre{font:13.5px/1.6 'JetBrains Mono',monospace;white-space:pre-wrap;word-break:break-word;margin:10px 0 0;color:var(--ink)}
.prompt{border:1px solid var(--line);background:var(--paper);margin:0 0 14px;scroll-margin-top:16px}
.prompt-top{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:12px 16px;border-bottom:1px solid var(--line)}
.prompt h3{font:700 16px 'Onest',sans-serif;margin:0}
.prompt pre{margin:0;padding:14px 16px 18px;background:var(--code)}
.copy,.reset{font:600 12px 'JetBrains Mono',monospace;border:1px solid var(--ink);background:var(--ink);color:var(--bg);padding:7px 12px;cursor:pointer;border-radius:2px;white-space:nowrap}
.copy.done{background:var(--ok);border-color:var(--ok)}
.reset{background:none;color:var(--ink2);border-color:var(--line);margin-top:12px}
/* checklists */
.cls{display:grid;gap:16px}
@media(min-width:900px){.cls{grid-template-columns:1fr 1fr}}
.cl{background:var(--paper);border:1px solid var(--line);padding:20px}
.cl-top{display:flex;justify-content:space-between;align-items:baseline;gap:10px;margin-bottom:8px}
.cl h3{font-family:'Unbounded',sans-serif;font-size:17px;margin:0}
.cnt{font:12px 'JetBrains Mono',monospace;color:var(--acc)}
.cl ul{list-style:none;margin:0;padding:0}
.cl li{border-bottom:1px solid var(--line)}
.cl label{display:flex;gap:12px;padding:9px 0;font-size:15.5px;line-height:1.45;cursor:pointer}
.cl input:checked+span{color:var(--ink2)}
/* glossary */
.gloss{margin:0;display:grid;gap:0 40px}
@media(min-width:760px){.gloss{grid-template-columns:1fr 1fr}}
.gloss div{padding:10px 0;border-bottom:1px solid var(--line)}
.gloss dt{font-weight:700;display:inline}
.gloss dt::after{content:": "}
.gloss dd{display:inline;margin:0;color:var(--ink2);font-size:16px}
footer.end{padding:40px 0 60px;font:13px/1.6 'JetBrains Mono',monospace;color:var(--ink2)}
.top{position:fixed;right:16px;bottom:16px;width:44px;height:44px;border-radius:50%;border:1px solid var(--ink);background:var(--paper);color:var(--ink);cursor:pointer;display:grid;place-items:center;opacity:0;pointer-events:none;transition:opacity .2s}
.top.show{opacity:1;pointer-events:auto}
@media print{.toc,.copy,.reset,.top,.theme{display:none}.wrap{display:block}.trend,.prompt,.cl{break-inside:avoid}}
'''

JS=r'''
(function(){
var store={get:function(k){try{return localStorage.getItem(k)}catch(e){return null}},set:function(k,v){try{localStorage.setItem(k,v)}catch(e){}},del:function(k){try{localStorage.removeItem(k)}catch(e){}}};
var P='guide26:';
document.querySelectorAll('input[type=checkbox][data-k]').forEach(function(c){
  if(store.get(P+c.dataset.k)==='1')c.checked=true;
  c.addEventListener('change',function(){c.checked?store.set(P+c.dataset.k,'1'):store.del(P+c.dataset.k);count()});
});
function count(){document.querySelectorAll('.cl').forEach(function(cl){var all=cl.querySelectorAll('input'),on=cl.querySelectorAll('input:checked');cl.querySelector('.cnt').textContent=on.length+' / '+all.length})}
count();
document.querySelectorAll('.reset').forEach(function(b){b.addEventListener('click',function(){b.closest('.cl').querySelectorAll('input').forEach(function(c){c.checked=false;store.del(P+c.dataset.k)});count()})});
function selectText(el){var r=document.createRange();r.selectNodeContents(el);var s=window.getSelection();s.removeAllRanges();s.addRange(r)}
document.querySelectorAll('.copy').forEach(function(b){b.addEventListener('click',function(){
  var pre=b.closest('.prompt').querySelector('pre'),t=pre.textContent;
  function ok(){b.textContent='Скопировано';b.classList.add('done');setTimeout(function(){b.textContent='Скопировать';b.classList.remove('done')},1800)}
  function fallback(){selectText(pre);var done=false;try{done=document.execCommand('copy')}catch(e){}if(done)ok();else b.textContent='Выделено: Ctrl+C'}
  if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(t).then(ok,fallback)}else fallback();
})});
var links=[].slice.call(document.querySelectorAll('.toc a'));
var map={};links.forEach(function(l){map[l.getAttribute('href').slice(1)]=l});
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){links.forEach(function(l){l.classList.remove('on')});var l=map[e.target.id];if(l)l.classList.add('on')}})},{rootMargin:'-30% 0px -65% 0px'});
document.querySelectorAll('section.sec').forEach(function(s){io.observe(s)})}
var top=document.querySelector('.top');window.addEventListener('scroll',function(){top.classList.toggle('show',window.scrollY>900)},{passive:true});
top.addEventListener('click',function(){window.scrollTo(0,0)});
var th=document.querySelector('.theme');var saved=store.get(P+'theme');if(saved)document.documentElement.setAttribute('data-theme',saved);
th.addEventListener('click',function(){var cur=document.documentElement.getAttribute('data-theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');var n=cur==='dark'?'light':'dark';document.documentElement.setAttribute('data-theme',n);store.set(P+'theme',n)});
})();
'''

page=f'''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Сайты и лендинги 2026</title>
<meta name="description" content="Гайдбук-памятка для маркетологов: тренды, галереи, анимации, шрифты, ассеты, анти-ИИ чек-лист, лендинг за вечер, промпты, чек-листы и словарь.">
<link rel="stylesheet" href="../assets/fonts/fonts.css">
<style>{CSS}</style>
</head>
<body>
<div class="wrap0"><header class="mast">
<div class="kicker"><span>Гайдбук к лекции</span><span>Для маркетологов</span><span>Версия {CHECKED}</span></div>
<h1>Сайты и лендинги <em>в&nbsp;2026</em></h1>
<p class="intro">Справочник, к которому можно вернуться после лекции: какие стили сейчас работают, где брать референсы, шрифты и фото, как собрать лендинг с нейросетью за вечер и не получить очередной ИИ-шаблон.</p>
<span class="scrib">сделано руками, проверено вручную</span>
</header>
</div>
<div class="wrap">
<aside class="toc"><div class="toc-inner">
<h2>Содержание</h2>
<ol>{toc}</ol>
<div class="meta">Ссылки проверены {CHECKED}<br>{len(links)} ссылок</div>
<button class="theme" type="button">Светлая / темная</button>
</div></aside>
<main>
{''.join(H)}
<footer class="end">Все ссылки открывались {CHECKED}. Сайты меняются: если ссылка не работает, ищите проект по названию.</footer>
</main>
</div>
<button class="top" type="button" aria-label="Наверх"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 10l5-5 5 5"/></svg></button>
<script>{JS}</script>
</body>
</html>'''
open('/home/claude/kit/guide/index.html','w').write(page)

# ---------- README.md ----------
M=[]
M.append(f"# Сайты и лендинги в 2026\n\nГайдбук-памятка к лекции для маркетологов. Ссылки проверены {CHECKED}.\n")
M.append("## Содержание\n\n"+"\n".join(f"{n}. {t}" for n,(i,t) in enumerate(SECTIONS,1))+"\n")
m=f"## 1. Тренды 2026 и где смотреть живые примеры\n"
for n,t in enumerate(TRENDS,1):
    m+=f"\n### 1.{n}. {t['name']}\n\n*{t['short']}.* {t['what']}\n\n**Признаки:**\n\n"+"\n".join(f"* {x}" for x in t['signs'])
    m+=f"\n\n**Когда использовать:** {t['use']}\n\n**Когда не использовать:** {t['dont']}\n\n**Референсы:**\n\n"+"\n".join(f"* [{r[0]}]({r[1]})" for r in t['refs'])+"\n"
M.append(m)
M.append("## 2. Галереи и источники вдохновения\n\n"+"\n".join(f"* [{g[0]}]({g[1]}): {g[2]}" for g in GALLERIES)+"\n")
m="## 3. Анимации и микроанимации\n\n### Библиотеки\n\n| Библиотека | Что это | Сложность | Для чего |\n|---|---|---|---|\n"
m+="\n".join(f"| [{l[0]}]({l[1]}) | {l[2]} | {l[3]} | {l[4]} |" for l in LIBS)
m+="\n\nФакт про GSAP: [блог Webflow](https://webflow.com/blog/gsap-becomes-free), [релиз GSAP 3.13](https://gsap.com/blog/3-13/).\n\n"
m+=f"### React Bits: {len(REACTBITS)} компонентов для лендингов\n\n"+"\n".join(f"{i}. [{r[0]}](https://reactbits.dev/{r[1]}) ({r[1].split('/')[0]}): {r[2]}" for i,r in enumerate(REACTBITS,1))+"\n"
M.append(m)
m="## 4. Шрифты с кириллицей\n\n### Бесплатные (Google Fonts, OFL)\n\n"+"\n".join(f"* [{f[0]}]({f[1]}): {f[2]}" for f in FONTS_FREE)
m+="\n\nПодборка: [Typewolf: Google Fonts](https://www.typewolf.com/google-fonts).\n\n### Словолитни\n\n"+"\n".join(f"* [{f[0]}]({f[1]}): {f[2]}" for f in FOUNDRIES)
m+="\n\n### Как проверить лицензию\n\n1. Google Fonts: [SIL Open Font License](https://openfontlicense.org/) или Apache, можно в коммерции. Нельзя продавать сам шрифт.\n2. Платные словолитни: desktop, web, app, logo. Для сайта нужна web-лицензия.\n3. Скачанный с файлообменника шрифт это не лицензия.\n4. Для логотипа уточните право на товарный знак.\n5. Сохраните чек или скрин лицензии.\n\n### Пары шрифтов\n\n"+"\n".join(f"* **{p[0]}:** {p[1]}" for p in PAIRS)+"\n"
M.append(m)
m="## 5. Фото, иллюстрации и ассеты\n\n### Фото и архивы\n\n"+"\n".join(f"* [{p[0]}]({p[1]}): {p[2]}" for p in PHOTO)
m+="\n\n### Текстуры, 3D, иконки, логотипы\n\n"+"\n".join(f"* [{p[0]}]({p[1]}): {p[2]}" for p in ASSETS3D)
m+="\n\n### Как сделать визуал «анти-ИИ»\n\n"+"\n".join(f"{i}. {x}" for i,x in enumerate(ANTIAI_VISUAL,1))+"\n"
M.append(m)
M.append("## 6. Анти-ИИ чек-лист\n\n| # | Признак | Что делать вместо |\n|---|---|---|\n"+"\n".join(f"| {i} | {b} | {f} |" for i,(b,f) in enumerate(ANTIAI_CHECK,1))+"\n")
M.append("## 7. Памятка «Лендинг за вечер»\n\n"+"\n".join(f"{i}. **{e[0]}.** {e[1]}" for i,e in enumerate(EVENING,1))+"\n")
m="## 8. Промпты по стилям\n\n"+PALETTE_NOTE+"\n\nШаблон всего промпта:\n\n```\nСделай одностраничный лендинг на русском языке для [бизнес, город].\nАудитория: [кто]. Оффер: [что, за сколько, к какому сроку].\nБлоки: hero с оффером и одной кнопкой, проблема, решение, цены, отзывы, FAQ, форма заявки (имя, телефон, отдельный чекбокс согласия на обработку персональных данных со ссылкой на политику), футер с контактами.\nМобильная версия в приоритете, без горизонтального скролла.\n[ВСТАВЬ БЛОК СТИЛЯ НИЖЕ]\n```\n"
for t in TRENDS: m+=f"\n### {t['name']}\n\n```\n{PROMPTS[t['id']]}\n```\n"
M.append(m)
m="## 9. Чек-листы\n"
for k,(title,items) in CHECKLISTS.items(): m+=f"\n### {title}\n\n"+"\n".join(f"- [ ] {x}" for x in items)+"\n"
m+="\nПервоисточники: [152-ФЗ на КонсультантПлюс](https://www.consultant.ru/document/cons_doc_LAW_61801/), [Core Web Vitals](https://web.dev/articles/vitals). Это памятка, а не юридическая консультация.\n"
M.append(m)
M.append("## 10. Словарь терминов\n\n"+"\n".join(f"* **{g[0]}:** {g[1]}" for g in GLOSSARY)+"\n")
M.append(f"---\n\nВсе ссылки открывались {CHECKED}.\n")
open('/home/claude/kit/guide/README.md','w').write("\n".join(M))
print("links",len(links))
