angular.module('frontend').factory('MessageService', ['$http', function($http) {
    const baseUrl = 'http://localhost:8000/prototyping/api/messages/';
    
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
        }
    };
}]);
