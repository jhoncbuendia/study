var Curso = {};

Curso.cursos = [];
Curso.App = (function(){

  function reservar(curso_id){
    var curso_aux = {};
    for(var c in Curso.cursos){
      if(Curso.cursos[c]['id']  == curso_id){
        curso_aux = Curso.cursos[c];
        break;
      }
    }
    Reserva.App.init(curso_aux);
  }

  return {
    reservar: reservar,
  }

})();
