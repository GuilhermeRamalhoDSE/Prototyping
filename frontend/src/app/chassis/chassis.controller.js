angular.module('frontend').controller('ChassisController', ['$scope', 'ChassisService', '$state', function($scope, ChassisService, $state) {
    $scope.chassisList = [];
    $scope.isEditing = false;

    $scope.newChassis = {
        name: "",
        file: null
    };

    $scope.loadChassis = function() {
        ChassisService.getChassis().then(function(response) {
            $scope.chassisList = response.data;
        }).catch(function(error) {
            console.error('Error fetching chassis:', error);
        });
    };

    $scope.createChassis = function() {
        var chassisData = new FormData();
        chassisData.append('name', $scope.newChassis.name);
        if ($scope.newChassis.file) {
            chassisData.append('file', $scope.newChassis.file);
        }

        ChassisService.createChassis(chassisData).then(function(response) {
            alert('Chassis created successfully!');
            $scope.loadChassis();
            $scope.newChassis = { name: "", file: null };
        }).catch(function(error) {
            console.error('Error creating chassis:', error);
        });
    };

    $scope.editChassis = function(userId) {
        $state.go('base.chassis-update', { userId: userId });
    };

    $scope.deleteChassis = function(chassisId) {
        if (confirm('Are you sure you want to delete this chassis?')) {
            ChassisService.deleteChassis(chassisId).then(function(response) {
                alert('Chassis successfully deleted!');
                $scope.loadChassis();
            }).catch(function(error) {
                console.error('Error deleting chassis:', error);
            });
        }
    };

    $scope.loadChassis();
}]);
