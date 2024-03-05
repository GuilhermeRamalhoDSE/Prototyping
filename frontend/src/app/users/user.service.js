angular.module('frontend').factory('UserService', ['$http', function($http) {
    var service = {};

    var baseUrl = 'http://127.0.0.1:8000/prototyping/api/users/';

    service.getAllUsers = function() {
        return $http.get(baseUrl);
    };

    service.createUser = function(userData) {
        return $http.post(baseUrl, userData);
    };

    service.updateUser = function(id, userData) {
        return $http.put(`${baseUrl}${id}`, userData);
    };

    service.deleteUser = function(id) {
        return $http.delete(`${baseUrl}${id}`);
    };

    return service;
}]);
