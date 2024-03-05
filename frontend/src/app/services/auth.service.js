angular.module('frontend').factory('AuthService', ['$http', '$window', function($http, $window) {
    var authService = {};

    authService.login = function(credentials) {
        return $http.post('http://127.0.0.1:8000/prototyping/api/login/', credentials).then(function(response) {
            if (credentials.rememberMe) {
                $window.localStorage.setItem('jwtToken', response.data.token);
            } else {
                $window.sessionStorage.setItem('jwtToken', response.data.token);
            }
            return response.data;
        });
    };

    authService.logout = function() {
        $window.localStorage.removeItem('jwtToken');
        $window.sessionStorage.removeItem('jwtToken');
    };

    authService.isAuthenticated = function() {
        return !!($window.localStorage.getItem('jwtToken') || $window.sessionStorage.getItem('jwtToken'));
    };

    authService.getToken = function() {
        return $window.localStorage.getItem('jwtToken') || $window.sessionStorage.getItem('jwtToken');
    };

    return authService;
}]);
