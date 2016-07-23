Curso.Model = (function(){

    function find(category, level, country, max_price ){
        return  new Promise(function(resolve, reject){

            $.get(Global.dev_url+"cursos/?q=1&categoria="+category+"&nivel="+level+"&pais="+country+"&precio="+max_price, function(resp){
                if(resp['code'] == "404"){
                    reject(resp);
                }else{

                    $.get('/curso/templates/cursos.html', function(templates) {
                        var template = $(templates).filter('#cursos-template').html();
                        var rendered = Mustache.render(template, {"data": resp });
                        var response = [];
                        response['rendered'] = rendered;
                        response['cursos'] = resp;
                        resolve(response);

                    });
                }
            });
        });
    }

    function findById(id){
      var c;
      for(var i in Curso.cursos){
        console.log(Curso.cursos[i]);
        if(Curso.cursos[i]['plan']['id'] == i){          
          console.log(Curso.cursos[i]);
          break;
        }
      }
    }

    return {
        find: find,
        findById: findById
    }


})();
