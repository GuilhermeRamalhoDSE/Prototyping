angular.module('frontend')
.config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/login');
    $stateProvider
    .state('login', {
        url: '/login',
        templateUrl: 'app/login/login.html',
        controller: 'LoginController'
    })
    $stateProvider
    .state('base', {
        abstract: true,
        templateUrl: 'app/base.html',
        data: {
            requireLogin: true
        }
    })
    $stateProvider
    .state('error', {
        url: '/error',
        templateUrl: 'app/errors/error.html',
        controller: 'ErrorController',
        data: {
            requireLogin: true
        }
    })
    $stateProvider
    .state('base.home', {
        url: '/home',
        templateUrl: 'app/home/home.html',
        controller: 'HomeController',
        data: {
            requireLogin: true
        }
    })
    $stateProvider
    .state('base.licenses', {
        url: '/licenses/new',
        templateUrl: 'app/licenses/license.html',
        controller: 'LicenseController',
        data: {
            requireLogin: true, 
            requiredPermissions: ['superuser'] 
        }
    })
    $stateProvider
    .state('base.licenses-update', {
        url: '/licenses/update/:licenseId',
        templateUrl: 'app/licenses/update-license.html',
        controller: 'LicenseUpdateController',
        data: {
            requireLogin: true, 
            requiredPermissions: ['superuser'] 
        }
    })
    $stateProvider
    .state('base.list_licenses', {
        url: '/licenses/list',
        templateUrl: 'app/licenses/licenses-view.html',
        controller: 'LicenseController',
        data: {
            requireLogin: true, 
            requiredPermissions: ['superuser'] 
        }
    })
    $stateProvider
    .state('base.user-new', {
        url: '/user/new',
        templateUrl: 'app/users/user-new.html',
        controller: 'UserController',
        data: {
            requireLogin: true, 
            requiredPermissions: ['superuser', 'staff'] 
        }
    })
    $stateProvider
    .state('base.user-view', {
        url: '/user/list',
        templateUrl: 'app/users/user-view.html',
        controller: 'UserController',
        data: {
            requireLogin: true, 
            requiredPermissions: ['superuser', 'staff'] 
        }
    })
    $stateProvider
    .state('base.user-update', {
        url: '/user/update/:userId',
        templateUrl: 'app/users/update-user.html',
        controller: 'UserUpdateController',
        data: {
            requireLogin: true, 
            requiredPermissions: ['superuser', 'staff'] 
        }
    })
    $stateProvider
    .state('base.chassis-new', {
        url: '/chassis/new',
        templateUrl: 'app/chassis/chassis-new.html',
        controller: 'ChassisController',
        data: {
            requireLogin: true, 
            requiredPermissions: ['superuser', 'staff'] 
        }
    })
    $stateProvider
    .state('base.chassis-view', {
        url: '/chassis/list',
        templateUrl: 'app/chassis/chassis-view.html',
        controller: 'ChassisController',
        data: {
            requireLogin: true, 
            requiredPermissions: ['superuser', 'staff'] 
        }
    })
    $stateProvider
    .state('base.chassis-update', {
        url: '/chassis/update/:chassisId',
        templateUrl: 'app/chassis/chassis-update.html',
        controller: 'ChassisUpdateController',
        data: {
            requireLogin: true, 
            requiredPermissions: ['superuser', 'staff'] 
        }
    })
    $stateProvider
    .state('base.element-new', {
        url: '/chassis/:chassisId/element/new',
        templateUrl: 'app/elements/element-new.html',
        controller: 'ElementController',
        data: {
            requireLogin: true, 
            requiredPermissions: ['superuser', 'staff'] 
        }
    })
    $stateProvider
    .state('base.element-view', {
        url: '/chassis/:chassisId/elements',
        templateUrl: 'app/elements/element-view.html',
        controller: 'ElementController',
        data: {
            requireLogin: true, 
            requiredPermissions: ['superuser', 'staff'] 
        }
    })
    $stateProvider
    .state('base.element-update', {
        url: '/chassis/:chassisId/element/update/:elementId',
        templateUrl: 'app/elements/element-update.html',
        controller: 'ElementUpdateController',
        data: {
            requireLogin: true, 
            requiredPermissions: ['superuser', 'staff'] 
        }
    })
    $stateProvider
    .state('base.component-new', {
        url: '/chassis/:chassisId/element/:elementId/component/new',
        templateUrl: 'app/components/component-new.html',
        controller: 'ComponentController',
        data: {
            requireLogin: true, 
            requiredPermissions: ['superuser', 'staff'] 
        }
    })
    $stateProvider
    .state('base.component-view', {
        url: '/chassis/:chassisId/element/:elementId/components',
        templateUrl: 'app/components/component-view.html',
        controller: 'ComponentController',
        data: {
            requireLogin: true, 
            requiredPermissions: ['superuser', 'staff'] 
        }
    })
    $stateProvider
    .state('base.component-update', {
        url: '/chassis/:chassisId/element/:elementId/component/update/:componentId',
        templateUrl: 'app/components/component-update.html',
        controller: 'ComponentUpdateController',
        data: {
            requireLogin: true, 
            requiredPermissions: ['superuser', 'staff'] 
        }
    })
    $stateProvider
    .state('base.client-new', {
        url: '/clients/new',
        templateUrl: 'app/client/client-new.html',
        controller: 'ClientController',
        data: {
            requireLogin: true, 
            requiredPermissions: ['superuser', 'staff'] 
        }
    })
    $stateProvider
    .state('base.client-view', {
        url: '/clients/list',
        templateUrl: 'app/client/client-view.html',
        controller: 'ClientController',
        data: {
            requireLogin: true, 
            requiredPermissions: ['superuser', 'staff'] 
        }
    })
    $stateProvider
    .state('base.client-update', {
        url: '/clients/update/:clientId',
        templateUrl: 'app/client/client-update.html',
        controller: 'ClientUpdateController',
        data: {
            requireLogin: true, 
            requiredPermissions: ['superuser', 'staff'] 
        }
    })
    $stateProvider
    .state('base.project-new', {
        url: '/projects/new',
        templateUrl: 'app/project/project-new.html',
        controller: 'ProjectController',
        data: {
            requireLogin: true, 
            requiredPermissions: ['superuser', 'staff'] 
        }
    })
    $stateProvider
    .state('base.project-view', {
        url: '/projects/list/:clientId?',
        templateUrl: 'app/project/project-view.html',
        controller: 'ProjectController',
        data: {
            requireLogin: true, 
        }
    })
    $stateProvider
    .state('base.project-update', {
        url: '/project/update/:projectId',
        templateUrl: 'app/project/project-update.html',
        controller: 'ProjectUpdateController',
        data: {
            requireLogin: true, 
            requiredPermissions: ['superuser', 'staff'] 
        }
    })
    $stateProvider
    .state('base.chat', {
        url: '/chat',
        templateUrl: 'app/message/chat.html',
        controller: 'MessageController',
        data: {
            requireLogin: true, 
        }
    })
    $stateProvider
    .state('base.inbox', {
        url: '/inbox',
        templateUrl: 'app/message/inbox.html',
        controller: 'MessageController',
        data: {
            requireLogin: true, 
        }
    })
}]);
