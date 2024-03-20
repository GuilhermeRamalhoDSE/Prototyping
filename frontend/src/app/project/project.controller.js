angular.module('frontend').controller('ProjectController', ['$scope', 'ProjectService', 'UserService', '$state', 'AuthService', 
function($scope, ProjectService, UserService, $state, AuthService) {
    $scope.projects = [];
    $scope.users = []; 
    $scope.newProject = {
        name: "",
        client_id: null, 
        users_ids: [],
        start_date: new Date(),
        end_date: new Date()
    };

    $scope.loadProjects = function() {
        ProjectService.getAll().then(function(response) {
            $scope.projects = response.data.map(project => {
                project.start_date = new Date(project.start_date);
                project.end_date = new Date(project.end_date);
                return project;
            });
        }).catch(function(error) {
            console.error('Error loading projects:', error);
        });
    };

    $scope.loadUsers = function() {
        UserService.getAllUsers().then(function(response) {
            $scope.users = response.data;
        }).catch(function(error) {
            console.error('Error loading users:', error);
        });
    };
    

    $scope.goToNewProject = function() {
        $state.go('base.project-new');
    };

    $scope.createProject = function() {
        let projectToCreate = {
            ...$scope.newProject,
            start_date: $scope.newProject.start_date.toISOString().substring(0, 10),
            end_date: $scope.newProject.end_date.toISOString().substring(0, 10)
        };
        ProjectService.create(projectToCreate).then(function(response) {
            alert('Project created successfully!');
            $state.go('base.project-view');
        }).catch(function(error) {
            console.error('Error creating project:', error);
        });
    };

    $scope.isUserAssignedToProject = function(project, userId) {
        return project.users && project.users.some(user => user.id === userId);
    };    
    

    $scope.toggleUserAssignment = function(project, userId) {
        const isAssigned = $scope.isUserAssignedToProject(project, userId);
        if (isAssigned) {
            ProjectService.removeUserFromProject(project.id, userId)
                .then(function(response) {
                    $scope.loadProjects(); 
                })
                .catch(function(error) {
                    console.error('Error removing user from project:', error);
                });
        } else {
            ProjectService.addUserToProject(project.id, userId)
                .then(function(response) {
                    $scope.loadProjects(); 
                })
                .catch(function(error) {
                    console.error('Error adding user to project:', error);
                });
        }
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
    $scope.loadUsers();
}]);
