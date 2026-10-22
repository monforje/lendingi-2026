# -*- coding: utf-8 -*-
"""PDF-сценарий пары для лектора: python3 scenario.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from base import page, doc, md, checklist

R = 'Сценарий лектора'
SER = 'Сайты, что продают · сценарий пары'

TIMING = [
 ('0:00', '5', 'Вступление, GitHub', '1-6', 'QR на GitHub, все регистрируются фоном. Главная мысль. История 01.'),
 ('0:05', '7', 'Блок 01 · Зачем сайт', '7-13', '5 вопросов студенту. Бриф: поля 01-03.'),
 ('0:12', '6', 'Блок 02 · История', '14-23', 'Таймлайн, живые сайты. Вопрос «какой сайт помните из детства».'),
 ('0:18', '4', 'Блок 03 · Виды сайтов', '24-27', 'Бриф: поле 04. История 02.'),
 ('0:22', '9', 'Блок 04 · Лендинги', '28-35', 'Анатомия, AIDA, конверсия. Бриф: поля 05-06.'),
 ('0:31', '9', 'Блок 05 · UI/UX, тренды', '36-58', 'История 03. Анти-ИИ, impeccable. Тренды, голосование. Бриф: 07-09, 13.'),
 ('0:40', '6', 'Блоки 06-08 · Код и архитектура', '59-70', 'HTML/CSS/JS вживую (вкладки). Бриф: поле 10.'),
 ('0:46', '5', 'Блок 09 · SEO', '71-75', 'Бриф: поле 11.'),
 ('0:51', '5', 'Блок 10 · Домены, закон', '76-80', 'Бриф: поля 12-13. Бриф готов.'),
 ('0:56', '30', 'Блок 11 · Нейросети и практика', '81-91', 'Обзор 5 мин, генерация 10, код 5, GitHub Pages 10. История 04, ссылки в чат.'),
 ('1:26', '4', 'Блок 12 · Итоги', '92-95', 'История 05. Финальная мысль. Вопросы.'),
]

PREP = [
 'Выключить VPN на ноутбуке для показа: GitHub закрывает доступ некоторым VPN (проверено при подготовке)',
 'Войти заранее: GitHub, Google AI Studio, Lovable, ChatGPT или Claude. Проверить доступ с той же сети, что в аудитории',
 'Открыть вкладки: presentation/index.html, brief/index.html, aistudio.google.com, lovable.dev, github.com',
 'Создать чат группы (Telegram) и закрепить ссылку на бриф и на этот набор',
 'На проекторе нажать F в презентации. Заметки по клавише N, оглавление по M',
 'Заранее сгенерировать один сайт по примеру «барбершоп» на случай, если интернет упадет',
 'Проверить на своем GitHub, что Pages публикуется: залить тестовый index.html',
 'Распечатать этот сценарий и рабочий лист брифа (последняя страница) для группы',
]

BLOCKS = [
 ('01', 'Вступление и зачем маркетологу сайт', '0:00-0:12', [
   ('Сказать', 'Код стал дешевым, дорого понимать, что продавать. Пять лет назад лендинг делала команда за две недели и 50 000 ₽, сегодня один маркетолог за вечер.'),
   ('Интерактив', 'Слайд «Сделайте сейчас: GitHub»: все сканируют QR и регистрируются, пока вы говорите. Через 10 минут спросить, у кого не вышло.'),
   ('Интерактив', 'Пять вопросов студенту: что продаем, кому, почему у нас, какое действие, какое настроение. Ответы сразу в бриф, поля 01-03.'),
   ('История 01', 'Набор к паре сделан за вечер с ИИ-агентом. Что делал агент, что решали вы, что пришлось переделывать.'),
   ('Если спросят', '«Программисты больше не нужны?» Нужны для сложных систем, безопасности и нагрузок. Лендинг и прототип теперь закрывает маркетолог.')]),
 ('02', 'История веба и дизайна', '0:12-0:18', [
   ('Сказать', 'Каждые 5-10 лет порог входа падал: ученые, программисты, верстальщики, конструкторы, теперь любой с идеей. Обесценивалась техника, но не смысл.'),
   ('Показать', 'Слайд «Тогда и сейчас»: info.cern.ch 1991 года до сих пор открывается. WordPress держит больше 40% сайтов мира. Tilda с 2014 года.'),
   ('Если пауза', 'Спросить: какой сайт из детства вы помните? Флеш-игры, uCoz, счетчики посещений.')]),
 ('03', 'Виды сайтов', '0:18-0:22', [
   ('Сказать', 'Тип сайта выбирают от задачи. Частая ошибка: большой сайт про компанию вместо одного лендинга под кампанию.'),
   ('Бриф', 'Поле 04: тип сайта и действие. Варианты: запись, звонок, предзаказ, регистрация.'),
   ('История 02', 'Идею назвали плохой: настолку для чемпионата пришлось пересобрать. Вывод: лендинг «оставь почту» дает «нет» за день, а не за полгода.')]),
 ('04', 'Лендинги', '0:22-0:31', [
   ('Сказать', 'Одна цель, одна кнопка. Первый экран решает за 3-5 секунд. Блоки по порядку, AIDA и PAS.'),
   ('Показать', 'Магнитная кнопка на слайде «Что такое лендинг»: навести курсор.'),
   ('Цифры', 'Конверсия 2-5% для рекламы нормальна, выше 10% при горячем трафике. Сравнивать страницу с собой через A/B-тест.'),
   ('Бриф', 'Поля 05-06: оффер до 8 слов и 7-9 блоков страницы. Попросить группу придумать 2-3 заголовка, выбрать голосованием.')]),
 ('05', 'UI/UX, анти-ИИ и тренды', '0:31-0:40', [
   ('Сказать', 'UX это планировка, UI это ремонт. Тест 5 секунд. Главный тренд 2026: анти-ИИ, видно руку человека.'),
   ('История 03', 'Брендбук «Наследия» до первого слайда: сначала решения бренда, потом генерация.'),
   ('Показать', 'Impeccable: каталог ИИ-штампов и сканер `npx impeccable detect`. Слева на слайде «по умолчанию», справа «когда думал человек».'),
   ('Тренды', 'Пролистать 9 трендов быстро, на каждом открыть пример из папки sites и кнопку «О стиле». Живые референсы: swissted, pudding, awwwards.'),
   ('Бриф', 'Поля 07-09: голосуем за тренд, выбираем шрифты и 2-3 анимации. Поле 13 «Чего не должно быть» по слайду анти-ИИ.')]),
 ('06-08', 'Код, React, архитектура', '0:40-0:46', [
   ('Показать', 'Слайд «Сайт это три слоя»: нажать HTML, CSS, JS по очереди, потом нажать кнопку. F12 на любом сайте и поменять заголовок.'),
   ('Сказать', 'Lovable и AI Studio пишут на React. Для GitHub Pages проще всего один файл index.html. Лендинг это цепочка: трафик, UTM, страница, форма, заявка, аналитика.'),
   ('Бриф', 'Поле 10: техника. Для группы: один index.html. Сильным студентам: React + Vite и сборка.')]),
 ('09', 'Скорость и SEO', '0:46-0:51', [
   ('Сказать', 'PageSpeed от 90, LCP до 2,5 с. Главная причина медленных сайтов: фото с телефона по 5 МБ. Яндекс главный, карточка на Картах часто важнее сайта.'),
   ('Цифра', 'Во II квартале 2026 Алиса AI отвечала на 42% запросов в поиске Яндекса. Нужен GEO: FAQ, факты, микроразметка.'),
   ('Бриф', 'Поле 11: title до 60 символов, description до 160.')]),
 ('10', 'Домены, хостинг, закон', '0:51-0:56', [
   ('Сказать', 'Домен .ru у регистратора из списка cctld.ru, смотрите цену продления. Сайты на Vercel и за Cloudflare у части пользователей в России не открываются. Под рекламу: российский хостинг.'),
   ('Закон', 'Форма с телефоном делает вас оператором данных. Отдельный чекбокс согласия, политика, уведомление в РКН, данные в РФ.'),
   ('Бриф', 'Поля 12-13. Объявить: бриф готов, дальше практика.')]),
]

PRACTICE = [
 ('Обзор инструментов', '5 мин', 'Вайб-кодинг, три класса инструментов, история Lovable (600+ млн $ ARR, оценка 13,3 млрд $). Слайд со скриншотами: Lovable, AI Studio, ChatGPT Sites, Claude Code, v0.'),
 ('Практика 1: генерация', '10 мин', 'Скинуть ссылку на бриф в чат. Все копируют промпт и отправляют в любую платформу. Нажать на таймер на слайде. Сами генерируете на проекторе. Каждый делает одну правку своими словами.'),
 ('Практика 2: забираем код', '5 мин', 'AI Studio: скачать ZIP. Lovable: подключить GitHub. ChatGPT, Claude, GigaChat: «выдай одним файлом index.html». Двойной клик по файлу: сайт открылся.'),
 ('Практика 3: GitHub Pages', '10 мин', 'New repository my-site, Public. Add file, Upload files, index.html, Commit. Settings, Pages, Deploy from a branch, main, root, Save. Через 1-2 минуты сайт по адресу имя.github.io/my-site.'),
 ('Финал: ссылки в чат', '3 мин', 'Открыть 3-4 сайта на проекторе, найти что получилось и где вылез ИИ-шаблон. История 04 про git push.'),
]

TROUBLE = [
 ('GitHub: «Доступ временно ограничен»', 'Выключить VPN или зайти с мобильного интернета. Бывает на общих IP.'),
 ('Pages: 404', 'Подождать 2 минуты. Файл должен называться index.html маленькими буквами и лежать в корне. Репозиторий Public.'),
 ('Pages: белый экран у React-проекта', 'В vite.config добавить `base: \'/my-site/\'` и пересобрать `npm run build`. Загружать содержимое папки dist, а не саму папку.'),
 ('Стили и картинки не грузятся', 'Пути должны быть относительными: `assets/img.png`, а не `/assets/img.png` и не `C:\\Users\\...`.'),
 ('Нейросеть выдала код кусками', 'Попросить: «Выдай весь файл целиком, не сокращай». Или «разбей на 2 сообщения, я склею».'),
 ('Сервис недоступен из России', 'GigaChat или Алиса AI с промптом на один файл index.html. Код можно доработать в любой другой нейросети.'),
 ('Кончились кредиты Lovable', 'Бесплатно 5 кредитов в день. Перейти в Google AI Studio, он бесплатный.'),
 ('Сайт обновился, а в браузере старый', 'Ctrl+Shift+R. GitHub Pages обновляет кэш до нескольких минут.'),
]

STORIES = [
 ('01', 'Набор сделан за вечер с ИИ-агентом', 'после «Главная мысль»', 'Презентация, 8 сайтов, гайдбук и памятки собраны с агентом. Он писал код и правил ошибки, вы решали, что показать и кому. Честно про переделки: первые версии сайтов лагали и выглядели как ИИ-шаблон.'),
 ('02', 'Идею назвали плохой', 'после «9 видов сайтов»', 'Концепт настолки с цифровым слоем для чемпионата культурных проектов получил жесткий отзыв. Пересобрали под критерии жюри. Мораль: проверяйте идею лендингом до разработки.'),
 ('03', 'Брендбук до первого слайда', 'после «10 правил UI»', '«Наследие», визуальная новелла по фольклору народов России, команда из четырех человек. Перед питчем сделали брендбук, и все слайды пошли в одном стиле.'),
 ('04', 'Git push, и код уже проверен', 'после практики GitHub', 'Kornishon: разработчик отправляет решение через git push, проверки запускаются сами. Сегодня группа сделала первый шаг этого пути.'),
 ('05', 'Клиент покупает заявки', 'перед финалом', 'Профили на биржах фриланса: лендинги, боты, ИИ-агенты. Заказчику важны заявки и скорость, а не технология.'),
]

QA = [
 ('Сколько стоит лендинг в 2026?', 'Самому от 0 до 2-5 тысяч рублей в год за домен и хостинг. Фрилансер на Tilda от 15-30 тысяч. Агентство от 100 тысяч. Разница в стратегии и текстах.'),
 ('Можно на этом зарабатывать?', 'Да. Малому бизнесу нужен не код, а заявки. Продавайте «лендинг под рекламу с аналитикой».'),
 ('Тильда или нейросеть?', 'Тильда: стабильность, оплата из РФ, CRM, клиент правит сам. Нейросеть: уникальный дизайн, квизы, калькуляторы, свой код.'),
 ('Нейросеть украдет данные?', 'На бесплатных тарифах промпты могут идти в обучение. Не загружайте базы клиентов и пароли.'),
 ('Нужен ли дизайнер?', 'Для теста гипотезы нет. Для сильного бренда да: он задает визуальный язык, который потом отдают нейросети.'),
 ('GitHub Pages подходит для бизнеса?', 'Для визитки и портфолио да. Для рекламы на Россию лучше российский хостинг и свой домен: формы и персональные данные должны жить в РФ.'),
 ('С чего начать вечером?', 'Взять свой проект, 5 вопросов, промпт в Google AI Studio, деплой на GitHub Pages. 30 минут.'),
]

FIELDS = [('01','Бизнес','что продаем, название, город'),('02','Аудитория','кто клиент, чего хочет и боится'),('03','Почему у нас','факты: срок, цена, опыт, место'),
 ('04','Тип сайта и действие','что сделать на сайте'),('05','Оффер','заголовок до 8 слов'),('06','Блоки страницы','7-9 блоков сверху вниз'),
 ('07','Тренд','один из 9'),('08','Шрифты и цвета','2 шрифта, 2-3 HEX'),('09','Анимации','не больше трех'),('10','Технически','один index.html / React'),
 ('11','SEO','title и description'),('12','Форма и 152-ФЗ','поля + чекбокс'),('13','Чего не должно быть','запреты против ИИ-шаблона')]

def slide_ranges():
    import re
    t=re.findall(r'data-title="([^"]+)"', open(os.path.join(HERE,'..','..','presentation','index.html')).read())
    def idx(prefix): return next(i for i,x in enumerate(t) if x.startswith(prefix))+1
    marks=[('Обложка',None),('01 ·',None),('02 ·',None),('03 ·',None),('04 ·',None),('05 ·',None),('06 ·',None),('09 ·',None),('10 ·',None),('11 ·',None),('12 ·',None)]
    starts=[idx(m) for m,_ in marks]+[len(t)+1]
    starts[1]=idx('01 ·'); 
    return [f'{starts[i]}-{starts[i+1]-1}' for i in range(len(marks))], len(t)

def build():
    T = 10
    rng, NS = slide_ranges()
    global TIMING
    TIMING=[(a,b,c,rng[i],e) for i,(a,b,c,d,e) in enumerate(TIMING)]
    rows = ''.join(f'<tr><td class="mono"><b>{t}</b></td><td class="mono">{m}</td><td style="width:38mm"><b>{h}</b></td><td class="mono" style="font-size:7.5pt">{sl}</td><td>{x}</td></tr>' for t, m, h, sl, x in TIMING)
    p1 = f'''<p class="kick">Только для лектора</p>
<h1 style="font-size:42pt;margin-bottom:2mm">Сценарий пары</h1>
<p class="lead" style="margin-bottom:4mm;font-size:10.5pt">90 минут, {NS} слайдов, один общий бриф, который группа заполняет по ходу пары, и практика: каждый генерирует сайт и публикует его на GitHub Pages.</p>
<style>.tl td,.tl th{{padding:1.3mm 1.6mm}}</style><table class="vs tl" style="font-size:8pt;line-height:1.25"><tr><th>Время</th><th>Мин</th><th>Блок</th><th>Слайды</th><th>Интерактив</th></tr>{rows}</table>
<div class="g3" style="margin-top:4mm;gap:4mm;font-size:8.5pt">
 <div class="box ink"><p class="kick" style="color:var(--lime);opacity:1">Главная мысль</p><p style="margin:0;font:700 11pt/1.3 var(--ft)">Код стал дешевым. Дорого понимать, что продавать.</p></div>
 <div class="box lime"><p class="kick" style="opacity:1">Сквозной бриф</p><p style="margin:0">13 полей, заполняем после каждого блока в brief/index.html на проекторе.</p></div>
 <div class="box"><p class="kick">Клавиши</p><p style="margin:0">F полный экран, N заметки, M оглавление, стрелки листают. Таймер на слайде запускается кликом.</p></div>
</div>'''
    p2 = f'''<h2>Подготовка до пары</h2>
{checklist(PREP)}
<h2 style="margin-top:8mm">Сквозной бриф: когда какое поле</h2>
<table class="vs" style="font-size:8.8pt"><tr><th>Поле</th><th>Что спрашиваем</th><th>Когда</th></tr>
{''.join(f'<tr><td><b>{n} · {h}</b></td><td>{q}</td><td class="mono" style="font-size:7.5pt">{w}</td></tr>' for (n,h,q),w in zip(FIELDS,['блок 01','блок 01','блок 01','блок 03','блок 04','блок 04','блок 05','блок 05','блок 05','блоки 06-08','блок 09','блок 10','блок 05 / 10']))}</table>
<div class="box ink" style="margin-top:auto"><p style="margin:0">Если группа молчит, кнопка «Пример: барбершоп» в брифе заполняет всё. Тогда просите поменять одно поле под себя: так интерактив все равно происходит.</p></div>'''
    pages = [page(p1, R, 'Таймлайн', 1, T, series=SER), page(p2, R, 'Подготовка', 2, T, series=SER)]
    # блоки: по 3-4 на страницу
    def blk(b):
        n, h, t, items = b
        it = ''.join(f'<div style="display:grid;grid-template-columns:24mm 1fr;gap:3mm;padding:1.6mm 0;border-top:.6pt solid var(--line)"><span class="mono" style="font-size:7.3pt;text-transform:uppercase;letter-spacing:.05em;color:{"var(--signal)" if k.startswith("История") else "var(--blue)" if k in ("Бриф","Интерактив") else "var(--ink2)"};font-weight:600">{k}</span><span style="font-size:9pt;line-height:1.38">{md(x)}</span></div>' for k, x in items)
        return f'<div class="sec" style="margin-bottom:6mm"><div style="display:flex;justify-content:space-between;align-items:baseline;border-top:1.6pt solid var(--ink);padding-top:2mm;margin-bottom:1mm"><h3 style="margin:0"><b style="color:var(--blue);font:800 13pt var(--fd);margin-right:3mm">{n}</b>{h}</h3><span class="mono" style="font-size:8pt">{t}</span></div>{it}</div>'
    groups = [BLOCKS[0:3], BLOCKS[3:5], BLOCKS[5:8]]
    for gi, g in enumerate(groups):
        pages.append(page(''.join(blk(b) for b in g), R, 'Блоки ' + ', '.join(b[0] for b in g), 3 + gi, T, series=SER))
    pr = ''.join(f'<li><span><b>{h} · {m}</b>{md(x)}</span></li>' for h, m, x in PRACTICE)
    tr = ''.join(f'<tr><td>{md(a)}</td><td>{md(b)}</td></tr>' for a, b in TROUBLE)
    p6 = f'''<h2>Блок 11 · Нейросети и практика</h2>
<p class="muted" style="margin-bottom:3mm">0:56-1:26. Самая важная часть пары: каждый уходит со своим сайтом в интернете.</p>
<ol class="steps">{pr}</ol>
<h3 style="margin-top:5mm">Если что-то не работает</h3>
<table class="vs" style="font-size:8.4pt"><tr><th>Проблема</th><th>Решение</th></tr>{tr}</table>'''
    pages.append(page(p6, R, 'Практика', 6, T, series=SER))
    cmd = '''<pre class="prompt" style="font-size:8.2pt"># React / Vite проект из AI Studio или Lovable
npm install          # один раз, ставит зависимости
npm run dev          # сайт на localhost для проверки
npm run build        # готовые файлы в папке dist

# vite.config.ts для GitHub Pages
export default defineConfig({
  base: '/my-site/',   # имя репозитория
  plugins: [react()],
})

# для тех, кто хочет через git
git init
git add .
git commit -m "first site"
git branch -M main
git remote add origin https://github.com/ИМЯ/my-site.git
git push -u origin main</pre>'''
    p7 = f'''<h2>Шпаргалка: локальная сборка и git</h2>
<div class="g2" style="gap:7mm">
 <div>{cmd}</div>
 <div>
  <div class="cell" style="margin-bottom:4mm"><span class="k">Без терминала</span><p>GitHub Desktop: File, Add local repository, Publish repository. Затем Settings, Pages.</p></div>
  <div class="cell" style="margin-bottom:4mm"><span class="k">Автодеплой</span><p>Для Vite-проекта: Settings, Pages, Source: GitHub Actions, шаблон «Static HTML» или «Vite». Каждый push сам обновляет сайт.</p></div>
  <div class="cell" style="margin-bottom:4mm"><span class="k">Адрес сайта</span><p>Репозиторий my-site: `ИМЯ.github.io/my-site`. Репозиторий с именем `ИМЯ.github.io`: сайт прямо на `ИМЯ.github.io`.</p></div>
  <div class="cell"><span class="k">Свой домен</span><p>Settings, Pages, Custom domain. У регистратора добавить CNAME на `ИМЯ.github.io`.</p></div>
 </div>
</div>
<div class="box lime" style="margin-top:auto"><p style="margin:0"><b>Если не успели в паре:</b> это домашнее задание. Промпт: «Объясни по шагам, как собрать этот Vite-проект и опубликовать на GitHub Pages, я на Windows и никогда не открывал терминал».</p></div>'''
    pages.append(page(p7, R, 'Шпаргалка', 7, T, series=SER))
    st = ''.join(f'<div class="sec" style="margin-bottom:4mm;border-top:1.4pt solid var(--ink);padding-top:2.5mm"><div style="display:flex;justify-content:space-between"><b style="font:400 13pt \'Yeseva One\',serif">{n}. {h}</b><span class="mono" style="font-size:7.5pt;color:var(--signal)">{w}</span></div><p style="font-size:9pt;margin:1.5mm 0 1.5mm">{x}</p><div class="lines" style="height:13mm"></div></div>' for n, h, w, x in STORIES)
    p8 = f'''<h2>Истории из опыта</h2>
<p class="muted" style="margin-bottom:4mm">Пять коротких историй по 1 минуте. Основа взята из ваших проектов, детали допишите своими словами на линейках: цифры, имена, что было сложно.</p>
{st}'''
    pages.append(page(p8, R, 'Истории', 8, T, series=SER))
    qa = ''.join(f'<div style="border-top:.8pt solid var(--line);padding:2.4mm 0"><b style="font-size:10pt">{q}</b><p style="font-size:9pt;margin:1mm 0 0">{a}</p></div>' for q, a in QA)
    p9 = f'''<h2>Ответы на частые вопросы</h2>{qa}
<div class="box ink" style="margin-top:auto"><p class="kick" style="color:var(--lime);opacity:1">Финальная мысль, дословно</p>
<p style="margin:0;font:400 11pt/1.4 var(--ft)">Код больше не барьер. Сегодня вы видели, как сайт появился из пяти ответов и оказался в интернете за полчаса. Барьер в другом: знать, кому вы продаете, что обещаете и почему вам поверят. Пользуйтесь нейросетями каждый день и запускайтесь быстро.</p></div>'''
    pages.append(page(p9, R, 'Вопросы', 9, T, series=SER))
    fl = ''.join(f'<div style="display:grid;grid-template-columns:9mm 1fr;gap:3mm;border-top:.8pt solid var(--ink);padding:1.8mm 0 0;break-inside:avoid"><b style="font:800 12pt var(--fd);color:var(--blue)">{n}</b><span><b style="font-size:9.5pt">{h}</b> <span class="muted" style="font-size:7.6pt">{q}</span><div class="lines" style="height:13mm"></div></span></div>' for n, h, q in FIELDS)
    fl = '<div style="columns:2;column-gap:8mm">' + fl + '</div>'
    p10 = f'''<p class="kick">Раздаточный лист для группы</p>
<h1 style="font-size:40pt">Бриф для нейросети</h1>
<p style="margin-bottom:3mm">Заполняйте по ходу пары. В конце перенесите в промпт и отправьте в Lovable, Google AI Studio, ChatGPT, Claude или GigaChat.</p>
{fl}
<p class="mono" style="font-size:7.5pt;margin-top:3mm">Онлайн-версия с готовым промптом: brief/index.html в наборе лекции</p>'''
    pages.append(page(p10, 'Рабочий лист', 'для студентов', 10, T, series=SER))
    return doc('Сценарий пары', pages)

if __name__ == '__main__':
    from playwright.sync_api import sync_playwright
    h = os.path.join(HERE, 'scenario.html'); open(h, 'w').write(build())
    out = os.path.join(os.path.dirname(HERE), '00-scenarij-lektora.pdf')
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(); pg.goto('file://' + h); pg.wait_for_timeout(800)
        ov = pg.evaluate('''[...document.querySelectorAll('.page')].map((p,i)=>{const r=p.getBoundingClientRect();let m=0;p.querySelectorAll('*').forEach(e=>{if(e.closest('.foot'))return;const b=e.getBoundingClientRect().bottom-r.top;if(b>m)m=b});return [i+1,Math.round(m/r.height*1000)/10]}).filter(x=>x[1]>94)''')
        print('overflow', ov)
        pg.pdf(path=out, format='A4', print_background=True, prefer_css_page_size=True); b.close()
    os.remove(h); print('ok', out)
