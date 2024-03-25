angular.module('frontend').factory('NotificationService', ['$http', function($http) {
    var service = {};

    service.getUnreadNotifications = function() {
        return $http.get('http://localhost:8000/admin/prototyping/messages/notifications')
                    .then(function(response) {
                        return response.data;
                    })
                    .catch(function(error) {
                        console.error('Error fetching unread notifications:', error);
                        throw error;
                    });
    };

    return service;
}]);
