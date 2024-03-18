angular.module('frontend').controller('ElementUpdateController', ['$scope', '$http', 'ElementService', '$state', '$stateParams', function($scope, $http, ElementService, $state, $stateParams) {
    $scope.element = {};

    $scope.loadElementData = function() {
        const elementId = $stateParams.elementId; 
        
        ElementService.getById(elementId).then(function(response) {
            if (response.data) { 
                $scope.element = response.data; 
            } else {
                console.error('Element not found');
                alert('Element not found.');
                $state.go('base.element-view'); 
            }
        }).catch(function(error) {
            console.error('Error fetching element data:', error);
            alert('Error fetching element data.');
        });
    };

    $scope.updateElement = function() {
        if ($scope.element && $scope.element.id) {
            const payload = {
                name: $scope.element.name,
                chassis_id: $scope.element.chassis_id 
            };
            ElementService.update($scope.element.id, payload).then(function(response) {
                alert('Element updated successfully!');
                $state.go('base.element-view'); 
            }).catch(function(error) {
                console.error('Error updating element:', error);
                alert('Error updating element.');
            });
        }
    };

    $scope.cancelUpdate = function() {
        $state.go('base.element-view');
    };
    $scope.loadElementData();
}]);
