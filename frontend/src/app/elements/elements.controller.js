angular.module('frontend').controller('ElementController', ['$scope', '$http', 'ElementService', '$state', '$stateParams', 'AuthService', function($scope, $http, ElementService, $state, $stateParams, AuthService) {
    $scope.elementList = [];
    $scope.isSuperuser = AuthService.isSuperuser();

   
    $scope.newElement = {
        name: "",
        chassis_id: $stateParams.chassisId, 
    };

    console.log('Current $stateParams:', $stateParams);
    console.log('Current chassisId:', $stateParams.chassisId);

    $scope.loadElements = function() {
        console.log("Checking chassisId availability:", $stateParams.chassisId);
        if (!$stateParams.chassisId) {
            console.error('Chassis ID is missing');
            return; 
        }
        console.log('Loading elements for chassisId:', $stateParams.chassisId);
        ElementService.getAll($stateParams.chassisId).then(function(response) { 
            console.log('Elements loaded:', response.data);
            $scope.elementList = response.data;
        }).catch(function(error) {
            console.error('Error fetching elements:', error);
        });
    };

    $scope.createElement = function() {
        console.log("Initial $stateParams check:", $stateParams);
        ElementService.create($scope.newElement).then(function(response) {
            alert('Element created successfully!');
            $scope.loadElements();
            $state.go('base.element-view');
        }).catch(function(error) {
            console.error('Error creating element:', error);
        });
    };

    $scope.cancelCreate = function() {
        $state.go('base.element-view');
    };

    $scope.editElement = function(elementId) {
        $state.go('base.element-update', { elementId: elementId });
    };    

    $scope.resetForm = function() {
        $scope.newElement = {
            name: "",
            chassis_id: $stateParams.chassisId,
        };
    };

    $scope.loadElements();
}]);
