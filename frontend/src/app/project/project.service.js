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
        }        
    };
}]);
