// 全站静态搜索：输入关键字 -> 章节/页面匹配 -> 直达锚点
(function(){
  var IDX = null, box = document.getElementById('qk'), res = document.getElementById('qres');
  if (!box) return;
  function esc(s){var d=document.createElement('div');d.textContent=s;return d.innerHTML}
  function load(cb){ if(IDD) ; if(IDX) return cb();
    fetch('/search_index.json').then(function(r){return r.json()}).then(function(j){IDX=j;cb()}).catch(function(){res.innerHTML=''}) }
  function score(e, q){
    var s=0
    if(e.t.indexOf(q)>=0) s+=10
    if(e.s.indexOf(q)>=0) s+=8
    if(e.x.indexOf(q)>=0) s+=3
    return s
  }
  function run(){
    var q=box.value.trim().toLowerCase()
    if(q.length<2){res.innerHTML='';return}
    load(function(){
      var out=[]
      for(var i=0;i<IDX.length;i++){var e=IDX[i];var sc=score(e,q);if(sc>0)out.push([sc,e])}
      out.sort(function(a,b){return b[0]-a[0]})
      var top=out.slice(0,20), h=top.map(function(p){
        var e=p[1]
        var url='/'+e.u+(e.a?('#'+e.a):'')
        return '<a class="qi" href="'+url+'"><b>'+esc(e.s)+'</b><span class="qp">'+esc(e.t)+'</span></a>'
      }).join('')
      res.innerHTML = h || '<span class="qi">无匹配</span>'
    })
  }
  box.addEventListener('input', run)
  box.addEventListener('focus', run)
})();

// ===== 侧栏折叠（内容全屏） =====
(function(){
  var lay = document.querySelector('.layout');
  if(!lay) return;
  var KEY = 'sidebar-collapsed';
  var b = document.createElement('button');
  b.className = 'tgl'; b.title = '折叠/展开侧栏';
  function sync(){
    var off = localStorage.getItem(KEY) === '1';
    lay.classList.toggle('full', off);
    b.textContent = off ? '\u25B6 \u5c55\u5f00' : '\u25C0 \u6536\u8d77';
  }
  b.onclick = function(){
    localStorage.setItem(KEY, localStorage.getItem(KEY) === '1' ? '0' : '1');
    sync();
  };
  document.body.appendChild(b);
  sync();
})();

// ===== 图片灯箱（点击放大 + 缩放按钮） =====
(function(){
  var box = null, img = null, scale = 1;
  function ensure(){
    if(box) return;
    box = document.createElement('div');
    box.className = 'lb';
    img = document.createElement('img');
    var bar = document.createElement('div'); bar.className = 'lbb';
    function mkBtn(t, fn){ var x = document.createElement('button'); x.textContent = t; x.onclick = fn; return x; }
    function zoom(f){ scale = Math.min(6, Math.max(0.2, scale * f)); img.style.transform = 'scale(' + scale + ')'; }
    bar.appendChild(mkBtn('\uff0b \u653e\u5927', function(){ zoom(1.25) }));
    bar.appendChild(mkBtn('\uff0d \u7f29\u5c0f', function(){ zoom(0.8) }));
    bar.appendChild(mkBtn('\u21ba \u590d\u4f4d', function(){ scale = 1; img.style.transform = ''; }));
    bar.appendChild(mkBtn('\u2715 \u5173\u95ed', close));
    box.appendChild(img); box.appendChild(bar);
    box.onclick = function(e){ if(e.target === box) close(); };
    document.body.appendChild(box);
    document.addEventListener('keydown', function(e){ if(e.key === 'Escape' && box.style.display === 'flex') close(); });
    function close(){ box.style.display = 'none'; }
  }
  document.addEventListener('click', function(e){
    var t = e.target;
    if(t.tagName === 'IMG' && t.closest('main') && !t.closest('.lb')){
      ensure();
      img.src = t.src; scale = 1; img.style.transform = '';
      box.style.display = 'flex';
      e.preventDefault();
    }
  });
})();
