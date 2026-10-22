# -*- coding: utf-8 -*-
from base import page, doc, md, checklist
import guide_content as G

T = 4
R = 'Памятка 01 · Анти-ИИ'

VISUAL = [
 ("Фиолетово-синий градиент на фоне, кнопках и заголовке", "Палитра из 2-3 цветов из мира бренда: фасад, упаковка, море за окном. HEX задайте сами"),
 ("Текст с градиентной заливкой", "Один сплошной цвет. Акцент делают размер и насыщенность"),
 ("Inter или Geist на всём", "Шрифт под характер бренда: Onest, Unbounded, Cormorant. Заголовок и текст разные"),
 ("Таблетка-бейдж над заголовком «✨ Новое поколение»", "Уберите или перенесите смысл в сам заголовок"),
 ("Центрированный hero, две кнопки, ряд логотипов, три карточки", "Начните с самого характерного: фото продукта, цена, живое демо, сильная фраза"),
 ("Три одинаковые карточки «иконка в кружке + заголовок + 2 строки»", "Разная форма и размер блоков, конкретные факты, цифры, фото"),
 ("Карточки внутри карточек, одинаковые тени и большие скругления", "Отступы, линии и типографика. Рамка только там, где нужно выделить объект"),
 ("Свечение-ореол на темном фоне, неон, стекло", "Плоские поверхности, бумага, зерно. Глубина только там, где она что-то значит"),
 ("Цветная полоска сбоку у каждой карточки", "Полоска только для статуса или предупреждения"),
 ("Пульсирующие точки и статусы везде", "Анимация только для реальных событий: «открыто сейчас», новая заявка"),
 ("Одинаковое «fade-up» на каждом блоке, пружинящие кнопки", "2-3 продуманные микроанимации. Остальное спокойно"),
 ("Эмодзи вместо иконок и маркеров", "Цифры, аккуратные маркеры, свои рисунки"),
 ("Стоковые 3D-люди, кристаллы, «идеальные» сгенерированные фото", "Свои фото на смартфон, сканы, архивные гравюры"),
 ("Отзывы «Анна К., довольный клиент» с ИИ-аватаром", "Скриншоты с Яндекс Карт или соцсетей, дата, имя, фото"),
]

SECOND = [
 ("Кремовый фон, антиква и терракотовый акцент «для уюта»", "Теплоту дают фото и текст. Фон выбирайте от бренда"),
 ("Почти черный фон и один кислотно-зеленый акцент", "Цвета из продукта, а не из шаблона «техно»"),
 ("Газетные линейки, колонки и ноль скруглений без причины", "Журнальная верстка только для журнального контента"),
 ("Мелкие моно-подписи капсом, «A · B · C» и стрелки у каждой ссылки", "Декор, который не зависит от темы, убираем"),
 ("Номера 01, 02, 03 у блоков, которые не являются шагами", "Нумерация только для настоящей последовательности"),
]

WORDS = ["в современном мире", "играет ключевую роль", "уникальный", "инновационный", "широкий спектр услуг",
 "индивидуальный подход", "команда профессионалов", "откройте для себя", "погрузимся в мир", "давайте разберемся",
 "это не просто X, это Y", "не про X, а про Y", "революционное решение", "новый уровень", "качественно, быстро, надежно",
 "мы ценим каждого клиента", "на рынке более 10 лет", "раскройте потенциал"]

PATTERNS = [
 ("Тире вместо связок, в каждой второй фразе", "Точка, запятая, союз. Перечитайте вслух"),
 ("Конструкция «это не А, это Б»", "Скажите прямо, что делаете и что получит клиент"),
 ("Тройки синонимов: «быстро, удобно, эффективно»", "Одно слово и один факт: «за 40 минут»"),
 ("Парцелляция. Короткие. Обрывки. Для пафоса", "Нормальные предложения разной длины"),
 ("Риторический вопрос в начале каждого блока", "Сразу ответ, цифра, польза"),
 ("Абзацы одинаковой длины и списки по 3 пункта", "Ритм как в живой речи: где-то длинно, где-то одно слово"),
 ("Цифры без источника: «1000+ клиентов, 99% довольны»", "Проверяемые: «312 заказов в 2026, 4,9 на Яндекс Картах»"),
]

BEFORE_AFTER = [
 ("В современном мире кофе играет ключевую роль в жизни каждого. Мы предлагаем уникальный опыт и индивидуальный подход.",
  "Обжариваем по четвергам. Фильтр 180 ₽, эспрессо 150 ₽. Алеутская, 11, с 8:00."),
 ("Наша команда профессионалов обеспечит качественный, быстрый и надежный ремонт.",
  "Меняем экран iPhone за 40 минут при вас. Гарантия 6 месяцев. 1 240 ремонтов в 2026."),
 ("Откройте для себя новый уровень красоты с инновационной косметикой.",
  "Сыворотка с шиповником с Шаморы. 30 мл на 2 месяца. 2 300 ₽."),
]

SOURCES = [
 ("Impeccable: The visible tells of AI design", "https://impeccable.style/slop"),
 ("925 Studios: AI Slop Fonts and Gradients", "https://www.925studios.co/blog/ai-slop-design-tells"),
 ("The Fountain Institute: 7 Tells that a UI is AI-Generated", "https://pages.thefountaininstitute.com/posts/7-tells-that-a-ui-is-ai-generated"),
 ("Capital and Compute: How to Fix AI Slop, Tell by Tell", "https://capitalandcompute.net/blog/fix-ai-slop-design/"),
 ("prg.sh: Why Your AI Keeps Building the Same Purple Gradient Website", "https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website"),
 ("TechCrunch: гайд Википедии «Signs of AI writing»", "https://techcrunch.com/2025/11/20/the-best-guide-to-spotting-ai-writing-comes-from-wikipedia/"),
 ("Unisender: как распознать ИИ-тексты", "https://www.unisender.com/ru/blog/kak-raspoznat-ii-teksty/"),
 ("vc.ru: как распознать текст, написанный нейросетью", "https://vc.ru/2720271-kak-raspoznat-tekst-napisannyi-neirosetyu"),
]

def vs(rows):
    return '<table class="vs"><tr><th>Видно сразу</th><th>Что сделать вместо</th></tr>' + ''.join(
        f'<tr><td><span class="no"></span>{md(a)}</td><td><span class="yes"></span>{md(b)}</td></tr>' for a, b in rows) + '</table>'

def build():
    p1 = f'''
<p class="kick">Памятка 01 из 09</p>
<h1 style="font-size:92pt">Анти-<br>ИИ</h1>
<p class="lead">Нейросеть делает сайт за минуту и всегда одинаково. Клиенты уже узнают ИИ-шаблон с первого экрана и меньше доверяют такому бизнесу. Эта памятка про то, как шаблон увидеть и убрать.</p>
<div class="g2" style="margin-top:8mm">
 <div class="box ink"><p class="kick" style="color:var(--lime);opacity:1">Почему всё фиолетовое</p>
 <p>Когда вышла библиотека компонентов Tailwind, для примеров взяли цвет indigo-500 просто как нейтральную заглушку. Примеры скопировали тысячи разработчиков, нейросети выучили этот код. На размытый промпт «сделай лендинг» модель выдает самое частое, то есть фиолетовый.</p>
 <p class="muted" style="font-size:8pt;margin:0">По разбору prg.sh</p></div>
 <div class="box lime"><p class="kick" style="opacity:1">Главное правило</p>
 <p style="font:700 13pt/1.25 var(--ft)">Приём сам по себе не ошибка. Ошибка: приём без причины.</p>
 <p>Крупный заголовок, наивные рисунки, бегущая строка работают, когда выбраны под бренд. И выдают ИИ, когда стоят «по умолчанию».</p></div>
</div>
<div class="g3" style="margin-top:auto">
 <div class="cell"><span class="k">Как узнают</span><p>Не по одному признаку, а по сумме. 3-5 штампов вместе и сайт считывается как сгенерированный.</p></div>
 <div class="cell"><span class="k">Что не работает</span><p>Детекторы ИИ-текста ненадежны. Решает вкус и конкретика, а не сервис проверки.</p></div>
 <div class="cell"><span class="k">Что работает</span><p>Свои фото, реальные цифры, адрес, имена. Решения бренда до первого промпта.</p></div>
</div>'''
    p2 = f'''<h2>Визуал: 14 штампов</h2>
<p class="muted" style="margin-bottom:4mm">Собрано по разборам дизайн-студий и инструментов проверки «AI slop». Источники на последней странице.</p>
{vs(VISUAL)}
<div class="g2" style="margin-top:auto;gap:5mm">
 <div style="height:40mm;border-radius:5mm;background:linear-gradient(135deg,#6d4dff,#3aa0ff);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:2mm;font-family:Arial,sans-serif;padding:4mm">
  <span style="font-size:6.5pt;background:rgba(255,255,255,.22);padding:1mm 3mm;border-radius:99px">Новое поколение решений</span>
  <b style="font-size:14pt;line-height:1.1">Революционное решение для вашего бизнеса</b>
  <span style="display:flex;gap:2mm;margin-top:1mm"><i style="width:18mm;height:9mm;border-radius:2.5mm;background:rgba(255,255,255,.18)"></i><i style="width:18mm;height:9mm;border-radius:2.5mm;background:rgba(255,255,255,.18)"></i><i style="width:18mm;height:9mm;border-radius:2.5mm;background:rgba(255,255,255,.18)"></i></span>
 </div>
 <div style="height:40mm;display:grid;grid-template-columns:1fr 1.1fr;grid-template-rows:40mm;background:#1a1916;color:#efe9dc;overflow:hidden">
  <img src="../../assets/photos/monk-window.webp" style="width:100%;height:100%;object-fit:cover" alt="">
  <div style="padding:4mm;display:flex;flex-direction:column;gap:1.5mm"><span style="font:500 6pt var(--fm);opacity:.6">Алеутская, 11 · с 8:00</span><b style="font:400 11pt/1 'Yeseva One',serif">Обжариваем по четвергам. Приходите в пятницу.</b><span class="hand" style="font-size:11pt;color:#ff8a4c;margin-top:auto;transform:none">лучшее время: 9 утра</span></div>
 </div>
</div>
<div class="g2" style="gap:5mm;margin-top:1.5mm;margin-bottom:2mm;font:500 7pt var(--fm);opacity:.6"><span>ПО УМОЛЧАНИЮ: ЛЮБОЙ БИЗНЕС</span><span>КОГДА ДУМАЛ ЧЕЛОВЕК: ТОЛЬКО ЭТОТ</span></div>'''
    words = ''.join(f'<span class="word">{w}</span>' for w in WORDS)
    p3 = f'''<h2>Вторая волна штампов</h2>
<p class="muted" style="margin-bottom:3mm">Появляется, когда первую волну уже запретили. Модель уходит в следующий «безопасный» шаблон.</p>
{vs(SECOND)}
<h2 style="margin-top:7mm">Тексты</h2>
<p class="kick" style="margin-bottom:2mm">Слова и обороты, которые выдают нейросеть</p>
<div style="margin-bottom:4mm">{words}</div>
{vs(PATTERNS)}'''
    ba = ''.join(f'''<div class="g2" style="gap:4mm;margin-bottom:3mm"><div class="box p2"><span class="no"></span><span style="font-size:9pt">{a}</span></div><div class="box"><span class="yes"></span><b style="font-size:9.5pt">{b}</b></div></div>''' for a, b in BEFORE_AFTER)
    src = ''.join(f'<div><a href="{u}">{t}</a></div>' for t, u in SOURCES)
    p4 = f'''<h2>Было и стало</h2>
{ba}
<div class="g2" style="margin-top:3mm;gap:6mm">
 <div><h3>Как не попасть в шаблон</h3>
 <ol class="steps">
  <li><span><b>Решения до промпта</b>Шрифт, палитра, принцип сетки, тон. Запишите в 5 строк.</span></li>
  <li><span><b>Направление в каждый промпт</b>Вставляйте эти 5 строк в каждый запрос, чтобы все страницы были одной системой.</span></li>
  <li><span><b>Свои материалы</b>Фото, цены, имена, адрес. Плейсхолдеры помечайте [ВСТАВИТЬ].</span></li>
  <li><span><b>Список запретов</b>Прямо напишите, чего не должно быть. Блок справа.</span></li>
  <li><span><b>Тест 5 секунд</b>Показали, закрыли, спросили: что продают и что делать.</span></li>
 </ol></div>
 <div><h3>Блок запретов для промпта</h3>
 <pre class="prompt">{md(G.PROMPTS["antiai"])}</pre></div>
</div>
<div style="margin-top:auto"><p class="kick" style="margin-bottom:2mm">Источники, проверено 21.10.2026</p><div class="src">{src}</div></div>'''
    pages = [page(p1, R, 'Гайдлайн', 1, T, style='padding-top:16mm'), page(p2, R, 'Визуал', 2, T),
             page(p3, R, 'Вторая волна и тексты', 3, T), page(p4, R, 'Практика', 4, T)]
    return doc('Анти-ИИ', pages)
