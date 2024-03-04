angular.module('frontend').controller('LicenseController', ['$scope', 'LicenseService', function($scope, LicenseService) {
    $scope.licenses = [];
 
    $scope.newLicense = {
        name: "",
        email: "",
        address: "",
        tel: "",
        license_code: "",
        active: true,
        start_date: "",
        end_date: ""
    };

    $scope.getAllLicenses = function() {
        LicenseService.getAll().then(function(response) {
            $scope.licenses = response.data;
        });
    };

    $scope.createLicense = function() {
        LicenseService.create($scope.newLicense).then(function(response) {
            $scope.licenses.push(response.data);

            $scope.newLicense = {
                name: "",
                email: "",
                address: "",
                tel: "",
                license_code: "",
                active: true,
                start_date: "",
                end_date: ""
            };
        });
    };

    $scope.getAllLicenses(); 
}]);
