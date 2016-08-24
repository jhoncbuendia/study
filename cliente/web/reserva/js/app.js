var Reserva = {};

Reserva.App = (function(){
  var _step;
  var _curso;
  var _plan;
  var _current_step = 1;
  var _reserva_info = {};
  function init(curso){


    $("#curse_title").html(curso['nombre']);
    _curso = curso;
    _reserva_info['curso_id'] = curso['id'];
    console.log(curso);
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

        _reserva_info['plan'] = plan;
        console.log(_reserva_info);

        $.get('/reserva/templates/plan-detalle.html', function(templates) {
          var template = $(templates).filter('#detalle').html();
          var rendered = Mustache.render(template, {"plan": plan });
          $("#plan-detail").html(rendered);
          updateTotal(parseInt(plan['precio'] - plan['descuento']))
          _current_step = 1;
          $("#next").prop( "disabled", false );
        });
      }
    })

    $("#next").click(function(){
      if(_current_step < 5){


        var info_form_complete = true;

        if ( _current_step == 2){

          if($("#nombre").val() == ""){
            $("#alert").css({'display': 'block'});
            $("#alert").text("Porfavor ingrese su nombre");
            info_form_complete = false;
          }

          if($("#apellido").val() == ""){
            $("#alert").css({'display': 'block'});
            $("#alert").text("Porfavor ingrese su apellido");
            info_form_complete = false;
          }

          if($("#correo").val() == ""){
            $("#alert").css({'display': 'block'});
            $("#alert").text("Porfavor ingrese su correo");
            info_form_complete = false;
          }

          if($("#pasaporte").val() == ""){
            $("#alert").css({'display': 'block'});
            $("#alert").text("Porfavor ingrese su pasaporte");
            info_form_complete = false;
          }

          if($("#whatsapp").val() == ""){
            $("#alert").css({'display': 'block'});
            $("#alert").text("Porfavor ingrese su whatsapp");
            info_form_complete = false;
          }


        }

        if(info_form_complete){
          _current_step ++;

        }

        if(_current_step == 1){
          $("#back").prop( "disabled", true );
        }else{
          $("#back").prop( "disabled", false );
        }

        changeStep();

      }


    })

    $("#back").click(function(){
        _current_step --;
        if(_current_step == 1){
          $("#back").prop( "disabled", true );
        }else{
          $("#back").prop( "disabled", false );
          $("#next").prop( "disabled", false );
          $("#next").text("Siguiente")
        }
        changeStep();
      })
  }

  function changeStep(){
    switch (_current_step) {
      case 1:
        $("#step1").css({'display': 'block'})
        $("#step2").css({'display': 'none'})
        $("#step3").css({'display': 'none'})
        $("#step4").css({'display': 'none'})

        break;
      case 2:
        $("#step2").css({'display': 'block'})
        $("#step1").css({'display': 'none'})
        $("#step3").css({'display': 'none'})
        $("#step4").css({'display': 'none'})
        break;
      case 3:
        step2completed();
        $("#step3").css({'display': 'block'})
        $("#step2").css({'display': 'none'})
        $("#step1").css({'display': 'none'})
        $("#step4").css({'display': 'none'})
        break;
      case 4:
        step3completed();
        $("#step4").css({'display': 'block'})
        $("#step1").css({'display': 'none'})
        $("#step3").css({'display': 'none'})
        $("#step2").css({'display': 'none'})
        $("#next").text("Finalizar")
        _reserva_info['visa'] = $("input[name=visa]:checked").val();
        break;
      case 5:
        _reserva_info['alojamiento'] = $("input[name=alojamiento]:checked").val();
        console.log(_reserva_info);

        $("#alert").css({'display': 'block'});
        $("#alert").html("<img src='../../asset/loading.gif' style='width: 100px; margin: 0 auto;  display: block;' /> ");

        $.post( Global.server_url + 'reservas/', {"data" : JSON.stringify( _reserva_info)})
          .done(function( data ) {
            console.log(data);
            $("#alert").text("Se te ha enviado un correo con toda la informacion para adquirir el curso")
            $("#alert").css({'display': 'block'});
        })

        $("#back").prop( "disabled", true );
        $("#next").prop( "disabled", true );
        break;


    }
  }


  function updateTotal(value){
    $("#total").html(value);
  }

  function completeWizard(){
    console.log("completing wizard")
  }

  function step2completed(){
      var personal_info = $("#personal-form").serializeArray();
      var data = {};
      for(var index in personal_info){
        data[personal_info[index]['name']] = personal_info[index]['value'];
      }

      _reserva_info['informacion_personal'] = data;
      console.log(_reserva_info);
  }

  function step3completed(){
    var viaje_info = $("#viaje-form").serializeArray();
    var data = {};
    for(var index in viaje_info){
      data[viaje_info[index]['name']] = viaje_info[index]['value'];
    }

    $.get('/reserva/templates/alojamiento.html', function(templates) {
      var template = $(templates).filter('#alojamiento').html();
      var rendered = Mustache.render(template, {"curso": _curso });
      $("#alojamiento-container").html(rendered);
    });

  }

  return{
    init: init
  }

})();
