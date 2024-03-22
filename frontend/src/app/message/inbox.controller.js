angular.module('frontend').controller('InboxController', ['$scope', 'ProjectService', 'MessageService', function($scope, ProjectService) {  
    $scope.projects = [];

    $scope.loadProjects = function() {
        ProjectService.getAll().then(function(response) {
            $scope.projects = response.data;
        }, function(error) {
            console.error("Error loading projects:", error.statusText);
        });
    };

    $scope.loadProjects();
}]);
