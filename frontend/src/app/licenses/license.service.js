angular.module('frontend').factory('LicenseService', ['$http', function($http) {
    var service = {};

    var baseUrl = 'http://52.50.91.105:8080/prototyping/api/licenses/';

    service.getAll = function() {
        return $http.get(baseUrl);
    };

    service.getById = function(licenseId) {
        return $http.get(baseUrl, {
            params: { license_id: licenseId } 
        });
    };
    
    service.create = function(licenseData) {
        return $http.post(baseUrl, licenseData);
    };

    service.update = function(id, licenseData) {
        return $http.put(`${baseUrl}${id}`, licenseData);
    };

    service.delete = function(id) {
        return $http.delete(`${baseUrl}${id}`);
    };

    return service;
}]);
