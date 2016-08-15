app.factory('indexCreate', function(){
  function initReserve(){
    $("#back").prop( "disabled", true );    
  }
  return{
    init: function(data){
      initReserve();
      var categories = data[0].filter_content.categories;
      var countries = data[0].filter_content.countries;
      var levels = data[0].filter_content.levels;

      var categories_filter = [];
      var countries_filter = [];
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

      $( "#country" ).autocomplete({
          source: countries_filter
      });

      $( "#level" ).autocomplete({
          source: levels_filter
      });
    }
  }
});
