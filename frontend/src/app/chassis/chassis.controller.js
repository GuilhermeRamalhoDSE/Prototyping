angular.module('frontend').controller('ChassisController', ['$scope', '$http', 'ChassisService', '$state', 'AuthService', function($scope, $http, ChassisService, $state, AuthService) {
    $scope.chassisList = [];
    $scope.isEditing = false;
    $scope.isSuperuser = AuthService.isSuperuser();

    $scope.newChassis = {
        name: "",
        file: null,
        license_id: AuthService.getLicenseId()
    };

    $scope.initForm = function() {
        if (!$scope.isSuperuser) {
            var userLicenseId = AuthService.getLicenseId();
            $scope.newChassis.license_id = userLicenseId;
        }
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
        var chassisIn = JSON.stringify({
            name: $scope.newChassis.name,
            license_id: $scope.newChassis.license_id,

            file: $scope.newChassis.file ? $scope.newChassis.file.name : null
        });
    

        chassisData.append('chassis_in', chassisIn);

        if ($scope.newChassis.file) {
            chassisData.append('file', $scope.newChassis.file);
        }
    
        ChassisService.createChassis(chassisData).then(function(response) {
            alert('Chassis created successfully!');
            $scope.loadChassis();
            $scope.resetForm();
            $state.go('base.chassis-view');
        }).catch(function(error) {
            console.error('Error creating chassis:', error);
        });
    };
    $scope.cancelCreate = function() {
        $state.go('base.chassis-view');
    };

    $scope.editChassis = function(chassisId) {
        $state.go('base.chassis-update', { chassisId: chassisId });
    };

    $scope.detailingChassis = function(chassisId) {
        $state.go('base.element-view', { chassisId: chassisId });
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

    $scope.downloadChassisFile = function(chassisId) {
        if (chassisId) {
            var downloadUrl = 'https://www.prototypingdse.it/prototyping/api/chassis/download/' + chassisId;
            
            $http({
                url: downloadUrl,
                method: 'GET',
                responseType: 'blob', 
            }).then(function (response) {
                var blob = new Blob([response.data], {type: response.headers('Content-Type')});
                var downloadLink = angular.element('<a></a>');
                downloadLink.attr('href', window.URL.createObjectURL(blob));
                downloadLink.attr('download', 'ChassisFile-' + chassisId + '.fbx');
                
                downloadLink[0].click();
            }).catch(function (data) {
                console.error("Download failed: ", data);
            });
        } else {
            console.error("Download failed: Chassis ID is invalid.");
        }
    };
    
    $scope.resetForm = function() {
        $scope.newChassis = { name: "", file: null, license_id: AuthService.getLicenseId() };
        $scope.isEditing = false;
        $scope.initForm();
    };

    $scope.loadChassis();
    $scope.initForm();
}]);
