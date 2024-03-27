angular.module('frontend').controller('InboxController', ['$scope', '$state', 'ProjectService', 'MessageService', 'WebSocketService', 'AuthService', function($scope, $state, ProjectService, MessageService, WebSocketService, AuthService) {
    $scope.projects = [];
    var notificationSound = new Audio('../assets/sounds/Messenger.mp3'); 

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
        var senderId = data.user_id; 
        var currentUserId = AuthService.getUserId();
        
        if (currentUserId) currentUserId = currentUserId.toString();
    
        var project = $scope.projects.find(p => p.id === projectId);
        
        if (project && senderId && senderId.toString() !== currentUserId) {
            if (!project.unreadMessagesCount) project.unreadMessagesCount = 0;
            project.unreadMessagesCount += 1;
    
            notificationSound.play().catch(error => console.error("Playback failed:", error));
    
            if (!$scope.$$phase) $scope.$apply();
        }
    });
     
    
    $scope.totalUnreadMessages = function() {
        return $scope.projects.reduce((total, project) => total + project.unreadMessagesCount, 0);
    };
    
    $scope.loadProjects();
}]);
