angular.module('frontend').factory('LicenseService', ['$http', function($http) {
    var service = {};

    var baseUrl = 'http://127.0.0.1:8000/prototyping/api/licenses';

    service.getAll = function() {
        return $http.get(baseUrl);
    };

    service.create = function(licenseData) {
        return $http.post(baseUrl, licenseData);
    };

    service.update = function(id, licenseData) {
        return $http.put(`${baseUrl}/${id}`, licenseData);
    };

    service.delete = function(id) {
        return $http.delete(`${baseUrl}/${id}`);
    };

    return service;
}]);
