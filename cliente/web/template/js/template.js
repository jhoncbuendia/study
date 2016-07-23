var Template = {};

Template.Mustache = (function(){

  function render( url, filter, data, cb ){
    $.get( url, function(templates) {
      var template = $(templates).filter( filter ).html();
      var rendered = Mustache.render(template, { "data" : data });
      cb(rendered);
    });
  }

  return {
    render: render,
  }

})();
