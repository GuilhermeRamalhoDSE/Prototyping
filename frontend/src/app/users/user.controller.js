angular.module('frontend').controller('UserController', ['$scope', 'UserService', '$state', 'AuthService', function($scope, UserService, $state, AuthService) {
    $scope.users = [];
    $scope.formUser = {};
    $scope.isEditing = false;
    $scope.isSuperuser = AuthService.isSuperuser();

    $scope.getAllUsers = function() {
        UserService.getAllUsers().then(function(response) {
            $scope.users = response.data;
        }).catch(function(error) {
            console.error('Error fetching users:', error);
        });
    };

    $scope.initForm = function() {
        if (!$scope.isSuperuser) {
            var userLicenseId = AuthService.getLicenseId();
            $scope.formUser.licenseId = userLicenseId;
        }
    };

    $scope.createUser = function() {
        var formLicenseId = $scope.formUser.licenseId;
        var userLicenseId = AuthService.getLicenseId();
        
        if (!$scope.isSuperuser && (formLicenseId !== userLicenseId)) {
            alert('Only superusers can create users in different licenses.');
            return;
        }

        var userData = {
            ...$scope.formUser,
            license_id: $scope.formUser.licenseId 
        };
        delete userData.licenseId; 

        UserService.createUser(userData).then(function(response) {
            alert('User created successfully');
            $scope.getAllUsers();
            $scope.resetForm();
            $state.go('base.user-view');
        }).catch(function(error) {
            console.error('Error creating user:', error);
            if (error.data && error.data.detail) {
                alert('Error details: ' + JSON.stringify(error.data.detail));
            }
        });
    };
    $scope.cancelCreate = function() {
        $state.go('base.chassis-view');
    };

    $scope.editUser = function(userId) {
        $state.go('base.user-update', { userId: userId });
    };
    $scope.goBack = function() {
        $state.go('base.home');
    }; 

    $scope.deleteUser = function(userId) {
        if (confirm('Are you sure you want to delete this user?')) {
            UserService.deleteUser(userId).then(function(response) {
                $scope.getAllUsers();
            }).catch(function(error) {
                console.error('Error deleting user:', error);
            });
        }
    };

    $scope.resetForm = function() {
        $scope.formUser = {};
        $scope.isEditing = false;
        $scope.initForm();
    };

    $scope.getAllUsers();
    $scope.initForm();
}]);
