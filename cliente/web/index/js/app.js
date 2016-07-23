var Index = {

    data: [],
    popular_courses : [],

    loadData: function(){

        $.get(Global.server_url+"index/", function(resp){

            Index.data = resp;
            Index.loadFiltersData();
            Index.loadIndexTemplate();

        });

    },

    loadIndexTemplate : function(){

        var popular_courses = Index.data[0]['popular_courses'];

        Template.Mustache.render('/curso/templates/cursos.html', '#cursos-template', popular_courses,
        function(rendered){
            Index.popular_courses = popular_courses;
            Curso.cursos = Index.popular_courses;
            $("#popular_courses").html(rendered);
        }
    );


},

loadFiltersData(){

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


btn_search_handler: function(){
    $(".src-btn").click(function(){

        Curso.cursos = Index.popular_courses;

        var category = $("#category").val() == '' ? "null" :  $("#category").val();
        var level = $("#level").val() == '' ? "null" :  $("#level").val();
        var country = $("#country").val() == '' ? "null" :  $("#country").val();
        var max_price = $("#max_price").val() == '' ? "0" :  $("#max_price").val();

        var promise = Curso.Model.find(category, level, country, max_price);

        promise.then(function(response){
            $("#intereactive-container").html(response['rendered']);
            $('html, body').animate({ scrollTop: $('#intereactive-container').offset().top }, { duration: 2000 });

            Curso.cursos = Curso.cursos.concat(response['cursos']);
            return false;

        }, function(err){ alert("no se encontraron cursos")});

        return false;
    });
}
}

Index.loadData();
Index.btn_search_handler();
