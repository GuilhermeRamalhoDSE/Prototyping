angular.module('frontend').controller('ElementController', ['$scope', '$http', 'ElementService', '$state', '$stateParams', 'AuthService', function($scope, $http, ElementService, $state, $stateParams, AuthService) {
    $scope.elementList = [];
    $scope.isSuperuser = AuthService.isSuperuser();

    let chassisId = parseInt($stateParams.chassisId || sessionStorage.getItem('lastChassisId'), 10);
    if (isNaN(chassisId)) {
        console.error('Invalid chassisId');
        return;
    }

    sessionStorage.setItem('lastChassisId', chassisId.toString());

    $scope.newElement = {
        name: "",
        chassis_id: chassisId,
    };

    $scope.loadElements = function() {
        if (!chassisId) {
            console.error('Chassis ID is missing');
            return;
        }
        ElementService.getAll(chassisId).then(function(response) {
            $scope.elementList = response.data;
        }).catch(function(error) {
            console.error('Error fetching elements:', error);
        });
    };

    $scope.goToCreateElement = function() {
        if (chassisId) {
            $state.go('base.element-new', { chassisId: chassisId });
        } else {
            console.error('Chassis ID is missing');
            $state.go('base.element-view', { chassisId: chassisId });
        }
    };

    $scope.createElement = function() {
        if (!chassisId) {
            console.error('Chassis ID is missing');
            return;
        }
        ElementService.create($scope.newElement).then(function(response) {
            alert('Element created successfully!');
            $scope.loadElements();
            $state.go('base.element-view', { chassisId: chassisId });
        }).catch(function(error) {
            console.error('Error creating element:', error);
        });
    };

    $scope.cancelCreate = function() {
        $state.go('base.element-view', { chassisId: chassisId });
    };

    $scope.editElement = function(elementId) {
        $state.go('base.element-update', { chassisId: chassisId, elementId: elementId });
    };

    $scope.detailElement = function(elementId) {
        $state.go('base.component-view', { chassisId: chassisId, elementId: elementId });
    };

    $scope.goBack = function() {
        $state.go('base.chassis-view');
    }; 

    $scope.deleteElement = function(elementId) {
        if (!elementId) {
            console.error('Element ID is missing');
            return;
        }
        var isConfirmed = confirm('Are you sure you want to delete this element?');
        if (isConfirmed) {
            ElementService.delete(elementId).then(function(response) {
                alert('Element deleted successfully!');
                $scope.loadElements();
            }).catch(function(error) {
                console.error('Error deleting element:', error);
            });
        }
    };
    
    $scope.resetForm = function() {
        $scope.newElement = {
            name: "",
            chassis_id: chassisId,
        };
    };

    $scope.loadElements();
}]);
