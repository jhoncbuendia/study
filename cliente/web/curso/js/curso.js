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

  function renderCursos(cursos, country, lang, mnd,  container, cb ){
    var c = setLanguaje(country, cursos);
    $.get('/curso/templates/cursos_' +lang+'.html', function(templates) {
        console.log(c);
        var template = $(templates).filter('#cursos-template').html();
        var rendered = Mustache.render(template, {"data": c });
        $(container).html(rendered);
        $('#coin').html(country+' '+mnd);
        cb();
    });
  }

  function ajustIdioma(idioma){

  }

  function setLanguaje(country, cursos){

      for(var i in cursos){
          cursos[i]['precio'] = cursos[i]['precio_' + country];
           for (var j in cursos[i]['plan']){
               cursos[i]['plan'][j]['resume'] = cursos[i]['plan'][j]['resume_' + country]
           }
      }

      //ajustIdioma(idioma);
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
