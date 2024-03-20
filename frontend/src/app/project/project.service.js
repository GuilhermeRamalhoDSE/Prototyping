angular.module('frontend').factory('ProjectService', ['$http', function($http) {
    const baseUrl = 'http://localhost:8000/prototyping/api/projects/';
    return {
        create: function(projectData) {
            return $http.post(baseUrl, projectData);
        },
        getAll: function() {
            return $http.get(baseUrl);
        },
        getById: function(projectId) {
            return $http.get(baseUrl, { params: { project_id: projectId } });
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
            return $http.get('http://localhost:8000/prototyping/api/users/');
        }
    };
}]);