angular.module('frontend')
.config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/login');

    $stateProvider
    .state('base', {
        abstract: true,
        templateUrl: 'app/base.html',
    })
    $stateProvider
    .state('list', {
        abstract: true,
        templateUrl: 'app/list.html',
    })
    .state('base.home', {
        url: '/home',
        templateUrl: 'app/home/home.html',
        controller: 'HomeController'
    })
    .state('base.licenses', {
        url: '/licenses',
        templateUrl: 'app/licenses/license.html',
        controller: 'LicenseController'
    })
    .state('login', {
        url: '/login',
        templateUrl: 'app/login/login.html',
        controller: 'LoginController'
    });
}]);
