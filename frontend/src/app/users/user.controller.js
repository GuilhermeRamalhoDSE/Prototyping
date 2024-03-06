angular.module('frontend').controller('UserController', ['$scope', 'UserService', '$state', function($scope, UserService, $state) {
    $scope.users = [];
    $scope.formUser = {}; 
    $scope.isEditing = false;

    $scope.getAllUsers = function() {
        UserService.getAllUsers().then(function(response) {
            $scope.users = response.data;
        }).catch(function(error) {
            console.error('Error fetching users:', error);
        });
    };

    $scope.createUser = function() {
        UserService.createUser($scope.formUser).then(function(response) {
            alert('User created successfully');
            $scope.getAllUsers();
            $scope.resetForm();
            $state.go('base.user-view'); 
        }).catch(function(error) {
            alert('Error creating user:', error);
        });
    };

    $scope.editUser = function(userId) {
        $state.go('base.user-update', { userId: userId });
    };  

    $scope.deleteUser = function(userId) {
        UserService.deleteUser(userId).then(function(response) {
            console.log('User successfully deleted:', response.data);
            $scope.getAllUsers();
        }).catch(function(error) {
            console.error('Error deleting user:', error);
        });
    };

    $scope.resetForm = function() {
        $scope.formUser = {};
        $scope.isEditing = false;
    };

    $scope.getAllUsers();
}]);
