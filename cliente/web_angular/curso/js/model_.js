app.factory('CursoModel', ['SERVER_URL','defaultService', function(SERVER_URL, defaultService){
  return {
    filter: function(category, level, country, price, cb){
      defaultService.get(
        SERVER_URL
        +"cursos/?q=1&categoria="+category+"&nivel="+level
        +"&pais="+country+"&precio="+price,
        function(data){
          cb(data);
        });
      }
  }

}])
