

var Index = (function(){
    var _country = localStorage.getItem("country");
    var _lang = localStorage.getItem("lang");
    var _mnd = localStorage.getItem("mnd");

    function getQueryParams(qs) {
        qs = qs.split('+').join(' ');

        var params = {},
            tokens,
            re = /[?&]?([^=]+)=([^&]*)/g;

        while (tokens = re.exec(qs)) {
            params[decodeURIComponent(tokens[1])] = decodeURIComponent(tokens[2]);
        }

        return params;
    }


    function init(){


        render();
        eventHandler();

    }

    function render(){
        renderPopularCourses();
    }

    function eventHandler(){

        $(".idioma-btn-selected").click(function(){
            $(".idioma-btn").css({'display': 'block'});
        });


        $(".src-btn").on('click', function(){
            renderFilteredCourses();
            return false;
        });
    }



    function renderPopularCourses(){
        console.log(_lang);
        console.log(_mnd);
            Curso.getPopular().done(function(cursos){
                Curso.renderCursos(cursos, _country, _lang, _mnd,  "#popular_courses", function(){

                    $(".booking-course").on('click',function(){
                        Reserva.init(Curso.getCurso(cursos, $(this).data('id')), _country, _lang, _mnd);
                    });
                });

            });

    }

    function renderFilteredCourses(){

        var category = $("#category").val() == '' ? "null" :  $("#category").val();
        var level = $("#level").val() == '' ? "null" :  $("#level").val();
        var country = $("#country").val() == '' ? "null" :  $("#country").val();
        var max_price = $("#max_price").val() == '' ? "0" :  $("#max_price").val();
        var moneda = "";

        Curso.filter(category.substring(0, 4), level.substring(0, 4), country.substring(0, 4), max_price, moneda)
        .done(function(cursos){
            if(cursos.length == 0){
                $("#popular_courses").html("<h1 style='text-align: center; margin-bottom: 2em;margin-top: 1em; font-size: 47px;'>Lo sentimos no se encontraron cursos</h1>");
                $('html, body').animate({ scrollTop: $('#intereactive-container').offset().top }, { duration: 2000 });
                return false;
            }else{

                cursos = Curso.setLanguaje(cursos, _pais);
                Curso.renderCursos(cursos, "#popular_courses", function(){
                    Idioma.renderIdioma(_pais);
                    $(".booking-course").on('click',function(){
                        Reserva.init(Curso.getCurso(cursos, $(this).data('id')), _pais);
                    });
                    $('html, body').animate({ scrollTop: $('#popular_courses').offset().top }, { duration: 2000 });
                });
            }
            return false;
        });

        return false;
    }

    return {
        init : init ,

    }

})();


(function(){
    $(document).ready(
        function(){
            Index.init();
        }
    );
})();
