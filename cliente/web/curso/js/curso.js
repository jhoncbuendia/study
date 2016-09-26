var Curso = (function(){
  var _cursos;

  function getPopular(){
    return $.get(server_url + 'cursos/?popular=1');
  }


  function getCurso(cursos, id){
    var curso_aux = {};
    for(var c in cursos){
      if(cursos[c]['id']  == id){
        curso_aux = cursos[c];
        curso_aux['precio'] = curso_aux['precio_' + window.window._currentMoneda]
        break;
      }
    }
    return curso_aux;
  }

  function filter(category, level, country, max_price, moneda ){
      return $.get( server_url + "cursos/?q=1&categoria="+category+"&nivel="+level+"&pais="+country+"&precio="+max_price+"&moneda="+moneda);
  }

  function renderCursos(cursos, container, cb ){
    $.get('/curso/templates/cursos.html', function(templates) {
        var template = $(templates).filter('#cursos-template').html();
        var rendered = Mustache.render(template, {"data": cursos });
        $(container).html(rendered);
        cb();
    });
  }

  function ajustIdioma(idioma){

  }

  function setLanguaje(cursos, pais){
      console.log(cursos);
      var moneda;
      var idioma;

      switch (pais) {
          case "col":
                moneda = "cop";
                idioma = "es";
              break;
          case "ns":
                moneda = "usd";
                idioma = "ing";
                break;
          default:

      }
      console.log('precio_' + moneda);
      for(var i in cursos){
          cursos[i]['precio'] = cursos[i]['precio_' + moneda];
           for (var j in cursos[i]['plan']){
               cursos[i]['plan'][j]['resume'] = cursos[i]['plan'][j]['resume_' + idioma]
           }
      }

      ajustIdioma(idioma);
      return cursos;
  }

  return {
    getPopular : getPopular,
    renderCursos: renderCursos,
    getCurso: getCurso,
    filter: filter,
    setLanguaje : setLanguaje,

  }

})();
