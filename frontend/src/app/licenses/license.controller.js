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
        var licenseData = angular.copy($scope.newLicense);
        
        // Converte as datas usando moment.js
        if (licenseData.start_date) {
            licenseData.start_date = moment(licenseData.start_date, "DD/MM/YYYY").format('YYYY-MM-DD');
        }
        if (licenseData.end_date) {
            licenseData.end_date = moment(licenseData.end_date, "DD/MM/YYYY").format('YYYY-MM-DD');
        }

        LicenseService.create(licenseData).then(function(response) {
            $scope.licenses.push(response.data);
            
            // Reset do formulário
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
        }, function(error) {
            console.error('Erro ao criar a licença:', error);
        });
    };

    $scope.getAllLicenses(); 
}]);
