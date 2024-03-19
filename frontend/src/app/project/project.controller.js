angular.module('frontend').controller('ProjectController', ['$scope', 'ProjectService', '$state', 'AuthService', function($scope, ProjectService, $state, AuthService) {
    $scope.projects = [];
    $scope.newProject = {
        name: "",
        client_id: null, 
        users_ids: [],
        creation_date: new Date(), 
        last_release_date: new Date() 
    };

    $scope.loadProjects = function() {
        ProjectService.getAll().then(function(response) {
            $scope.projects = response.data;
        }).catch(function(error) {
            console.error('Error loading projects:', error);
        });
    };

    $scope.goToNewProject = function() {
        $state.go('base.project-new');
    };

    $scope.createProject = function() {
        ProjectService.create($scope.newProject).then(function(response) {
            alert('Project created successfully!');
            $state.go('base.project-view');
        }).catch(function(error) {
            console.error('Error creating project:', error);
        });
    };

    $scope.editProject = function(projectId) {
        $state.go('base.project-update', { projectId: projectId });
    };

    $scope.cancelCreate = function() {
        $state.go('base.project-view');
    };

    $scope.goBack = function() {
        $state.go('base.home');
    };

    $scope.deleteProject = function(projectId) {
        if (confirm('Are you sure you want to delete this project?')) {
            ProjectService.delete(projectId).then(function(response) {
                alert('Project deleted successfully!');
                $scope.loadProjects();
            }).catch(function(error) {
                console.error('Error deleting project:', error);
            });
        }
    };

    $scope.loadProjects();
}]);
