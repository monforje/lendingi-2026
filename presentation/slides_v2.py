# -*- coding: utf-8 -*-
"""Вставляет интерактив, истории, бриф и реальные скриншоты в презентацию. Запуск один раз."""
import re
P = '/home/claude/kit/presentation/index.html'
s = open(P).read()

def find(title):
    i = s.index(f'data-title="{title}"')
    a = s.rindex('<section', 0, i)
    b = s.index('</section>', i) + len('</section>')
    return a, b

def after(title, html):
    global s
    a, b = find(title); s = s[:b] + '\n\n' + html + s[b:]

def before(title, html):
    global s
    a, b = find(title); s = s[:a] + html + '\n\n' + s[a:]

def replace(title, html):
    global s
    a, b = find(title); s = s[:a] + html + s[b:]

def bf(img, url, style='', alt=''):
    return f'<div class="bf" style="{style}"><div class="bar"><i></i><i></i><i></i><span>{url}</span></div><img src="screens/{img}.webp" alt="{alt or url}" loading="lazy"></div>'

def brief(nums, title, run, fields, note=''):
    rows = ''
    for n, h, q, opts in fields:
        o = ''.join(f'<span>{x}</span>' for x in opts)
        rows += f'<div class="fld" data-a="up"><b>{n}</b><div><h3>{h}</h3><p>{q}</p><div class="opts">{o}</div></div></div>'
    return f'''<section class="slide brief-slide" data-title="Бриф: {title}">
  <div class="run"><span>Сквозной бриф · поля {nums}</span><span>{run}</span></div>
  <div class="row between" style="align-items:flex-end"><h2 class="h-l" data-a="up">Заполняем бриф</h2><a class="go-brief interactive" href="../brief/index.html#f-{fields[0][4] if len(fields[0])>4 else 'biz'}" target="_blank" rel="noopener">Открыть бриф</a></div>
  <div style="margin-top:30px">{rows}</div>
  <p class="small" style="margin-top:auto;opacity:.8">{note}</p>
  <template class="n"><p>Спросите группу, запишите ответ в бриф на проекторе (brief/index.html). Можно голосовать поднятием рук. Не больше 2 минут на поле.</p></template>
</section>'''

def story(n, title, beats, note):
    b = ''.join(f'<div data-a="up" style="--d:{i+2}"><span>{h}</span><p>{t}</p></div>' for i, (h, t) in enumerate(beats))
    return f'''<section class="slide story" data-title="История {n}: {re.sub('<[^>]+>','',title).replace('&nbsp;',' ')}">
  <div class="run"><span>История из опыта</span><span>{n}</span></div>
  <span class="lbl" data-a="rot">история из опыта</span>
  <h2 data-a="up" style="--d:1">{title}</h2>
  <div class="beats">{b}</div>
  <template class="n">{note}</template>
</section>'''

# ---------- 1. GitHub в начале и сквозной бриф ----------
after('План лекции', f'''<section class="slide" data-title="Сделайте сейчас: GitHub">
  <div class="run"><span>Сделайте сейчас</span><span>понадобится в конце пары</span></div>
  <div class="g2 grow" style="grid-template-columns:1.1fr .9fr;gap:70px">
    <div class="col">
      <p class="eyebrow" data-a="fade">Пока я рассказываю, зарегистрируйтесь</p>
      <h2 class="h-l" data-a="up">GitHub: аккаунт за 3 минуты</h2>
      <ol class="steps2" style="margin-top:20px;color:var(--ink)">
        <li data-a="up" style="--d:2;border-color:var(--line)"><span><b>github.com/signup</b>, почта и пароль</span></li>
        <li data-a="up" style="--d:3;border-color:var(--line)"><span><b>Имя пользователя</b> станет адресом сайта: <code style="background:var(--paper2);color:var(--ink)">имя.github.io</code></span></li>
        <li data-a="up" style="--d:4;border-color:var(--line)"><span><b>Подтвердите почту</b> кодом из письма</span></li>
      </ol>
    </div>
    <div class="col" style="align-items:center;justify-content:center;gap:26px">
      <div class="qr" data-a="scale" style="--d:2"><img src="screens/qr-github-signup.svg" alt="QR-код github.com/signup"></div>
      <span class="mono small">github.com/signup</span>
    </div>
  </div>
  <div class="row" style="align-items:center;gap:30px;margin-top:20px" data-a="up" style2="">
    <div class="bf" style="width:420px;height:262px;flex:none;box-shadow:6px 6px 0 var(--ink)"><div class="bar"><i></i><i></i><i></i><span>github.com/signup</span></div><img src="screens/github-blocked.webp" alt="GitHub: доступ временно ограничен"></div>
    <p class="txt"><b>Видите «Доступ временно ограничен»?</b> GitHub режет подозрительные VPN и общие IP. Выключите VPN или зайдите с мобильного интернета. Этот скриншот я поймал сам, пока готовил лекцию.</p>
  </div>
  <template class="n"><p>Попросить всех открыть QR прямо сейчас. Через 10 минут спросить, у кого не получилось. Частые проблемы: VPN (скриншот реальный, GitHub закрыл доступ при подготовке лекции), письмо подтверждения в спаме, занятое имя пользователя.</p></template>
</section>''')

after('Сделайте сейчас: GitHub', '''<section class="slide dark" data-title="Сквозной бриф">
  <div class="run"><span>Как устроена пара</span><span>13 полей</span></div>
  <div class="g2 grow" style="grid-template-columns:1fr 1fr;gap:70px">
    <div class="col">
      <h2 class="h-l" data-a="up">Один промпт на всю пару</h2>
      <p class="lead" style="color:#ccc" data-a="up" style2="">После каждого блока заполняем вместе одно-два поля. К блоку про нейросети у нас будет готовый бриф, и вы сгенерируете по нему сайт.</p>
      <a class="go-brief interactive" href="../brief/index.html" target="_blank" rel="noopener" style="align-self:flex-start;margin-top:20px" data-a="up">Открыть бриф группы</a>
    </div>
    <pre class="prompt" data-a="right" style="font-size:22px;line-height:1.55;align-self:center">Создай одностраничный сайт на русском.
БИЗНЕС: <em>[01]</em>
АУДИТОРИЯ: <em>[02]</em>
ПОЧЕМУ У НАС: <em>[03]</em>
ТИП И ДЕЙСТВИЕ: <em>[04]</em>
ОФФЕР: <em>[05]</em>
СТРУКТУРА: <em>[06]</em>
СТИЛЬ: <em>[07]</em>  ШРИФТЫ И ЦВЕТА: <em>[08]</em>
АНИМАЦИИ: <em>[09]</em>
ТЕХНИЧЕСКИ: <em>[10]</em>
SEO: <em>[11]</em>  ФОРМА: <em>[12]</em>
НЕ ИСПОЛЬЗУЙ: <em>[13]</em></pre>
  </div>
  <template class="n"><p>Откройте brief/index.html на проекторе во второй вкладке. Кнопка «Пример: барбершоп» заполняет всё сразу, если группа молчит.</p></template>
</section>''')

# ---------- 2. История 1: набор сделан за вечер ----------
after('Главная мысль', story('01', 'Этот набор сделан за&nbsp;вечер с&nbsp;ИИ-агентом', [
  ('Что было', 'Презентация, 8 сайтов, гайдбук и памятки к этой паре. Раньше на такое ушел бы месяц работы дизайнера и верстальщика.'),
  ('Как сделано', 'Я описывал задачу и проверял результат, агент писал код, делал скриншоты и правил ошибки. Мои решения: что показать, кому и зачем.'),
  ('Вывод', 'Код стоил вечер. Дорогим было понимать, что нужно вам, и выбирать из вариантов лучшее.')],
  '<p>Рассказать честно, с деталями: сколько итераций было, что пришлось переделать руками, где агент ошибся (например, сайты сначала лагали и выглядели как ИИ-шаблон, пришлось переделывать). Это мостик к главной мысли.</p>'))

# ---------- 3. Бриф 01-03 после интерактива ----------
after('Интерактив: 5 вопросов', brief('01-03', 'бизнес, аудитория, отличие', 'после блока 01', [
  ('01', 'Бизнес', 'Что продаем, как называется, где?', ['кофейня', 'барбершоп', 'репетитор', 'кондитерская', 'фотограф']),
  ('02', 'Аудитория', 'Кто клиент, чего хочет, чего боится?', ['возраст', 'доход', 'главный страх']),
  ('03', 'Почему у нас', 'Только факты: срок, цена, опыт, место', ['быстрее', 'дешевле', 'ближе', 'уникальнее'])],
  'Если группа молчит: «Пример: барбершоп» в брифе.'))

# ---------- 4. Реальные сайты в истории ----------
after('2013-2022: React, Figma, конструкторы', f'''<section class="slide paper2" data-title="Тогда и сейчас: живые сайты">
  <div class="run"><span>02 · История</span><span>скриншоты из браузера, октябрь 2026</span></div>
  <h2 class="h-m" data-a="up">35 лет одной картинкой</h2>
  <div class="g3" style="margin-top:40px;flex:1;min-height:0;gap:40px">
    <div class="col" data-a="up" style="--d:1;min-height:0">{bf('cern','info.cern.ch','height:420px')}<p class="small"><b>1991.</b> Первый сайт. До сих пор открывается.</p></div>
    <div class="col" data-a="up" style="--d:2;min-height:0">{bf('wordpress','wordpress.org','height:420px')}<p class="small"><b>2003.</b> WordPress: больше 40% всех сайтов мира.</p></div>
    <div class="col" data-a="up" style="--d:3;min-height:0">{bf('tilda','tilda.cc','height:420px')}<p class="small"><b>2014.</b> Tilda. Сегодня уже обещает «сайт вместе с AI».</p></div>
  </div>
</section>''')

# ---------- 5. Бриф 04 + история 02 после видов сайтов ----------
after('9 видов сайтов', brief('04', 'тип сайта', 'после блока 03', [
  ('04', 'Тип сайта и действие', 'Какой сайт нужен нашему бизнесу и что человек должен сделать?', ['лендинг + запись', 'лендинг + звонок', 'предзаказ + почта', 'ивент + регистрация'])]))
after('Бриф: тип сайта', story('02', 'Идею назвали плохой. И&nbsp;это сэкономило месяцы', [
  ('Что было', 'Для чемпионата культурных проектов я придумал настолку с цифровым слоем. Показал людям и услышал жесткое «не то».'),
  ('Что сделал', 'Не стал спорить, а вернулся к критериям жюри и пересобрал идею. Отзыв за один день вместо полугода разработки.'),
  ('Вывод для вас', 'Лендинг «оставь почту» проверяет идею до того, как вы потратите деньги. Это самый дешевый способ услышать «нет».')],
  '<p>Расскажите своими словами: какой был проект, кто и как отреагировал, что поменяли. Можно добавить, какую идею выбрали в итоге. Подставьте реальные детали.</p>'))

# ---------- 6. Бриф 05-06 после конверсии ----------
after('Конверсия', brief('05-06', 'оффер и блоки', 'после блока 04', [
  ('05', 'Оффер и заголовок', 'Что получит + за какой срок + почему без риска. До 8 слов.', ['«Стрижка за 40 минут»', '«Первый урок бесплатно»']),
  ('06', 'Блоки страницы', 'Выбираем 7-9 блоков сверху вниз', ['первый экран', 'доверие', 'боль', 'услуги и цены', 'как работает', 'отзывы', 'FAQ', 'форма', 'контакты'])]))

# ---------- 7. История 03: Наследие и брендбук ----------
after('10 правил UI', story('03', 'Брендбук до&nbsp;первого слайда', [
  ('Проект', 'Наша команда из четырех человек делает визуальную новеллу «Наследие» по фольклору народов России.'),
  ('Что сделали', 'Прежде чем собирать питч для инвесторов, сделали брендбук: шрифты, цвета, правила. Дальше все слайды команда собирала в одном стиле.'),
  ('Вывод', 'С нейросетью так же: сначала решения бренда, потом генерация. Иначе каждый экран будет из своего шаблона.')],
  '<p>Добавьте детали: кто в команде за что отвечает, как выглядел брендбук, что изменилось после. Можно показать пару слайдов, если есть.</p>'))

# ---------- 8. Анти-ИИ: impeccable ----------
after('Как сделать анти-ИИ', f'''<section class="slide" data-title="Инструмент: impeccable">
  <div class="run"><span>05 · Анти-ИИ</span><span>impeccable.style/slop</span></div>
  <div class="g2 grow" style="grid-template-columns:1.25fr .75fr;gap:60px;align-items:center">
    <div data-a="left">{bf('impeccable','impeccable.style/slop','height:640px')}</div>
    <div class="col">
      <h2 class="h-m" data-a="up">Проверка на ИИ-слоп</h2>
      <p class="txt" data-a="up" style="--d:1">Каталог из 60+ признаков сгенерированного дизайна и бесплатный сканер. Показывает, где фиолетовый градиент, Inter, карточки в карточках и мелкий текст.</p>
      <pre class="prompt" data-a="up" style="--d:2;font-size:22px">npx impeccable detect index.html</pre>
      <p class="small muted" data-a="up" style="--d:3">Сайты-примеры из набора прошли эту проверку и переделку перед парой.</p>
    </div>
  </div>
</section>''')

# ---------- 9. Живые референсы и анимации ----------
after('Все тренды на одной странице', f'''<section class="slide" data-title="Живые референсы">
  <div class="run"><span>05 · Тренды</span><span>реальные сайты, октябрь 2026</span></div>
  <h2 class="h-m" data-a="up">Как это выглядит у сильных команд</h2>
  <div class="g3" style="margin-top:36px;gap:40px;flex:1;min-height:0">
    <div class="col" data-a="up" style="--d:1">{bf('swissted','swissted.com','height:430px')}<p class="small"><b>Модульная сетка.</b> Постеры концертов в швейцарском стиле.</p></div>
    <div class="col" data-a="up" style="--d:2">{bf('pudding','pudding.cool','height:430px')}<p class="small"><b>Editorial.</b> Визуальные эссе, номера выпусков, стикеры.</p></div>
    <div class="col" data-a="up" style="--d:3">{bf('awwwards','awwwards.com','height:430px')}<p class="small"><b>Галерея.</b> Сайт дня: oversize-типографика и живые фото.</p></div>
  </div>
</section>''')

after('Микроанимации', f'''<section class="slide dark" data-title="Где брать анимации">
  <div class="run"><span>05 · Моушен</span><span>скриншоты из браузера</span></div>
  <div class="g2 grow" style="gap:50px;margin-top:10px">
    <div class="col" data-a="left">{bf('reactbits','reactbits.dev','height:560px')}<p class="small" style="color:#ccc"><b>React Bits.</b> 200+ анимированных компонентов. Можно скопировать или отдать название нейросети.</p></div>
    <div class="col" data-a="right">{bf('gsap','gsap.com','height:560px')}<p class="small" style="color:#ccc"><b>GSAP.</b> Стандарт анимации, с 2025 года бесплатен целиком благодаря Webflow.</p></div>
  </div>
</section>''')

after('Где брать анимации', brief('07-09', 'стиль, шрифты, анимации', 'после блока 05', [
  ('07', 'Тренд', 'Голосуем руками за один тренд', ['oversize', 'editorial', 'bento', 'new rococo', 'ascii', 'grunge', 'naive', 'trinket']),
  ('08', 'Шрифты и цвета', '2 шрифта с кириллицей и 2-3 цвета', ['Unbounded + Onest', 'Cormorant + Onest']),
  ('09', 'Анимации', 'Не больше трех эффектов', ['Split Text', 'Magnet', 'Marquee', 'Count Up'])], 'Поле 13 «Чего не должно быть» заполняем по слайду анти-ИИ.'))

# ---------- 10. Бриф 10 после архитектуры ----------
after('Статика, SSR, SPA', brief('10', 'техника', 'после блоков 06-08', [
  ('10', 'Технически', 'Для GitHub Pages проще всего один файл index.html. Опытным: React + Vite и сборка.', ['один index.html', 'React + Vite', 'Astro'])]))

# ---------- 11. Бриф 11 после GEO, 12-13 после 152-ФЗ ----------
after('GEO: SEO для нейросетей', brief('11', 'SEO', 'после блока 09', [
  ('11', 'SEO', 'Title до 60 символов и описание до 160', ['что + город + выгода'])]))
after('152-ФЗ: форма на лендинге', brief('12-13', 'форма и запреты', 'после блока 10', [
  ('12', 'Форма и 152-ФЗ', 'Какие поля? Чекбокс согласия обязателен', ['имя + телефон', 'имя + телефон + услуга']),
  ('13', 'Чего не должно быть', 'Запреты против ИИ-шаблона', ['градиенты', 'Inter', 'эмодзи', 'иконки в кружках', 'всё по центру'])], 'Бриф готов. Дальше генерируем сайт.'))

# ---------- 12. Инструменты: реальные скриншоты ----------
after('Инструменты по отдельности', f'''<section class="slide paper2" data-title="Так выглядят инструменты">
  <div class="run"><span>11 · AI</span><span>скриншоты из браузера, октябрь 2026</span></div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:28px;flex:1;min-height:0">
    <div style="grid-row:span 2" class="col" data-a="up">{bf('lovable','lovable.dev','height:100%')}</div>
    <div data-a="up" style="--d:1;min-height:0">{bf('aistudio','ai.google.dev · Build mode','height:100%')}</div>
    <div data-a="up" style="--d:2;min-height:0">{bf('chatgptsites','openai.com · ChatGPT Sites','height:100%')}</div>
    <div data-a="up" style="--d:3;min-height:0">{bf('claudecode','claude.com · Claude Code','height:100%')}</div>
    <div data-a="up" style="--d:4;min-height:0">{bf('v0','v0.app','height:100%')}</div>
  </div>
</section>''')

# ---------- 13. Практика вместо «Демо: порядок» ----------
replace('Демо: порядок', '''<section class="slide practice" data-title="Практика 1: генерируем сайт">
  <div class="run"><span>Практика 1 из 3</span><span>10 минут</span></div>
  <div class="g2 grow" style="grid-template-columns:1.2fr .8fr;gap:60px">
    <div class="col">
      <span class="tag-p" data-a="fade">Все за ноутбуки и телефоны</span>
      <h2 class="h-l" data-a="up" style="margin-top:20px">Генерируем сайт по нашему брифу</h2>
      <ol class="steps2" style="margin-top:20px">
        <li data-a="up" style="--d:2"><span><b>Скопируйте промпт</b> из брифа группы (ссылку пришлю в чат)</span></li>
        <li data-a="up" style="--d:3"><span><b>Выберите платформу:</b> Google AI Studio (бесплатно), Lovable, ChatGPT, Claude, GigaChat</span></li>
        <li data-a="up" style="--d:4"><span><b>Сделайте одну правку</b> своими словами: «сделай дороже», «замени цвет»</span></li>
      </ol>
    </div>
    <div class="col center interactive" style="gap:20px">
      <div class="timer" data-min="10" title="Нажмите, чтобы запустить">10:00</div>
      <span class="mono small" style="opacity:.6">нажмите на таймер</span>
    </div>
  </div>
  <template class="n"><p>Пока все генерируют, сами делаете то же самое на проекторе (Lovable или AI Studio). Ходите по аудитории, помогайте. Кто без доступа к зарубежным сервисам: GigaChat или Алиса AI, промпт «выдай один файл index.html целиком».</p></template>
</section>

<section class="slide practice" data-title="Практика 2: забираем код">
  <div class="run"><span>Практика 2 из 3</span><span>5 минут</span></div>
  <h2 class="h-l" data-a="up">Забираем код себе</h2>
  <div class="g4" style="margin-top:44px;gap:30px">
    <div class="cell" data-a="up" style="--d:1"><span class="k">Google AI Studio</span><p>Кнопка скачивания проекта (Download / Export) или «Export to GitHub». Получите ZIP с проектом.</p></div>
    <div class="cell" data-a="up" style="--d:2"><span class="k">Lovable</span><p>Подключите GitHub в настройках проекта: код сам появится в репозитории.</p></div>
    <div class="cell" data-a="up" style="--d:3"><span class="k">ChatGPT, Claude, GigaChat</span><p>Попросите: «Выдай сайт одним файлом index.html, CSS и JS внутри». Сохраните текст в файл.</p></div>
    <div class="cell" data-a="up" style="--d:4"><span class="k">Проверка</span><p>Дважды кликните по index.html. Открылся в браузере? Значит, это и есть сайт.</p></div>
  </div>
  <div class="box" style="margin-top:auto;background:#262624;padding:30px" data-a="up" style2=""><p class="txt" style="color:#fff;max-width:none;margin:0"><b style="color:var(--lime)">Главный момент пары:</b> сайт это просто файл. Его можно положить куда угодно, и он будет работать.</p></div>
</section>

<section class="slide practice" data-title="Практика 3: GitHub Pages">
  <div class="run"><span>Практика 3 из 3</span><span>10 минут · без терминала</span></div>
  <div class="g2 grow" style="grid-template-columns:1fr 1fr;gap:60px">
    <div class="col">
      <h2 class="h-m" data-a="up">Публикуем на GitHub Pages</h2>
      <ol class="steps2" style="margin-top:14px">
        <li data-a="up" style="--d:1"><span><b>New repository</b>, имя <code>my-site</code>, Public</span></li>
        <li data-a="up" style="--d:2"><span><b>Add file</b>, затем <b>Upload files</b>: перетащите index.html, нажмите Commit</span></li>
        <li data-a="up" style="--d:3"><span><b>Settings</b>, раздел <b>Pages</b>: Deploy from a branch, main, / (root), Save</span></li>
        <li data-a="up" style="--d:4"><span>Через 1-2 минуты сайт по адресу <code>имя.github.io/my-site</code></span></li>
      </ol>
    </div>
    <div class="col" data-a="right" style="--d:2;min-height:0">
      <div class="bf" style="height:520px;box-shadow:10px 10px 0 #000"><div class="bar"><i></i><i></i><i></i><span>docs.github.com · GitHub Pages</span></div><img src="screens/ghpages.webp" alt="Документация GitHub Pages"></div>
      <div class="row" style="align-items:center;gap:24px;margin-top:20px"><div class="qr" style="width:150px;height:150px;padding:10px"><img src="screens/qr-ghpages-docs.svg" alt="QR-код инструкции GitHub Pages"></div><span class="small" style="color:#ccc">Официальная инструкция на русском</span></div>
    </div>
  </div>
  <template class="n"><p>Если GitHub пишет «Доступ ограничен», выключить VPN. Если сайт 404: подождать 2 минуты, проверить, что файл называется index.html (маленькими буквами) и лежит в корне.</p></template>
</section>

<section class="slide practice" data-title="Практика 3б: React-проект локально">
  <div class="run"><span>Для тех, кто успел</span><span>React / Vite из AI Studio или Lovable</span></div>
  <div class="g2 grow" style="gap:60px">
    <div class="col">
      <h2 class="h-m" data-a="up">Собираем проект на своем компьютере</h2>
      <ol class="steps2" style="margin-top:14px">
        <li data-a="up" style="--d:1"><span>Установите <b>Node.js LTS</b> с nodejs.org</span></li>
        <li data-a="up" style="--d:2"><span>Распакуйте ZIP, откройте папку в терминале</span></li>
        <li data-a="up" style="--d:3"><span><code>npm install</code>, потом <code>npm run dev</code>: сайт на localhost</span></li>
        <li data-a="up" style="--d:4"><span><code>npm run build</code> создаст папку <code>dist</code></span></li>
        <li data-a="up" style="--d:5"><span>Загрузите содержимое <code>dist</code> в репозиторий, как в практике 3</span></li>
      </ol>
    </div>
    <div class="col" style="justify-content:center;gap:26px">
      <pre class="prompt" data-a="right" style="font-size:22px">// vite.config.ts
export default defineConfig({
  <em>base: '/my-site/',</em>
  plugins: [react()],
})</pre>
      <p class="small" style="color:#ccc" data-a="up">Без строки <b>base</b> на GitHub Pages будет белый экран: сайт ищет файлы в корне домена, а лежит в папке репозитория. Самый частый вопрос после пары.</p>
    </div>
  </div>
  <template class="n"><p>Если не успели: это домашнее задание. Попросить нейросеть: «Объясни по шагам, как собрать этот Vite-проект и опубликовать на GitHub Pages, я на Windows».</p></template>
</section>''')

after('Практика 3б: React-проект локально', story('04', 'Git push, и&nbsp;код уже проверен', [
  ('Проект', 'Я делаю kornishon: платформу, где разработчики решают реальные задачи и отправляют код через Git.'),
  ('Как работает', 'Человек делает git push, а автоматика сама запускает проверки: линтер, тесты, нагрузку. Никто не носит файлы руками.'),
  ('Для вас', 'Вы сегодня сделали первый шаг того же пути: код лежит в GitHub и сам превращается в сайт. Дальше можно настроить автодеплой.')],
  '<p>Коротко, 1 минута. Если есть время, покажите, как GitHub Actions публикует сайт при каждом пуше (вкладка Actions в репозитории).</p>'))

after('История 04: Git push, и код уже проверен', '''<section class="slide lime" data-title="Показываем ссылки">
  <div class="run"><span>Финал практики</span><span>3 минуты</span></div>
  <div class="grow col center" style="align-items:flex-start">
    <h2 class="h-xl split" style="font-size:150px">Кидайте ссылки в чат</h2>
    <p class="lead" data-a="up" style="--d:5;margin-top:30px;max-width:40ch">Открываем 3-4 сайта на проекторе. Ищем вместе: где получилось, где вылез ИИ-шаблон, что бы вы поправили одной фразой.</p>
  </div>
  <template class="n"><p>Похвалить конкретное. Найти на одном сайте 2-3 признака слопа по памятке 01 и показать, какой фразой их убрать.</p></template>
</section>''')

# ---------- 14. История 05: фриланс, перед финалом ----------
before('Финальная мысль', story('05', 'Клиент покупает заявки, а&nbsp;не&nbsp;сайт', [
  ('Контекст', 'Я выкладываю услуги на биржи фриланса: лендинги, боты, автоматизация, ИИ-агенты для бизнеса.'),
  ('Что понял', 'Заказчику неважно, на чем сайт. Ему важно, сколько придет заявок и как быстро. Продается результат.'),
  ('Для вас', 'Маркетолог, который умеет за вечер собрать лендинг с аналитикой, продает именно результат. Это уже профессия.')],
  '<p>Подставьте свои цифры и случаи: что заказывают, сколько стоит лендинг на биржах, что клиенты спрашивают первым.</p>'))

# ---------- 15. План и интерактив ----------
s = s.replace('<p class="small mono muted" data-a="fade" style="--d:13;margin-top:auto">Минуты указаны справа. Самый большой блок: нейросети, там будем делать сайт вживую.</p>',
              '<p class="small mono muted" data-a="fade" style="--d:13;margin-top:auto">Минуты указаны справа. По ходу пары заполняем общий бриф, в конце генерируем по нему сайт и публикуем на GitHub Pages.</p>')
s = s.replace('<div class="big" data-a="up" style="--d:11"><b>11</b><span>AI-разработка и живые демо</span><i>20</i></div>',
              '<div class="big" data-a="up" style="--d:11"><b>11</b><span>Практика: генерация и деплой</span><i>30</i></div>')
for a,b in [('<span>История веба и дизайна</span><i>8</i>','<span>История веба и дизайна</span><i>6</i>'),('<span>UI/UX и тренды 2026</span><i>10</i>','<span>UI/UX и тренды 2026</span><i>9</i>'),('<span>HTML, CSS, JS</span><i>4</i>','<span>HTML, CSS, JS</span><i>3</i>'),('<span>React и стек</span><i>4</i>','<span>React и стек</span><i>3</i>'),('<span>Скорость и SEO</span><i>7</i>','<span>Скорость и SEO</span><i>5</i>'),('<span>Домены, деплой, закон</span><i>7</i>','<span>Домены, деплой, закон</span><i>5</i>')]:
    assert a in s, a
    s = s.replace(a,b)
s = s.replace(' style2=""', '')
open(P, 'w').write(s)
print('slides:', s.count('<section class="slide'))
