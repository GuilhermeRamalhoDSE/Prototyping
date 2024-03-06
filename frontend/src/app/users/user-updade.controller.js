angular.module('frontend').controller('UserUpdateController', ['$scope', '$state', 'UserService', function($scope, $state, UserService) {
    $scope.formUser = {};
    $scope.isEditing = true;

    $scope.loadUser = function() {
        const userId = $state.params.userId; 
        UserService.getUserById(userId).then(function(response) {
            if (response.data && response.data.length > 0) {
                $scope.formUser = response.data[0];
            } else {
                console.error('User not found');
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
            password: $scope.formUser.password, 
            license_id: $scope.formUser.license_id 
        };

        UserService.updateUser($scope.formUser.id, userDataToUpdate).then(function(response) {
            alert('User updated successfully');
            $state.go('base.user-view'); 
        }).catch(function(error) {
            console.error('Error updating user:', error);
            alert('Failed to update user'); 
        });
    };

    $scope.loadUser(); 
}]);
