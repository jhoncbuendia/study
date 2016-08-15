app.controller('indexCreated', ['$scope', 'IndexModel', 'CursoModel', 'indexCreate',
function ($scope, IndexModel, CursoModel, indexCreate) {
  
  IndexModel.get(function(data){
    $scope.courses = data[0].popular_courses;
    indexCreate.init(data);
  });

  $scope.searchCourses = function(){
    var category = $("#category").val() == '' ? "null" :  $("#category").val();
    var level = $("#level").val() == '' ? "null" :  $("#level").val();
    var country = $("#country").val() == '' ? "null" :  $("#country").val();
    var max_price = $("#max_price").val() == '' ? "0" :  $("#max_price").val();

    CursoModel.filter(category,level, country, max_price, function(data){
      $('html, body').animate({ scrollTop: $('#intereactive-container').offset().top }, { duration: 2000 });
      $scope.courses = data;
    })
  }



  $scope.reserve = function(index){
    $scope.current_course = $scope.courses[index];
    if($scope.current_course.plan[0] === undefined){
      $("#next").prop( "disabled", true );
    }else{
      $scope.chosenplan = $scope.current_course.plan[0];
      $scope.current_step = 1;
      $scope.plan_price = $scope.chosenplan.precio;
      $scope.accomodation_price = 0;
      $scope.travel_price = 0;
      updateTotal();

    }

    $('#myModal').modal('show');
  }

  $scope.chosePlan = function (){
    console.log($scope.chosenplan);
    $scope.plan_price = $scope.chosenplan.precio;
    updateTotal();
    $("#next").prop( "disabled", false );
  }

  $scope.backState = function(){
    $scope.current_step --;
    if($scope.current_step == 1){
      $("#back").prop( "disabled", true );
    }else{
      $("#next").prop( "disabled", false );
    }
    console.log($scope.current_step);
  }

  $scope.nextState = function(){
    $scope.current_step ++;
    if($scope.current_step == 4){
      $("#next").prop( "disabled", true );
    }else{
      $("#back").prop( "disabled", false );
    }
    $("#back").prop( "disabled", false );
    console.log($scope.current_step);
  }

  function updateTotal(){
    $scope.total  = $scope.plan_price + $scope.accomodation_price + $scope.travel_price;
  }




}]);
