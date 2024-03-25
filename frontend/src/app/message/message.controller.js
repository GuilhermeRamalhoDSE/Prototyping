angular.module('frontend').controller('MessageController', ['$scope', '$state', 'MessageService', '$stateParams', 'AuthService', 'ProjectService', 'WebSocketService', function($scope, $state, MessageService, $stateParams, AuthService, ProjectService, WebSocketService) {
    $scope.messages = [];
    $scope.newMessage = "";
    $scope.currentUser = {
        id: parseInt(AuthService.getUserId(), 10)
    };

    $scope.projectId = $stateParams.projectId;
    $scope.clientId = null;

    $scope.loadProjectDetails = function() {
        ProjectService.getById($scope.projectId).then(function(response) {
            $scope.clientId = response.data.client_id;
        }, function(error) {
            console.error("Error loading project details:", error.statusText);
        });
    };

    $scope.loadMessages = function() {
        MessageService.getMessagesForProject($scope.projectId).then(function(response) {
            $scope.messages = response.data.map(function(message) {
                message.formattedDate = new Date(message.date).toLocaleString();
                return message;
            });

            if ($scope.messages.length > 0 && !$scope.clientId) {
                $scope.clientId = $scope.messages[0].client_id;
            }
        }, function(error) {
            console.error("Error loading messages:", error.statusText);
        });

        WebSocketService.connect($scope.projectId);
        
        $scope.$on('newMessage', function(event, data) {
            
            $scope.$apply(function() {
            var isCurrentUser = (data.user_id === $scope.currentUser.id);
            const newMessage = {
                user: {
                    id: data.user_id,
                    full_name: isCurrentUser ? 'You' : data.user_full_name
                },
                message: data.message,
                formattedDate: new Date().toLocaleString()
                };
            console.log('Evento newMessage capturado', data);
            $scope.messages.push(newMessage); 
            });
        });
    };
    $scope.sendMessage = function() {
        if ($scope.newMessage.trim() !== "" && $scope.clientId) {
            var messageData = {
                client_id: $scope.clientId,
                project_id: $scope.projectId,
                message: $scope.newMessage,
                user_id: $scope.currentUser.id
            };
            
            WebSocketService.sendMessage(messageData);

            $scope.newMessage = "";
        }
    };
    
    $scope.goBack = function() {
        $state.go('base.inbox');
    };

    $scope.loadProjectDetails();
    $scope.loadMessages();
}]);
