app.factory('IndexModel', ['SERVER_URL','defaultService', function(SERVER_URL, defaultService){
  return {
    get: function(cb){
      defaultService.get(SERVER_URL+"index/",
        function(data){
          cb(data);
        },
        function(err){
          cb(err);
        });

      console.log("geting popular curses");
    }
  }
}])
