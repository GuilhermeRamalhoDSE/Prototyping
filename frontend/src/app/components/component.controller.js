angular.module('frontend').controller('ComponentController', ['$scope', '$http','ComponentService', '$state', '$stateParams', 'AuthService', function($scope, $http, ComponentService, $state, $stateParams, AuthService) {
    $scope.componentList = [];
    $scope.isSuperuser = AuthService.isSuperuser();
    $scope.file = null;
    let elementId = parseInt($stateParams.elementId || sessionStorage.getItem('lastElementId'), 10);
    sessionStorage.setItem('lastElementId', elementId.toString());

    $scope.newComponent = {
        name: "",
        version_id: 0,
        element_id: elementId,
        limit_position_x: 0,
        limit_position_y: 0,
        limit_position_z: 0,
        limit_rotation_x: 0,
        limit_rotation_y: 0,
        limit_rotation_z: 0,
        limit_rotation_w: 0,
        area_radius: 0,
        haptic_stiffness: 0,
        haptic_temperature: 0,
        haptic_texture: 0,
        component_number: null
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
        if (!elementId || !$scope.file) {
            console.error('Element ID or file is missing');
            return;
        }
    
        var formData = new FormData();
        formData.append('file', $scope.file);
    
        var componentData = { ...$scope.newComponent };
        formData.append('component_in', JSON.stringify(componentData));
    
        ComponentService.create(formData).then(function(response) {
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
            limit_position_x: 0,
            limit_position_y: 0,
            limit_position_z: 0,
            limit_rotation_x: 0,
            limit_rotation_y: 0,
            limit_rotation_z: 0,
            limit_rotation_w: 0,
            area_radius: 0,
            haptic_stiffness: 0,
            haptic_temperature: 0,
            haptic_texture: 0,
            component_number: null
        };
    };

    $scope.downloadComponentFile = function(componentId) {
        if (componentId) {
            var downloadUrl = 'https://prototypingdse.it/prototyping/api/components/download/' + componentId;
            
            $http({
                url: downloadUrl,
                method: 'GET',
                responseType: 'blob',
            }).then(function (response) {
                var blob = new Blob([response.data], {type: response.headers('Content-Type')});
                var downloadLink = angular.element('<a></a>');
                downloadLink.attr('href', window.URL.createObjectURL(blob));
                downloadLink.attr('download', 'ComponentFile-' + componentId+ '.fbx');
                
                document.body.appendChild(downloadLink[0]);
                downloadLink[0].click();
                document.body.removeChild(downloadLink[0]);
            }).catch(function (data) {
                console.error("Download failed: ", data);
            });
        } else {
            console.error("Download failed: Component ID is invalid.");
        }
    };
    

    $scope.loadComponents();
}]);
