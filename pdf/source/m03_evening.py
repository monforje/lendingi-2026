# -*- coding: utf-8 -*-
from base import page, doc, md

R = 'Памятка 03 · Лендинг за вечер'
Q = [("Что продаем?", "Продукт или услуга одной фразой"),
     ("Кому?", "Кто клиент, сколько лет, чего хочет, чего боится"),
     ("Почему у нас?", "Отличие от конкурентов, факты"),
     ("Что человек должен сделать?", "Записаться, позвонить, купить, оставить почту"),
     ("Какое настроение у бренда?", "")]
MOODS = ["строгое", "дерзкое", "уютное", "премиальное", "детское", "техно", "романтичное", "панковское"]
PLAN = [
 ("18:00", "20 мин", "Бриф", "Ответьте на 5 вопросов на первой странице. Соберите свои фото, цены, адрес."),
 ("18:20", "20 мин", "ТЗ через нейросеть", "Вставьте ответы в ChatGPT, GigaChat или Алису AI с промптом 0. Уберите воду, добавьте свои цифры."),
 ("18:40", "20 мин", "Стиль и референсы", "Выберите один тренд из памятки 04, возьмите его блок стиля. 3-5 референсов из Awwwards или Siteinspire."),
 ("19:00", "30 мин", "Генерация", "Lovable или Google AI Studio, промпт 1. Пока генерируется, пишите тексты отзывов и FAQ из реальных вопросов."),
 ("19:30", "45 мин", "Правки", "Одна правка в одном сообщении. После каждой смотрите на телефоне."),
 ("20:15", "30 мин", "Реальный контент", "Свои фото, цены, имена, отзывы со скриншотами. Удалите выдуманное."),
 ("20:45", "30 мин", "Форма и заявки", "Чекбокс согласия, политика, отправка в Telegram через серверную функцию."),
 ("21:15", "30 мин", "Домен и хостинг", "Домен .ru у аккредитованного регистратора, российский хостинг, HTTPS."),
 ("21:45", "15 мин", "Аналитика", "Яндекс Метрика с целью на форму, сайт в Яндекс Вебмастер."),
 ("22:00", "30 мин", "Проверка и запуск", "Чек-лист из памятки 02, тестовая заявка с телефона, UTM-метки на рекламу."),
]
P0 = """Ты опытный маркетолог. Вот ответы клиента о бизнесе:
что продаем: <em>[...]</em> · кому: <em>[...]</em> · почему у нас: <em>[...]</em>
действие: <em>[...]</em> · настроение: <em>[...]</em>
Сделай ТЗ на одностраничный лендинг: 3 варианта заголовка
(выбери лучший), блоки сверху вниз с текстами на русском,
палитра в HEX, шрифты Google Fonts с кириллицей, текст
кнопок, поля формы. Без воды. Оформи как готовый промпт."""
P1 = """Создай современный одностраничный продающий лендинг на русском.
БИЗНЕС: <em>[название, что продаем, город]</em>
АУДИТОРИЯ: <em>[кто клиент, чего хочет, чего боится]</em>
ОТЛИЧИЕ: <em>[УТП]</em>  ДЕЙСТВИЕ: <em>[записаться / купить]</em>
СТИЛЬ: <em>[блок стиля из памятки 04]</em>
СТРУКТУРА: шапка, первый экран с оффером и кнопкой, цифры
доверия, боли, услуги с ценами, 4 шага, отзывы, FAQ, форма
(имя, телефон, обязательный чекбокс согласия на обработку
персональных данных со ссылкой на политику), футер.
Mobile first. SEO: title, description, Open Graph, один H1.
Не используй фиолетовые градиенты, Inter, эмодзи, иконки в
кружках, три одинаковые карточки."""
EDITS = [
 ("Дизайн", "Сделай дороже: больше воздуха между блоками, заголовки крупнее, убери лишние тени и рамки, один акцентный цвет для всех кнопок."),
 ("Тексты", "Перепиши тексты короче и конкретнее, выгоды вместо характеристик, без канцелярита и фраз «индивидуальный подход». Заголовок до 8 слов."),
 ("Телефон", "Проверь ширину 375px: кнопки от 44px, текст от 16px, ничего не вылезает. Кнопку записи закрепи внизу экрана."),
 ("Конверсия", "Добавь бейдж «Популярный» на средний тариф, блок гарантии перед формой и кнопку Telegram для быстрой связи."),
 ("Скорость и SEO", "Картинки в WebP с lazy loading, один H1, alt у всех картинок, title, description, Open Graph, микроразметка FAQPage."),
 ("Заявки", "Отправляй форму в Telegram-бота через серверную функцию. Токен и chat_id только в переменных окружения, не в коде страницы."),
]

def build():
    qs = ''.join(f'<div style="margin-bottom:4.5mm"><div style="display:flex;gap:3mm;align-items:baseline"><b style="font:800 18pt/1 var(--fd);color:var(--blue)">{i+1}</b><b style="font-size:11.5pt">{q}</b><span class="muted" style="font-size:8.5pt">{h}</span></div><div class="lines"></div></div>' for i, (q, h) in enumerate(Q[:4]))
    moods = ''.join(f'<span style="display:inline-flex;align-items:center;gap:1.6mm;margin:0 4mm 2mm 0;font-size:10pt"><i style="width:3.8mm;height:3.8mm;border:1pt solid var(--ink);background:#fff;display:inline-block"></i>{m}</span>' for m in MOODS)
    p1 = f'''<p class="kick">Памятка 03 из 08 · рабочий лист</p>
<h1 style="font-size:52pt">Лендинг за вечер</h1>
<p class="lead" style="margin-bottom:7mm">Ответы на эти пять вопросов и есть бриф. Без них нейросеть сделает красивый пустой шаблон.</p>
{qs}
<div><div style="display:flex;gap:3mm;align-items:baseline;margin-bottom:3mm"><b style="font:800 18pt/1 var(--fd);color:var(--blue)">5</b><b style="font-size:11.5pt">Какое настроение у бренда?</b></div>{moods}<div class="lines" style="height:7mm"></div></div>
<p class="hand" style="margin-top:auto;align-self:flex-end">хороший промпт = хороший бриф</p>'''
    plan = ''.join(f'''<div style="display:grid;grid-template-columns:18mm 14mm 1fr;gap:3mm;padding:2.6mm 0;border-top:.8pt solid var(--line);align-items:baseline">
 <b style="font:800 12pt/1 var(--fd)">{t}</b><span class="mono" style="font-size:7pt;opacity:.6">{d}</span><span><b>{h}.</b> {x}</span></div>''' for t, d, h, x in PLAN)
    p2 = f'''<h2>План вечера: 4 часа</h2>
<p class="muted" style="margin-bottom:4mm">От идеи до сайта, который принимает заявки. Время ориентировочное, первый раз закладывайте в полтора раза больше.</p>
<div style="display:flex;height:6mm;margin-bottom:4mm">{''.join(f'<i style="flex:{int(d.split()[0])};background:{c};display:block"></i>' for (t,d,h,x),c in zip(PLAN,['#2335FF','#2335FF','#C6F432','#FF5A1F','#FF5A1F','#121212','#C6F432','#2335FF','#121212','#FF5A1F']))}</div>
{plan}
<div class="g3" style="margin-top:auto">
 <div class="cell"><span class="k">Сгенерировать</span><p>Lovable, Google AI Studio (Build), ChatGPT Sites, Claude</p></div>
 <div class="cell"><span class="k">Тексты и ТЗ</span><p>ChatGPT, Claude, GigaChat, Алиса AI</p></div>
 <div class="cell"><span class="k">Не забыть</span><p>Сохранять версии. В каждом сервисе есть откат к прошлому варианту</p></div>
</div>'''
    edits = ''.join(f'<div class="cell" style="margin-bottom:3mm"><span class="k">{h}</span><p style="font:400 8.6pt/1.4 var(--fm)">{x}</p></div>' for h, x in EDITS)
    p3 = f'''<h2>Промпты</h2>
<div class="g2" style="gap:6mm">
 <div><p class="kick">Промпт 0 · ТЗ из ответов</p><pre class="prompt" style="margin-bottom:5mm">{P0}</pre>
 <p class="kick">Промпт 1 · сам лендинг</p><pre class="prompt">{P1}</pre></div>
 <div><p class="kick">Правки одной фразой</p>{edits}</div>
</div>
<div class="box blue" style="margin-top:auto;display:flex;justify-content:space-between;align-items:center;gap:6mm">
 <p style="margin:0;font:700 12pt/1.3 var(--ft)">Одна подробная правка лучше десяти мелких. Экономит кредиты и время.</p>
 <span class="mono" style="font-size:7.5pt;white-space:nowrap">Lovable Free: 5 кредитов в день</span>
</div>'''
    return doc('Лендинг за вечер', [page(p1, R, 'Рабочий лист', 1, 3), page(p2, R, 'План', 2, 3), page(p3, R, 'Промпты', 3, 3)])
