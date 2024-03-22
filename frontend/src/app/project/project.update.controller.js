angular.module('frontend').controller('ProjectUpdateController', ['$scope', 'ProjectService', 'ClientService', '$stateParams', '$state', function($scope, ProjectService, ClientService, $stateParams, $state) {

    var projectId = $stateParams.projectId;

    $scope.init = function() {
        ClientService.getAll().then(function(response) {
            $scope.clients = response.data;
            $scope.loadProject();
        }).catch(function(error) {
            console.error('Error loading clients:', error);
        });
    };
    
    $scope.loadProject = function() {
        ProjectService.getById(projectId).then(function(response) {
            let projectData = response.data;
            $scope.currentProject = projectData;

            $scope.currentProject.start_date = new Date(projectData.start_date);
            $scope.currentProject.end_date = new Date(projectData.end_date);
            if (projectData.client_id && $scope.clients) {
                $scope.selectedClient = $scope.clients.find(client => client.id === projectData.client_id);
            }
        }).catch(function(error) {
            console.error('Error loading project:', error);
        });
    };     

    $scope.updateProject = function() {
        let projectToUpdate = {
            ...$scope.currentProject,
            start_date: $scope.currentProject.start_date.toISOString().substring(0, 10),
            end_date: $scope.currentProject.end_date.toISOString().substring(0, 10)
        };
        ProjectService.update(projectId, projectToUpdate).then(function(response) {
            alert('Project updated successfully!');
            $state.go('base.project-view');
        }).catch(function(error) {
            console.error('Error updating project:', error);
        });
    };

    $scope.cancelUpdate = function() {
        $state.go('base.project-view');
    };

    $scope.loadProject();
    $scope.init();
}]);
