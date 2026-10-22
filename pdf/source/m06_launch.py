# -*- coding: utf-8 -*-
from base import page, doc, md, checklist
import guide_content as G

R = 'Памятка 06 · Запуск в России'
PLAT = [
 ("Lovable, AI Studio, ChatGPT Sites", "встроено", "Зарубежные: доступ и оплата из РФ ограничены", "warn"),
 ("Vercel, Netlify", "бесплатно", "Свой домен часто не открывается с мобильного интернета без VPN", "bad"),
 ("Cloudflare Pages", "бесплатно", "С июня 2025 провайдеры пропускают только первые 16 КБ", "bad"),
 ("GitHub Pages", "бесплатно", "Обычно стабильнее, только статика", "warn"),
 ("Timeweb Cloud, Beget, Рег.ру, Selectel, Яндекс Облако", "от 0 ₽", "Серверы в РФ, оплата картой, поддержка на русском", "ok"),
]
DEPLOY = [
 ("Скачайте код", "Экспорт или синхронизация с GitHub в Lovable и AI Studio."),
 ("Соберите", "`npm run build` создаст папку `dist`. Не умеете: попросите нейросеть объяснить по шагам для вашего хостинга."),
 ("Загрузите", "Содержимое `dist` в панель хостинга или подключите GitHub-репозиторий."),
 ("Привяжите домен", "У регистратора укажите DNS хостинга. Обновление от минут до суток."),
 ("Включите HTTPS", "Бесплатный сертификат Let's Encrypt в панели хостинга."),
 ("Проверьте", "Откройте с мобильного интернета двух операторов без VPN."),
]

def build():
    col = {'ok': 'var(--blue)', 'warn': '#B08000', 'bad': 'var(--signal)'}
    rows = ''.join(f'<tr><td><b>{a}</b></td><td class="mono" style="font-size:8pt">{b}</td><td style="color:{col[c]}">{d}</td></tr>' for a, b, d, c in PLAT)
    dep = ''.join(f'<div class="cell"><span class="k">{i+1:02d}</span><b style="font-size:9.5pt">{h}</b><p style="font-size:8.3pt;margin-top:1mm">{md(x)}</p></div>' for i,(h, x) in enumerate(DEPLOY))
    p1 = f'''<p class="kick">Памятка 06 из 08</p>
<h1 style="font-size:44pt">Запуск в России</h1>
<p class="lead" style="margin-bottom:5mm;font-size:12pt">Чтобы сайт увидели, нужны адрес, место для файлов и публикация. В России к этому добавляются блокировки зарубежных платформ и закон о персональных данных.</p>
<div style="display:grid;grid-template-columns:1fr 8mm 1fr 8mm 1fr;align-items:stretch;margin-bottom:6mm">
 <div class="box lime"><h3>Домен</h3><p class="mono" style="font-size:8pt;margin:0">kofe-vl.ru</p><p style="font-size:8.5pt;margin:1.5mm 0 0">адрес, аренда на год</p></div>
 <svg viewBox="0 0 30 20" style="width:8mm;align-self:center"><path d="M2 10 H26 M20 4 L27 10 L20 16" fill="none" stroke="#121212" stroke-width="2.2"/></svg>
 <div class="box"><h3>DNS</h3><p class="mono" style="font-size:8pt;margin:0">домен = IP сервера</p><p style="font-size:8.5pt;margin:1.5mm 0 0">телефонная книга интернета</p></div>
 <svg viewBox="0 0 30 20" style="width:8mm;align-self:center"><path d="M2 10 H26 M20 4 L27 10 L20 16" fill="none" stroke="#121212" stroke-width="2.2"/></svg>
 <div class="box blue"><h3>Хостинг</h3><p class="mono" style="font-size:8pt;margin:0">файлы сайта</p><p style="font-size:8.5pt;margin:1.5mm 0 0">дом, где он живет</p></div>
</div>
<div class="g2" style="gap:6mm;margin-bottom:5mm">
 <div class="cell"><span class="k">Где купить .ru и .рф</span><p>У аккредитованных регистраторов, список на <a href="https://cctld.ru/">cctld.ru</a>. Крупнейшие: Рег.ру и RU-CENTER.</p></div>
 <div class="cell"><span class="k">Ловушка цены</span><p>Рег.ру с января 2026: регистрация .ru 129 ₽ по акции, продление 999 ₽ в год. Смотрите цену продления до покупки.</p></div>
</div>
<h3>Где разместить сайт для аудитории в России</h3>
<table class="vs" style="margin-bottom:5mm"><tr><th>Платформа</th><th>Цена</th><th>Для России, проверено 21.10.2026</th></tr>{rows}</table>
<h3>Деплой на российский хостинг</h3>
<div class="g3" style="gap:3mm 5mm">{dep}</div>'''
    p2 = f'''<div class="g2" style="gap:7mm">
 <div>
  <h2>152-ФЗ</h2>
  <p style="font-size:9.3pt">Любая форма с именем и телефоном делает владельца сайта оператором персональных данных. С 30 мая 2025 штрафы выросли до сотен тысяч рублей, с 1 сентября 2025 согласие оформляется отдельно от других документов.</p>
  <div style="background:#fff;padding:5mm;box-shadow:0 2mm 8mm rgba(0,0,0,.08);margin:3mm 0 5mm;display:flex;flex-direction:column;gap:2.5mm">
   <b style="font:800 11pt var(--fd)">Запись на стрижку</b>
   <div style="border:.8pt solid var(--line);padding:2.5mm;font-size:9pt;color:var(--ink2)">Имя</div>
   <div style="border:.8pt solid var(--line);padding:2.5mm;font-size:9pt;color:var(--ink2)">+7 (___) ___-__-__</div>
   <div style="display:flex;gap:2.5mm;font-size:8pt;outline:1.4pt solid var(--signal);outline-offset:1.5mm"><i style="flex:none;width:3.8mm;height:3.8mm;border:1pt solid var(--ink)"></i><span>Согласен на обработку персональных данных и с <u>политикой конфиденциальности</u></span></div>
   <div style="background:var(--ink);color:#fff;text-align:center;padding:2.8mm;font:700 9.5pt var(--ft);margin-top:1.5mm">Записаться</div>
   <span class="hand" style="align-self:flex-end;font-size:12pt">галочку ставит сам человек</span>
  </div>
  {checklist(G.CHECKLISTS['pd'][1][:8])}
  <p class="muted" style="font-size:7.5pt;margin-top:3mm">Это памятка, а не юридическая консультация. Для реального бизнеса покажите документы юристу.</p>
 </div>
 <div>
  <h2>Перед рекламой</h2>
  {checklist(G.CHECKLISTS['ads'][1])}
  <div class="box ink" style="margin-top:5mm"><p class="kick" style="color:var(--lime);opacity:1">Заявки в Telegram</p>
  <p style="margin:0">Создайте бота через @BotFather, получите токен и chat_id. Попросите нейросеть сделать отправку формы через серверную функцию. Токен никогда не должен лежать в коде страницы.</p></div>
  <div class="cell" style="margin-top:5mm"><span class="k">Аналитика</span><p>Яндекс Метрика: счетчик на все страницы, цель «отправка формы», Вебвизор. UTM-метки на каждом объявлении: utm_source, utm_medium, utm_campaign.</p></div>
 </div>
</div>'''
    return doc('Запуск в России', [page(p1, R, 'Домен и хостинг', 1, 2), page(p2, R, 'Закон и реклама', 2, 2)])
