angular.module('frontend').factory('MessageService', ['$http', function($http) {
    const baseUrl = 'https://prototypingdse.it/prototyping/api/messages/';
    
    return {
        getMessagesForProject: function(projectId) {
            return $http.get(baseUrl + projectId);
        },
        sendMessage: function(messageData) {
            return $http.post(baseUrl, messageData);
        },
        updateMessage: function(messageId, messageData) {
            return $http.put(baseUrl + messageId + '/', messageData);
        },
        deleteMessage: function(messageId) {
            return $http.delete(baseUrl + messageId + '/');
        },
        getUnreadMessagesCount: function(projectId) {
            return $http.get(baseUrl + projectId + '/unread-count');
        },
        markMessageAsRead: function(messageId) {
            return $http.patch(baseUrl + messageId + '/read');
        },
        markAllMessagesAsRead: function(projectId) {
            return $http.patch(baseUrl + 'project/' + projectId + '/read-all');
        },
    };
}]);
