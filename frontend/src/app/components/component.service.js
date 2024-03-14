angular.module('frontend').factory('ComponentService', ['$http', function($http) {
    var service = {};
    var baseUrl = 'https://www.prototypingdse.it/prototyping/api/components/';

    service.getAll = function(elementId) {
        return $http.get(baseUrl, { params: { element_id: elementId } });
    };

    service.getById = function(componentId) {
        return $http.get(baseUrl + componentId);
    };

    service.create = function(componentData) {
        return $http.post(baseUrl, componentData, {
            transformRequest: angular.identity,
            headers: {'Content-Type': undefined} 
        });
    };

    service.update = function(id, componentData) {
        return $http.put(baseUrl + id, componentData, {
            transformRequest: angular.identity,
            headers: {'Content-Type': undefined}
        });
    };

    service.delete = function(id) {
        return $http.delete(baseUrl + id);
    };

    return service;
}]);
