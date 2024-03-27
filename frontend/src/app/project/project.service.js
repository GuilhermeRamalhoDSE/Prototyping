angular.module('frontend').factory('ProjectService', ['$http', function($http) {
    const baseUrl = 'https://prototypingdse.it/prototyping/api/projects/';
    return {
        create: function(projectData) {
            return $http.post(baseUrl, projectData);
        },
        getAll: function() {
            return $http.get(baseUrl);
        },
        getById: function(projectId) {
            return $http.get(baseUrl + projectId);
        },        
        update: function(projectId, projectData) {
            return $http.put(baseUrl + projectId, projectData);
        },
        delete: function(projectId) {
            return $http.delete(baseUrl + projectId);
        },   
        addUserToProject: function(projectId, userId) {
            return $http.post(baseUrl + projectId + '/add-user/', {user_id: userId});
        },
        removeUserFromProject: function(projectId, userId) {
            return $http.post(baseUrl + projectId + '/remove-user/', {user_id: userId});
        },  
        getAllUsers: function() {
            return $http.get('https://prototypingdse.it/prototyping/api/users/');
        },
        getAllClients: function() {
            return $http.get('https://prototypingdse.it/prototyping/api/clients/');
        },
        getAllByClientId: function(clientId) {
            return $http.get(baseUrl, { params: { client_id: clientId } });
        },        
    };
}]);
