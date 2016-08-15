app.factory('defaultService', function($http){

    return {

        get: function (url, callback, error) {
            $http.get(url).success(callback).error(error);


        },


        put: function (url, data, callback, error) {
            $http.put(url, data).success(callback).error(error);

        },

        delete: function (url, callback, error) {
            $http.delete(url).success(callback).error(error);

        },

        post: function (url, data, callback, error) {
            $http.post(url, data).success(callback).error(error);

        }

    }
});
