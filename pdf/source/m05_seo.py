# -*- coding: utf-8 -*-
from base import page, doc, md, checklist
import guide_content as G

R = 'Памятка 05 · Скорость и SEO'
SPEED = [
 "Фото в WebP или AVIF, ширина не больше, чем на экране (обычно до 1600 px)",
 "Фото со смартфона сжаты: в Squoosh или TinyPNG, 100-300 КБ вместо 5 МБ",
 "Lazy loading у картинок ниже первого экрана",
 "Не больше 2-3 начертаний шрифта, `font-display: swap`",
 "Видео встроено с Rutube или VK Видео, а не загружено файлом",
 "Минимум сторонних виджетов: каждый чат, пиксель и счетчик замедляет",
 "Хостинг рядом с аудиторией, для России сервер в России",
 "Проверено в PageSpeed Insights на мобильном, оценка от 90",
]

def gauge(val, label, sub, pct, col):
    return f'''<div style="display:flex;flex-direction:column;align-items:flex-start;gap:2mm">
<div style="width:30mm;height:30mm;border-radius:50%;background:conic-gradient({col} {pct}%,#d7d7d0 0);display:grid;place-items:center;position:relative">
<div style="position:absolute;inset:3mm;border-radius:50%;background:var(--paper)"></div><b style="position:relative;font:800 13pt var(--fd)">{val}</b></div>
<b style="font:700 11pt var(--fd)">{label}</b><span class="muted" style="font-size:8.5pt">{sub}</span></div>'''

def build():
    p1 = f'''<p class="kick">Памятка 05 из 08</p>
<h1 style="font-size:54pt">Скорость и SEO</h1>
<p class="lead" style="margin-bottom:7mm">Медленный сайт теряет людей до того, как они увидят оффер. SEO дает бесплатный трафик годами, реклама работает, только пока платите.</p>
<div style="display:flex;justify-content:space-between;margin-bottom:7mm">
 {gauge('90+','PageSpeed','на телефоне',92,'#1a8f4a')}
 {gauge('2,5 с','LCP','главный блок загрузился',70,'var(--blue)')}
 {gauge('200 мс','INP','реакция на нажатие',55,'var(--blue)')}
 {gauge('0,1','CLS','верстка не прыгает',20,'var(--signal)')}
</div>
<div class="g2" style="gap:7mm">
 <div class="sec"><h3><b>01</b>Чек-лист скорости</h3>{checklist(SPEED)}</div>
 <div>
  <p class="kick">Промпт</p>
  <pre class="prompt" style="margin-bottom:5mm">Оптимизируй сайт под PageSpeed:
переведи картинки в <em>WebP</em>, добавь
<em>lazy loading</em>, оставь 2 начертания
шрифтов с font-display: swap, убери
неиспользуемый код, проверь LCP и CLS
на мобильном.</pre>
  <div class="cell"><span class="k">Инструменты</span><p><a href="https://pagespeed.web.dev/">PageSpeed Insights</a> · <a href="https://squoosh.app/">Squoosh</a> · <a href="https://tinypng.com/">TinyPNG</a></p></div>
  <div class="box ink" style="margin-top:4mm"><p style="margin:0"><b>Главная причина медленных сайтов:</b> фото с телефона по 5 МБ прямо на первом экране.</p></div>
 </div>
</div>'''
    p2 = f'''<div class="g2" style="gap:7mm">
 <div>
  <h2>SEO-минимум</h2>
  <div style="background:#fff;padding:5mm;box-shadow:0 2mm 8mm rgba(0,0,0,.08);font-family:Arial,sans-serif;margin-bottom:2mm">
   <div style="font-size:8pt;color:#1a7f37">kofe-vl.ru › menu</div>
   <div style="font-size:12pt;color:#1a0dab;margin:1mm 0">Кофейня во Владивостоке на Светланской | Кофе с собой</div>
   <div style="font-size:8.5pt;color:#333;line-height:1.4">Свежая обжарка каждый четверг. Фильтр от 180 ₽, завтраки до 12:00. Закажите онлайн и заберите без очереди.</div>
  </div>
  <div style="display:flex;justify-content:space-between;margin-bottom:5mm"><span class="hand" style="font-size:13pt">title: до 60 символов</span><span class="hand" style="font-size:13pt">description: до 160</span></div>
  {checklist(G.CHECKLISTS['seo'][1])}
 </div>
 <div>
  <h2>Россия и GEO</h2>
  <div class="cell" style="margin-bottom:4mm"><span class="k">Яндекс</span><p>Главный поисковик страны. Добавьте сайт в Яндекс Вебмастер и Google Search Console, отправьте sitemap. Для локального бизнеса карточка в Яндекс Бизнесе и на Картах бывает важнее сайта.</p></div>
  <div class="box lime" style="margin-bottom:4mm"><div class="big-num">42%</div><p style="margin:2mm 0 0">запросов в Яндексе во II квартале 2026 получали ответ Алисы AI прямо под строкой поиска, это 49,5 млн человек в месяц. <span class="muted">По данным Яндекса в публикации TenChat.</span></p></div>
  <p class="kick">Чтобы нейросеть цитировала ваш сайт</p>
  {checklist(["Блок FAQ с четкими ответами на конкретные вопросы","Факты и цифры вместо общих слов","Подзаголовки и микроразметка Schema.org: организация, FAQ","Упоминания бренда на других площадках: карты, СМИ, каталоги","Видимость сайта в ответах Алисы AI смотрите в Вебмастере"])}
  <div class="box ink" style="margin-top:4mm"><p style="margin:0"><b>SPA и поиск.</b> Lovable и AI Studio делают SPA. Если важен поисковый трафик, проверьте в Вебмастере, видит ли робот текст. Нет: попросите пререндеринг или Astro.</p></div>
 </div>
</div>'''
    return doc('Скорость и SEO', [page(p1, R, 'Скорость', 1, 2), page(p2, R, 'Поиск', 2, 2)])
