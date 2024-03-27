angular.module('frontend').controller('InboxController', ['$scope', '$state', 'ProjectService', 'MessageService', 'WebSocketService', 'AuthService', '$timeout', 
function($scope, $state, ProjectService, MessageService, WebSocketService, AuthService, $timeout) {
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
            $scope.updateTotalUnreadMessages();
        }, function(error) {
            console.error("Error loading projects:", error.statusText);
        });
    };

    $scope.$on('newMessage', function(event, data) {
        $scope.$apply(function() { 
            var projectId = parseInt(data.project_id, 10);
            var senderId = data.user_id;
            var currentUserId = AuthService.getUserId();
            if (currentUserId) currentUserId = currentUserId.toString();
            var project = $scope.projects.find(p => p.id === projectId);
            if (project && senderId && senderId.toString() !== currentUserId) {
                if (!project.unreadMessagesCount) project.unreadMessagesCount = 0;
                project.unreadMessagesCount += 1;
                notificationSound.play().catch(error => console.error("Playback failed:", error));
                $scope.updateTotalUnreadMessages();
            }
        });
    });

    $scope.markMessagesAsRead = function(projectId) {
        MessageService.markAllMessagesAsRead(projectId).then(function() {
            $timeout(function() { 
                var project = $scope.projects.find(p => p.id === projectId);
                if (project) {
                    project.unreadMessagesCount = 0;
                }
                $scope.updateTotalUnreadMessages();
            });
        });
    };
    
    $scope.totalUnreadMessages = function() {
        return $scope.projects.reduce((total, project) => total + project.unreadMessagesCount, 0);
    };

    $scope.updateTotalUnreadMessages = function() {
        $scope.totalUnreadCount = $scope.projects.reduce((total, project) => total + project.unreadMessagesCount, 0);
    };

    $scope.loadProjects();
}]);
