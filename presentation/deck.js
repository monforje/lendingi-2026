/* Движок презентации: масштаб сцены, навигация, заметки, оглавление, мини-демо.
   Клавиши: стрелки / пробел / PageUp/PageDown, Home/End, N заметки, M оглавление, F полный экран. */
(function(){
  const stage=document.getElementById('stage');
  const slides=[...stage.querySelectorAll('.slide')];
  const total=slides.length;
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  let cur=0;

  // масштаб
  function fit(){
    const s=Math.min(innerWidth/1920,innerHeight/1080);
    stage.style.transform=`scale(${s})`;
    stage.style.margin=`${(1080*s-1080)/2}px ${(1920*s-1920)/2}px`;
  }
  addEventListener('resize',fit);fit();

  // split: буквы с индексом, слова не разрываются
  document.querySelectorAll('.split').forEach(el=>{
    let i=0;const out=[];
    el.childNodes.forEach(n=>{
      if(n.nodeType===3){
        n.textContent.split(/(\s+)/).forEach(part=>{
          if(!part)return;
          if(/^\s+$/.test(part)){out.push(document.createTextNode(' '));return;}
          const w=document.createElement('span');w.className='w';
          [...part].forEach(c=>{const s=document.createElement('span');s.className='ch';s.style.setProperty('--i',i++);s.textContent=c;w.appendChild(s)});
          out.push(w);
        });
      }else{ // элемент (например <br> или <em>) сохраняем, буквы внутри тоже
        if(n.nodeName==='BR'){out.push(n.cloneNode());return}
        const clone=n.cloneNode(false);
        n.textContent.split(/(\s+)/).forEach(part=>{
          if(!part)return;
          if(/^\s+$/.test(part)){clone.appendChild(document.createTextNode(' '));return}
          const w=document.createElement('span');w.className='w';
          [...part].forEach(c=>{const s=document.createElement('span');s.className='ch';s.style.setProperty('--i',i++);s.textContent=c;w.appendChild(s)});
          clone.appendChild(w);
        });
        out.push(clone);
      }
    });
    el.textContent='';out.forEach(o=>el.appendChild(o));
  });

  // заметки и оглавление
  const notes=document.getElementById('notes'),menu=document.getElementById('menu'),ol=menu.querySelector('ol');
  slides.forEach((s,i)=>{
    const li=document.createElement('li');li.value=i+1;
    li.textContent=s.dataset.title||('Слайд '+(i+1));
    if(s.dataset.chapter)li.className='ch';
    li.onclick=()=>{go(i);menu.hidden=true};ol.appendChild(li);
  });

  // счетчики
  function count(slide){
    slide.querySelectorAll('[data-count]').forEach(el=>{
      const to=parseFloat(el.dataset.count),dec=(el.dataset.count.split('.')[1]||'').length,suf=el.dataset.suf||'';
      if(reduce||!window.anime){el.textContent=fmt(to,dec)+suf;return}
      const o={v:0};
      anime.animate(o,{v:to,duration:1600,delay:300,ease:'out(3)',onUpdate:()=>{el.textContent=fmt(o.v,dec)+suf}});
    });
  }
  const fmt=(v,d)=>v.toLocaleString('ru-RU',{minimumFractionDigits:d,maximumFractionDigits:d});

  function go(n){
    n=Math.max(0,Math.min(total-1,n));
    slides[cur].classList.remove('active');
    cur=n;const s=slides[cur];s.classList.add('active');
    document.querySelector('#ui .count').textContent=`${cur+1} / ${total}`;
    document.querySelector('#ui .prog').style.setProperty('--p',(cur+1)/total);
    notes.querySelector('div').innerHTML=s.querySelector('template.n')?s.querySelector('template.n').innerHTML:'<p>Заметок нет.</p>';
    notes.querySelector('h5').textContent=`Заметки · ${cur+1}. ${s.dataset.title||''}`;
    count(s);
    s.dispatchEvent(new CustomEvent('enter'));
    try{history.replaceState(null,'','#s'+(cur+1))}catch(e){}
  }
  window.deckGo=go;

  // навигация
  addEventListener('keydown',e=>{
    if(e.target.closest('input,textarea,[contenteditable]'))return;
    const k=e.key;
    if(['ArrowRight','PageDown',' ','Enter'].includes(k)){e.preventDefault();go(cur+1)}
    else if(['ArrowLeft','PageUp','Backspace'].includes(k)){e.preventDefault();go(cur-1)}
    else if(k==='Home')go(0);else if(k==='End')go(total-1);
    else if(k==='n'||k==='N'||k==='т'||k==='Т')notes.hidden=!notes.hidden;
    else if(k==='m'||k==='M'||k==='ь'||k==='Ь')menu.hidden=!menu.hidden;
    else if(k==='f'||k==='F'||k==='а'||k==='А')fs();
    else if(k==='Escape'){menu.hidden=true;notes.hidden=true}
  });
  function fs(){const d=document.documentElement;if(!document.fullscreenElement){(d.requestFullscreen&&d.requestFullscreen().catch(()=>{}))}else document.exitFullscreen&&document.exitFullscreen()}
  document.getElementById('bPrev').onclick=()=>go(cur-1);
  document.getElementById('bNext').onclick=()=>go(cur+1);
  document.getElementById('bNotes').onclick=()=>notes.hidden=!notes.hidden;
  document.getElementById('bMenu').onclick=()=>menu.hidden=false;
  document.getElementById('bFs').onclick=fs;
  menu.querySelector('.close button').onclick=()=>menu.hidden=true;

  // клик по сцене: правая треть вперед, левая назад (кроме интерактивных элементов)
  stage.addEventListener('click',e=>{
    if(e.target.closest('a,button,input,label,.interactive'))return;
    const r=stage.getBoundingClientRect();const x=(e.clientX-r.left)/r.width;
    if(x>.66)go(cur+1);else if(x<.2)go(cur-1);
  });
  // свайпы
  let tx=null,ty=null;
  let uiT=null;addEventListener('touchstart',e=>{document.body.classList.add('touch');clearTimeout(uiT);uiT=setTimeout(()=>{if(!document.querySelector('#ui:focus-within'))document.body.classList.remove('touch')},3500);tx=e.touches[0].clientX;ty=e.touches[0].clientY},{passive:true});
  addEventListener('touchend',e=>{if(tx===null)return;const dx=e.changedTouches[0].clientX-tx,dy=e.changedTouches[0].clientY-ty;if(Math.abs(dx)>50&&Math.abs(dx)>Math.abs(dy))go(cur+(dx<0?1:-1));tx=null},{passive:true});

  // подсказка
  const hint=document.getElementById('hint');setTimeout(()=>hint.style.opacity=0,4500);

  // ---------- мини-демо ----------
  // Magnet (по мотивам reactbits Magnet)
  document.querySelectorAll('.magnet').forEach(m=>{
    const area=m.parentElement;
    area.addEventListener('mousemove',e=>{
      const r=m.getBoundingClientRect(),sc=r.width/m.offsetWidth;
      const dx=(e.clientX-(r.left+r.width/2))/sc,dy=(e.clientY-(r.top+r.height/2))/sc;
      m.style.transform=`translate(${dx*.35}px,${dy*.35}px)`;
    });
    area.addEventListener('mouseleave',()=>m.style.transform='');
  });
  // Scrambled text (по мотивам reactbits Scrambled Text / Decrypted Text)
  const glyphs='АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ#%&*+=<>/\\0123456789';
  function scramble(el){
    const final=el.dataset.text||el.textContent;el.dataset.text=final;let f=0;
    const tick=()=>{f++;el.textContent=[...final].map((c,i)=>c===' '?' ':(i<f/2?c:glyphs[Math.random()*glyphs.length|0])).join('');if(f/2<final.length)requestAnimationFrame(tick)};
    if(reduce){el.textContent=final;return}tick();
  }
  document.querySelectorAll('.scramble').forEach(el=>{el.addEventListener('mouseenter',()=>scramble(el))});
  slides.forEach(s=>s.addEventListener('enter',()=>s.querySelectorAll('.scramble').forEach(scramble)));

  // HTML / CSS / JS демо
  document.querySelectorAll('.hcj').forEach(box=>{
    const btns=box.querySelectorAll('[data-layer]'),target=box.querySelector('.hcj-target'),code=box.querySelector('.hcj-code');
    const codes={
      html:'<button>Записаться</button>',
      css:'<button>Записаться</button>\n\nbutton {\n  background: #2335FF;\n  color: white;\n  border-radius: 999px;\n  padding: 28px 56px;\n}',
      js:'<button>Записаться</button>\n\nbutton { ... }\n\nbutton.onclick = () => {\n  button.textContent = "Готово! Ждем вас";\n}'
    };
    btns.forEach(b=>b.addEventListener('click',()=>{
      btns.forEach(x=>x.classList.toggle('on',x===b));
      target.className='hcj-target '+b.dataset.layer;target.textContent='Записаться';
      code.textContent=codes[b.dataset.layer];
    }));
    target.addEventListener('click',()=>{if(target.classList.contains('js')){target.textContent='Готово! Ждем вас';if(window.anime&&!reduce)anime.animate(target,{scale:[1,1.12,1],duration:500})}});
  });

  // старт
  const m=location.hash.match(/^#s(\d+)$/);
  go(m?parseInt(m[1],10)-1:0);
})();

/* ASCII-рендер фото на canvas (по мотивам reactbits ASCII Text). Картинка встроена как data URI,
   поэтому работает и при открытии файла с диска. */
(function(){
  const chars=' .:-=+*#%@';
  document.querySelectorAll('canvas.ascii-cv').forEach(cv=>{
    const ctx=cv.getContext('2d');const img=new Image();
    img.onload=()=>{
      const N=img.width;const off=document.createElement('canvas');off.width=N;off.height=N;
      const o=off.getContext('2d');o.drawImage(img,0,0,N,N);
      let data;try{data=o.getImageData(0,0,N,N).data}catch(e){ctx.drawImage(img,0,0,cv.width,cv.height);return}
      const cols=76,cell=cv.width/cols;let t0=performance.now(),raf;
      function frame(now){
        const t=(now-t0)/1000;ctx.fillStyle='#0E0F12';ctx.fillRect(0,0,cv.width,cv.height);
        ctx.globalAlpha=.55;ctx.filter='grayscale(1) contrast(1.1)';ctx.drawImage(img,0,0,cv.width,cv.height);ctx.filter='none';ctx.globalAlpha=1;
        ctx.font=`700 ${cell*1.05}px "JetBrains Mono",monospace`;ctx.textBaseline='top';
        for(let y=0;y<cols;y++)for(let x=0;x<cols;x++){
          const sx=Math.floor(x/cols*N),sy=Math.floor(y/cols*N),i=(sy*N+sx)*4;
          const r=data[i],g=data[i+1],b=data[i+2],l=(r*.3+g*.59+b*.11)/255;
          const reveal=Math.min(1,Math.max(0,t*1.4-(y/cols)*1.2));
          if(reveal<=0)continue;
          const warm=r>g+28&&r>b+40; // рыжая шерсть коровы
          const ch=chars[Math.min(chars.length-1,Math.floor(l*chars.length))];
          if(warm){ctx.fillStyle=`rgba(255,110,190,${.4+.6*reveal})`;ctx.fillRect(x*cell,y*cell,cell,cell);ctx.fillStyle='#0E0F12'}
          else ctx.fillStyle=`rgba(232,232,232,${.55*reveal})`;
          ctx.fillText(ch,x*cell+cell*.18,y*cell);
        }
        if(t<3)raf=requestAnimationFrame(frame);
      }
      const slide=cv.closest('.slide');
      const start=()=>{cancelAnimationFrame(raf);t0=performance.now();raf=requestAnimationFrame(frame)};
      slide.addEventListener('enter',start);if(slide.classList.contains('active'))start(); else frame(t0+5000);
    };
    img.src=cv.dataset.src;
  });
})();

/* Таймер практики: клик запускает и ставит на паузу, двойной клик сбрасывает. */
(function(){
  document.querySelectorAll('.timer').forEach(t=>{
    const total=(+t.dataset.min||10)*60;let left=total,id=null;
    const draw=()=>{t.textContent=String(Math.floor(left/60)).padStart(2,'0')+':'+String(left%60).padStart(2,'0');t.classList.toggle('done',left<=0)};
    t.addEventListener('click',()=>{if(id){clearInterval(id);id=null;return}id=setInterval(()=>{left=Math.max(0,left-1);draw();if(!left){clearInterval(id);id=null}},1000)});
    t.addEventListener('dblclick',()=>{clearInterval(id);id=null;left=total;draw()});
    draw();
  });
})();
