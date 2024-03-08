angular.module('frontend').controller('ChassisUpdateController', ['$scope', '$state', 'ChassisService', 'AuthService', function($scope, $state, ChassisService, AuthService) {
    $scope.formChassis = {};
    $scope.isEditing = true;
    $scope.isSuperuser = AuthService.isSuperuser();

    $scope.loadChassis = function() {
        const chassisId = $state.params.chassisId;
        ChassisService.getChassisById(chassisId).then(function(response) {
            if (response.data && response.data.length > 0) {
                $scope.formChassis = response.data[0];
            } else {
                $state.go('base.chassis-view');
            }
        }).catch(function(error) {
            console.error('Error fetching chassis:', error);
        });
    };

    $scope.updateChassis = function() {
        var chassisDataToUpdate = new FormData();
        var chassisIn = JSON.stringify({
            name: $scope.formChassis.name,
            license_id: $scope.isSuperuser ? $scope.formChassis.license_id : AuthService.getLicenseId(),
        });

        chassisDataToUpdate.append('chassis_in', chassisIn);

        if ($scope.formChassis.file && $scope.formChassis.file != $scope.formChassis.originalFile) {
            chassisDataToUpdate.append('file', $scope.formChassis.file);
        }

        ChassisService.updateChassis($scope.formChassis.id, chassisDataToUpdate).then(function(response) {
            alert('Chassis updated successfully');
            $state.go('base.chassis-view');
        }).catch(function(error) {
            console.error('Error updating chassis:', error);
            alert('Failed to update chassis');
        });
    };
    $scope.cancelUpdate = function() {
        $state.go('base.chassis-view');
    };

    $scope.loadChassis();
}]);
