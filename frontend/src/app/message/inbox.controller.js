angular.module('frontend').controller('InboxController', ['$scope', '$state', 'ProjectService', 'MessageService', 'WebSocketService', function($scope, $state, ProjectService, MessageService, WebSocketService) {
    $scope.projects = [];

    $scope.loadProjects = function() {
        ProjectService.getAll().then(function(response) {
            $scope.projects = response.data;
            $scope.projects.forEach(function(project) {
                project.unreadMessagesCount = 0;
                WebSocketService.connect(project.id);
                
                MessageService.getUnreadMessagesCount(project.id).then(function(countResponse) {
                    project.unreadMessagesCount = countResponse.data;
                });
            });
        }, function(error) {
            console.error("Error loading projects:", error.statusText);
        });
    };

    $scope.$on('newMessage', function(event, data) {
        
        var projectId = parseInt(data.project_id, 10); 
    
        var project = $scope.projects.find(function(p) {
            return p.id === projectId; 
        });
    
        if (project) {
            if (!project.unreadMessagesCount) {
                project.unreadMessagesCount = 0;
            }
            project.unreadMessagesCount += 1;
            
            if(!$scope.$$phase) { 
                $scope.$apply(); 
            }
        } else {
            console.log("Project not found for ID:", projectId);
        }
    });
    
    $scope.totalUnreadMessages = function() {
        return $scope.projects.reduce((total, project) => total + project.unreadMessagesCount, 0);
    };
    
    // $scope.goToProject = function(projectId) {
    //     $state.go('base.chat', {projectId: projectId});
    // };  
    
    $scope.loadProjects();
}]);
