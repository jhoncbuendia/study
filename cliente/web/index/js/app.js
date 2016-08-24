var Index = {
  data: [],
  popular_courses : [],

  init : function(){
    Index.renderIndex();
    Index.bindEvents();

  },

  render: function(data, templateUrl, tempalteId, target, cb){
    $.get(templateUrl).done(function(templates){
      var template = $(templates).filter(tempalteId).html();
      var rendered = Mustache.render(template, {'data': data});
      $(target).html(rendered);
      cb();
    });
  },

  renderIndex: function(){
    $.get(Global.server_url+"index/", function(data){

      Index.data = data;
      Curso.cursos = Index.data[0]['popular_courses'];
      console.log(Curso.cursos);
      Index.renderFilters();
      Index.render(Index.data[0]['popular_courses'], '/curso/templates/cursos.html', '#cursos-template', '#popular_courses',
        function(){
          $(".booking-course").on('click',function(){
            Curso.App.reservar($(this).data('id'));
          });
        }
      );



      //Index.loadIndexTemplate();
    });

  },

  renderFilters(){
    var categories = Index.data[0]['filter_content']['categories'];
    var categories_filter = [];

    var countries = Index.data[0]['filter_content']['countries'];
    var countries_filter = [];

    var levels = Index.data[0]['filter_content']['levels'];
    var levels_filter = [];

    for (var c in categories) {
      categories_filter.push(categories[c]['nombre']);
    }
    for (var c in countries) {
      countries_filter.push(countries[c]['nombre']);
    }
    for (var c in levels) {
      levels_filter.push(levels[c]['nombre']);
    }
    $( "#category" ).autocomplete({
      source: categories_filter
    });
    $( "#level" ).autocomplete({
      source: levels_filter
    });
    $( "#country" ).autocomplete({
      source: countries_filter
    });
  },


  bindEvents: function(){

    $(".src-btn").on('click', function(){
      Curso.cursos = Index.popular_courses;

      var category = $("#category").val() == '' ? "null" :  $("#category").val();
      var level = $("#level").val() == '' ? "null" :  $("#level").val();
      var country = $("#country").val() == '' ? "null" :  $("#country").val();
      var max_price = $("#max_price").val() == '' ? "0" :  $("#max_price").val();

      Curso.Model.find(category.substring(0, 4), level.substring(0, 4), country.substring(0, 4), max_price).then(function(response){
        console.log(response['cursos'].length);
        if(response['cursos'].length == 0){
          $("#intereactive-container").html(response['rendered']);
          $("#intereactive-container").append("<h1 style='text-align: center; margin-bottom: 2em;margin-top: 1em; font-size: 47px;'>Lo sentimos no se encontraron cursos</h1>");
          $('html, body').animate({ scrollTop: $('#intereactive-container').offset().top }, { duration: 2000 });
        }else{
          $("#intereactive-container").html(response['rendered']);
          $('html, body').animate({ scrollTop: $('#intereactive-container').offset().top }, { duration: 2000 });
          $(".booking-course").on('click',function(){
            Curso.App.reservar($(this).data('id'));
          });

          Curso.cursos = Curso.cursos.concat(response['cursos']);
        }

        return false;
      }, function(err){ alert("no se encontraron cursos")});

      return false;
    });

  }
}

Index.init();
