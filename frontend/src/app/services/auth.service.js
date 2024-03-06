angular.module('frontend').factory('AuthService', ['$http', '$window', function($http, $window) {
    var authService = {};

    authService.login = function(credentials) {
        return $http.post('http://127.0.0.1:8000/prototyping/api/login/', credentials).then(function(response) {
            if (credentials.rememberMe) {
                $window.localStorage.setItem('jwtToken', response.data.token);
                $window.localStorage.setItem('isSuperuser', response.data.is_superuser);
                $window.localStorage.setItem('isStaff', response.data.is_staff); 
                $window.localStorage.setItem('licenseId', response.data.license_id.toString());
            } else {
                $window.sessionStorage.setItem('jwtToken', response.data.token);
                $window.sessionStorage.setItem('isSuperuser', response.data.is_superuser);
                $window.sessionStorage.setItem('isStaff', response.data.is_staff); 
                $window.sessionStorage.setItem('licenseId', response.data.license_id.toString());
            }
            return response.data;
        });
    };
    
    authService.isSuperuser = function() {
        return $window.localStorage.getItem('isSuperuser') === 'true' || $window.sessionStorage.getItem('isSuperuser') === 'true';
    };

    authService.isStaff = function() {
        return $window.localStorage.getItem('isStaff') === 'true' || $window.sessionStorage.getItem('isStaff') === 'true';
    };

    authService.getLicenseId = function() {
        return $window.localStorage.getItem('licenseId') || $window.sessionStorage.getItem('licenseId');
    };

    authService.logout = function() {
        $window.localStorage.removeItem('jwtToken');
        $window.localStorage.removeItem('isSuperuser');
        $window.localStorage.removeItem('isStaff'); 
        $window.localStorage.removeItem('licenseId'); 
        $window.sessionStorage.removeItem('jwtToken');
        $window.sessionStorage.removeItem('isSuperuser');
        $window.sessionStorage.removeItem('isStaff'); 
        $window.sessionStorage.removeItem('licenseId'); 
    };

    authService.isAuthenticated = function() {
        return !!($window.localStorage.getItem('jwtToken') || $window.sessionStorage.getItem('jwtToken'));
    };

    authService.getToken = function() {
        return $window.localStorage.getItem('jwtToken') || $window.sessionStorage.getItem('jwtToken');
    };

    return authService;
}]);
