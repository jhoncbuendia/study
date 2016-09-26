var Idioma = (function(){

    _UIidioma = [
        {
            pais: 'col',
            tags : [
                {
                    'id': 'msg',
                    'value': 'UN LUGAR DONDE QUIERES ESTUDIAR'
                },
                {
                    'id': 'text1',
                    'value': 'A tu medida Vive en propiedades diseñadas especialmente para la vida estudiantil.'
                },
                {
                    'id': 'country',
                    'value': 'PAIS'
                },
                {
                    'id': 'btn_srch',
                    'value': 'Buscar'
                },
                {
                    'id': 'coin',
                    'value': 'COP'
                },

                {
                    'id': 'hxs',
                    'value': 'Horas x Semana'
                },
                {
                    'id': 'reserve',
                    'value': 'Reservar'
                },

                {
                    'id': 'set_plan_title',
                    'value': 'Configure su plan'
                },

                {
                    'id': 'reserve_title',
                    'value': 'Siga los pasos para completar su reserva del'
                },
            ]
        },
        {
            pais: 'ns',
            tags : [
                {
                    'id': 'msg',
                    'value': 'A PLACE WHERE YOU WANT TO STUDY'
                },
                {
                    'id': 'text1',
                    'value': 'A measure your lives in properties specially designed for student life'
                },
                {
                    'id': 'country',
                    'value': 'COUNTRY'
                },
                {
                    'id': 'btn_srch',
                    'value': 'Search'
                },
                {
                    'id': 'coin',
                    'value': 'USD'
                },

                {
                    'id': 'hxs',
                    'value': 'Hours per week'
                },
                {
                    'id': 'reserve',
                    'value': 'Reserve'
                },

                {
                    'id': 'set_plan_title',
                    'value': 'Set your plan'
                },

                {
                    'id': 'reserve_title',
                    'value': 'Follow the steps to complete your booking'
                },

                {
                    'id': 'next',
                    'value': 'Next'
                },
                {
                    'id': 'back',
                    'value': 'Back'
                },
            ]
        }
    ];


    function renderIdioma(pais){
            _UIidioma.forEach(function(array){
                if(array['pais'] == pais){
                    array['tags'].forEach(function(array){
                        $("#" + array['id']).text(array['value']);
                    })
                    return;
                }
            });
    }



    function init(idioma){
        renderIdioma(idioma);

    }

    return {
        init : init,
        renderIdioma : renderIdioma
    }

})();
