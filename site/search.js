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
