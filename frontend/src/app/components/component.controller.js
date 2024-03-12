angular.module('frontend').controller('ComponentController', ['$scope', 'ComponentService', '$state', '$stateParams', 'AuthService', function($scope, ComponentService, $state, $stateParams, AuthService) {
    $scope.componentList = [];
    $scope.isSuperuser = AuthService.isSuperuser();

    let elementId = parseInt($stateParams.elementId || sessionStorage.getItem('lastElementId'), 10);

    if (isNaN(elementId)) {
        console.error('Invalid elementId');
        return;
    }

    sessionStorage.setItem('lastElementId', elementId.toString());

    $scope.newComponent = {
        name: "",
        version_id: 0, 
        element_id: elementId,
    };

    $scope.loadComponents = function() {
        if (!elementId) {
            console.error('Element ID is missing');
            return;
        }
        ComponentService.getAll(elementId).then(function(response) {
            $scope.componentList = response.data;
        }).catch(function(error) {
            console.error('Error fetching components:', error);
        });
    };

    $scope.createComponent = function() {
        if (!elementId) {
            console.error('Element ID is missing');
            return;
        }
        ComponentService.create($scope.newComponent).then(function(response) {
            alert('Component created successfully!');
            $scope.loadComponents();
            $state.go('base.component-view', {elementId: elementId});
        }).catch(function(error) {
            console.error('Error creating component:', error);
        });
    };

    $scope.cancelCreate = function() {
        $state.go('base.component-view', {elementId: elementId});
    };

    $scope.editComponent = function(componentId) {
        $state.go('base.component-update', {elementId: elementId, componentId: componentId});
    };
    $scope.detailComponent = function(componentId) {
        $state.go('base.component-detail', {elementId: elementId, componentId: componentId});
    };

    $scope.deleteComponent = function(componentId) {
        if (!componentId) {
            console.error('Component ID is missing');
            return;
        }
        var isConfirmed = confirm('Are you sure you want to delete this component?');
        if (isConfirmed) {
            ComponentService.delete(componentId).then(function(response) {
                alert('Component deleted successfully!');
                $scope.loadComponents();
            }).catch(function(error) {
                console.error('Error deleting component:', error);
            });
        }
    };

    $scope.resetForm = function() {
        $scope.newComponent = {
            name: "",
            version_id: 0, 
            element_id: elementId,
        };
    };

    $scope.loadComponents();
}]);
