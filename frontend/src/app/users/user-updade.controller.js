angular.module('frontend').controller('UserUpdateController', ['$scope', '$state', 'UserService', 'AuthService', function($scope, $state, UserService, AuthService) {
    $scope.formUser = {};
    $scope.isEditing = true;
    $scope.isSuperuser = AuthService.isSuperuser();

    $scope.loadUser = function() {
        const userId = $state.params.userId;
        UserService.getUserById(userId).then(function(response) {
            if (response.data && response.data.length > 0) {
                $scope.formUser = response.data[0];
            } else {
                $state.go('base.user-view'); 
            }
        }).catch(function(error) {
            console.error('Error fetching user:', error);
        });
    }; 
    
    $scope.updateUser = function() {
        var userDataToUpdate = {
            first_name: $scope.formUser.first_name,
            last_name: $scope.formUser.last_name,
            email: $scope.formUser.email,
            is_staff: $scope.formUser.is_staff,
            role: $scope.formUser.role,
            license_id: $scope.formUser.license_id
        };

        if (!$scope.isSuperuser) {
            userDataToUpdate.license_id = AuthService.getLicenseId();
        }

        UserService.updateUser($scope.formUser.id, userDataToUpdate).then(function(response) {
            alert('User updated successfully');
            $state.go('base.user-view'); 
        }).catch(function(error) {
            console.error('Error updating user:', error);
            alert('Failed to update user'); 
        });
    };

    $scope.cancelUpdate = function() {
        $state.go('base.chassis-view');
    };

    $scope.loadUser(); 
}]);
