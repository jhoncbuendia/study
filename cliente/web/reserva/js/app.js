var Reserva = {};

Reserva.App = (function(){
  var _step;
  var _curso;
  var _plan;

  function init(curso){
    $("#curse_title").html(curso['nombre']);
    _curso = curso;
    $.get('/reserva/templates/reserva.html', function(templates) {
      var template = $(templates).filter('#reserva-template').html();
      var rendered = Mustache.render(template, {"curso": curso });
      $("#reserva-container").html(rendered);
      $('#myModal').modal('show');
      $("#back").prop( "disabled", true );
      $("#next").prop( "disabled", true );
      bindEvents();
    });
  }

  function searchPlan(id){
    var c = false;
    for( var v in _curso.plan){
      if(_curso.plan[v]['id'] == id){
        c = _curso.plan[v];
        //console.log(c);
        break;
      }
    }
    return c;
  }

  function bindEvents(){
    $("#plan").on("change", function(){
      var plan = searchPlan($("#plan").val());
      if(plan != false){
        $.get('/reserva/templates/plan-detalle.html', function(templates) {
          var template = $(templates).filter('#detalle').html();
          var rendered = Mustache.render(template, {"plan": plan });
          $("#plan-detail").html(rendered);
          updateTotal(parseInt(plan['precio'] - plan['descuento']))
          _step = 1;
          $("#next").prop( "disabled", false );
        });
      }
    })
  }

  function updateTotal(value){
    $("#total").html(value);
  }

  function validate(){

  }

  function next(){

  }

  function back(){

  }

  return{
    init: init
  }

})();
