angular.module('frontend').factory('ElementService', ['$http', function($http) {
    var service = {};
    var baseUrl = 'http://127.0.0.1:8000/prototyping/api/elements/';

    service.getAll = function(chassisId) {
        return $http.get(baseUrl, { params: { chassis_id: chassisId } });
    };

    service.getById = function(elementId) {
        return $http.get(baseUrl + elementId + '/');
    };

    service.create = function(elementData) {
        return $http.post(baseUrl, elementData);
    };

    service.update = function(id, elementData) {
        return $http.put(baseUrl + id + '/', elementData);
    };

    service.delete = function(id) {
        return $http.delete(baseUrl + id + '/');
    };

    return service;
}]);
