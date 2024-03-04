angular.module('frontend').config(function($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/home');

    $stateProvider
        .state('home', {
            url: '/home',
            templateUrl: 'app/views/home.html',
            controller: 'HomeController',
            data: { requireLogin: true } 
        })
        .state('login', {
            url: '/login',
            templateUrl: 'app/views/login.html',
            controller: 'LoginController'
        });
});
