angular.module('frontend').controller('ComponentUpdateController', ['$scope', 'ComponentService', '$state', '$stateParams', 'AuthService', function($scope, ComponentService, $state, $stateParams, AuthService) {
    $scope.componentId = $stateParams.componentId;
    

    $scope.componentData = {};
    $scope.file = null;

    $scope.loadComponentDetails = function() { 
        if ($scope.componentId) {
            ComponentService.getById($scope.componentId).then(function(response) {
                if (response.data) {
                    $scope.componentData = response.data; 
                } else {
                    console.error('Component not found');
                    alert('Component not found.');
                    $state.go('base.component-view', {elementId: $scope.componentData.element_id});
                }
            }).catch(function(error) {
                console.error('Error fetching component details:', error);
            });
        } else {
            console.log('No component ID provided.');
        }
    };

    $scope.updateComponent = function() {
        var formData = new FormData();

        if ($scope.file) {
            formData.append('file', $scope.file);
        }

        formData.append('data', JSON.stringify($scope.componentData));

        ComponentService.update($scope.componentId, formData).then(function(response) {
            alert('Component updated successfully!');
            $state.go('base.component-view', {elementId: $scope.componentData.element_id});
        }).catch(function(error) {
            console.error('Error updating component:', error);
        });
    };

    $scope.cancelUpdate = function() {
        $state.go('base.component-view', {elementId: $scope.componentData.element_id});
    };

    $scope.loadComponentDetails();
}]);
