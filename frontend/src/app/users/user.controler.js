angular.module('frontend').controller('UserController', ['$scope', 'UserService', function($scope, UserService) {
    $scope.users = [];
    $scope.formUser = {}; // Usado tanto para criar quanto para editar
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
            console.log('User created successfully:', response.data);
            $scope.getAllUsers();
            $scope.resetForm();
        }).catch(function(error) {
            console.error('Error creating user:', error);
        });
    };

    $scope.selectUserForEdit = function(user) {
        $scope.formUser = angular.copy(user);
        $scope.isEditing = true;
    };

    $scope.updateUser = function() {
        UserService.updateUser($scope.formUser.id, $scope.formUser).then(function(response) {
            console.log('User updated successfully:', response.data);
            $scope.getAllUsers();
            $scope.resetForm();
        }).catch(function(error) {
            console.error('Error updating user:', error);
        });
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
