angular.module('frontend').factory('ChassisService', ['$http', function($http) {
    var baseUrl = 'http://52.50.91.105:8080/prototyping/api/chassis/'; 
    return {
        getChassis: function() {
            return $http.get(baseUrl);
        },
        getChassisById: function(chassisId) {
            return $http.get(baseUrl, { params: { chassis_id: chassisId } });
        },        
        createChassis: function(chassisData) {
            return $http.post(baseUrl, chassisData, {
                transformRequest: angular.identity,
                headers: {'Content-Type': undefined}
            });
        },
        updateChassis: function(chassisId, chassisData) {
            return $http.put(baseUrl + chassisId, chassisData, {
                transformRequest: angular.identity,
                headers: {'Content-Type': undefined}
            });
        },
        deleteChassis: function(chassisId) {
            return $http.delete(baseUrl + chassisId);
        }
    };
}]);
