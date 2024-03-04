angular.module('frontend').controller('HomeController', ['$scope', 'AuthService', '$state', function($scope, AuthService, $state) {
    $scope.logout = function() {
        AuthService.logout();
        $state.go('login');
    };
}]);
