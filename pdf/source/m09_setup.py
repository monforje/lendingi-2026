# -*- coding: utf-8 -*-
import io, html
import qrcode, qrcode.image.svg
from base import page, doc, md

R = 'Памятка 09 · Установка'
BASE = 'https://monforje.github.io/lendingi-2026'

def qr(url):
    img = qrcode.make(url, image_factory=qrcode.image.svg.SvgPathImage, box_size=10, border=1)
    b = io.BytesIO(); img.save(b)
    s = b.getvalue().decode()
    return s[s.find('<svg'):].replace('<svg', '<svg style="width:100%;height:auto;display:block"', 1)

OS = [
 ('Windows 10 / 11', 'PowerShell', 'Win, наберите PowerShell, Enter',
  f'irm {BASE}/setup/win.txt | iex',
  'Вставка правой кнопкой мыши. Windows спросит разрешение: соглашайтесь.'),
 ('macOS', 'Терминал', 'Cmd + Пробел, наберите Терминал',
  f'curl -fsSL {BASE}/setup/install.sh | bash',
  'Появится окно «Инструменты командной строки»: нажмите «Установить» и дождитесь.'),
 ('Linux', 'Терминал', 'Ctrl + Alt + T',
  f'curl -fsSL {BASE}/setup/install.sh | bash',
  'Вставка Ctrl + Shift + V. Попросит пароль для sudo.'),
]

LINKS = [
 ('VS Code', 'редактор кода', 'code.visualstudio.com'),
 ('Git', 'ручная установка', 'git-scm.com/downloads'),
 ('Node.js', 'берите LTS', 'nodejs.org/en/download'),
 ('GitHub', 'регистрация, без VPN', 'github.com/signup'),
 ('GitHub Desktop', 'Git мышкой', 'desktop.github.com'),
 ('GitHub Pages', 'инструкция на русском', 'docs.github.com/ru/pages/quickstart'),
 ('Claude Code', 'ИИ-агент в терминале, платный план', 'code.claude.com/docs/en/setup'),
 ('Cursor', 'редактор с ИИ', 'cursor.com/download'),
 ('Google AI Studio', 'сайт из промпта, бесплатно', 'aistudio.google.com'),
 ('Lovable', 'сайт из промпта', 'lovable.dev'),
 ('GigaChat', 'работает в РФ без VPN', 'giga.chat'),
 ('React Bits', 'готовые анимации', 'reactbits.dev'),
]

TROUBLE = [
 ('«node» не является командой', 'Закройте терминал и откройте новый. PATH подхватывается только в новом окне.'),
 ('«Выполнение сценариев отключено» (npm в PowerShell)', 'Запустите скрипт еще раз или выполните `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.'),
 ('«winget» не найден', 'Скрипт сам скачает установщики. Можно обновить «Установщик приложений» в Microsoft Store.'),
 ('macOS: «command not found: node»', 'Выполните `source ~/.zshrc` или откройте новое окно Терминала.'),
 ('Скачивание зависло или ошибка сети', 'Выключите или включите VPN и запустите команду еще раз. Скрипт можно повторять.'),
 ('Git просит имя и email', '`git config --global user.name "Имя"` и `git config --global user.email "почта"`.'),
]

def build():
    rows = ''
    for name, app, how, cmd, tip in OS:
        rows += f'''<div style="border-top:1.4pt solid var(--ink);padding:3mm 0 3.2mm">
 <div style="display:flex;justify-content:space-between;align-items:baseline;gap:4mm"><h3 style="margin:0;font-size:15pt">{name}</h3><span class="mono" style="font-size:8pt;color:var(--ink2)">{app}: {how}</span></div>
 <pre class="prompt" style="font-size:9.6pt;margin:2.5mm 0 2mm;color:var(--lime)">{html.escape(cmd)}</pre>
 <p style="margin:0;font-size:8.8pt">{tip}</p></div>'''
    p1 = f'''<p class="kick">Памятка 09 из 09</p>
<h1 style="font-size:40pt">Установка за 5 минут</h1>
<p class="lead" style="margin-bottom:4mm;font-size:11.5pt">Одна команда ставит Git, Node.js LTS (node, npm, npx) и VS Code, прописывает PATH и настраивает Git на ветку main. Потом откройте <b>новый</b> терминал.</p>
<div style="display:grid;grid-template-columns:1fr 38mm;gap:7mm;align-items:start">
 <div>{rows}</div>
 <div><div style="background:#fff;padding:2.5mm">{qr(BASE + '/#setup')}</div><p class="mono" style="font-size:7.3pt;margin:2mm 0 0">Наведите камеру: страница с кнопкой «Копировать» и полным текстом скриптов</p></div>
</div>
<div class="box ink" style="margin-top:4mm"><p class="kick" style="color:var(--lime);opacity:1">Проверка</p>
<pre class="prompt" style="padding:0;font-size:9.5pt">node -v      # v24 или новее
npm -v
git --version
code .       # открыть папку в VS Code</pre></div>
<div class="g2" style="gap:6mm;margin-top:4mm">
 <div class="cell"><span class="k">Claude Code, по желанию</span><p style="font-size:8.6pt">Windows: <code>irm https://claude.ai/install.ps1 | iex</code><br>macOS, Linux: <code>curl -fsSL https://claude.ai/install.sh | bash</code><br>Нужен платный план Claude и поддерживаемая страна.</p></div>
 <div class="cell"><span class="k">Скрипт до запуска</span><p style="font-size:8.6pt">Никогда не вставляйте в терминал команды из непроверенных источников. Текст этих скриптов открыт на сайте курса, его можно прочитать перед запуском.</p></div>
</div>'''
    lk = ''.join(f'<tr><td><b>{n}</b></td><td>{d}</td><td class="mono" style="font-size:7.8pt">{u}</td></tr>' for n, d, u in LINKS)
    tr = ''.join(f'<tr><td style="width:62mm"><b>{a}</b></td><td>{md(b)}</td></tr>' for a, b in TROUBLE)
    p2 = f'''<style>.tt td,.tt th{{padding:1.4mm 1.8mm}}</style><h2>Ссылки</h2>
<table class="vs tt" style="font-size:8.6pt;margin-bottom:5mm"><tr><th>Что</th><th>Зачем</th><th>Адрес</th></tr>{lk}</table>
<h2>Если что-то не работает</h2>
<table class="vs tt" style="font-size:8.4pt;margin-bottom:5mm"><tr><th>Ошибка</th><th>Что сделать</th></tr>{tr}</table>
<div class="box lime"><p class="kick" style="opacity:1">Первый проект после установки</p>
<pre class="prompt" style="background:transparent;color:var(--ink);padding:0;font-size:9pt">npm create vite@latest my-site -- --template react
cd my-site
npm install
npm run dev      # сайт на http://localhost:5173</pre></div>'''
    return doc('Установка', [page(p1, R, 'Одна команда', 1, 2), page(p2, R, 'Ссылки и ошибки', 2, 2)])
