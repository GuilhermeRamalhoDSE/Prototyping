angular.module('frontend', ['ui.router'])
.config(['$httpProvider', function($httpProvider) {
    $httpProvider.interceptors.push('AuthInterceptor');
}])
.run(['$rootScope', '$state', 'AuthService', function($rootScope, $state, AuthService) {
    $rootScope.isSuperuser = function() {
        return AuthService.isSuperuser();
    };
    $rootScope.isStaff = function() {
        return AuthService.isStaff();
    };

    $rootScope.$on('$stateChangeStart', function(event, toState) {
        var requireLogin = toState.data && toState.data.requireLogin;
        var requiredPermissions = toState.data ? toState.data.requiredPermissions : null;

        if (requireLogin && !AuthService.isAuthenticated()) {
            event.preventDefault(); 
            $state.go('login'); 
        } else if (toState.name === 'login' && AuthService.isAuthenticated()) {
            event.preventDefault();
            $state.go('base.home'); 
        } else if (requiredPermissions && requiredPermissions.includes('superuser') && !AuthService.isSuperuser()) {
            event.preventDefault();
            $state.go('error');
        } else if (requiredPermissions && requiredPermissions.includes('staff') && !(AuthService.isSuperuser() || AuthService.isStaff())) {
            event.preventDefault();
            $state.go('error'); 
        }
    });
}]);
