angular.module('frontend').controller('MessageController', ['$scope',  '$state', 'MessageService', '$stateParams', 'AuthService', function($scope, $state, MessageService, $stateParams, AuthService) {  
    $scope.messages = [];
    $scope.newMessage = "";
    $scope.currentUser = {
        id: parseInt(AuthService.getUserId(), 10)
    };

    $scope.projectId = $stateParams.projectId;
    $scope.loadMessages = function() {
        MessageService.getMessagesForProject($scope.projectId).then(function(response) {
            $scope.messages = response.data.map(function(message) {
                message.formattedDate = new Date(message.date).toLocaleString();
                return message;
            });            
    
            if ($scope.messages.length > 0) {
                $scope.clientId = $scope.messages[0].client_id;
            }
        }, function(error) {
            console.error("Error loading messages:", error.statusText);
        });
    };
      
    $scope.sendMessage = function() {
        if ($scope.newMessage.trim() !== "") {
            var messageData = {
                client_id: $scope.clientId,
                project_id: $scope.projectId,
                message: $scope.newMessage,
                user_id: $scope.currentUser.id
            };
            MessageService.sendMessage(messageData).then(function(response) {
                $scope.messages.push(response.data);
                $scope.newMessage = "";
            }, function(error) {
                console.error("Error sending message:", error.statusText);
            });
        }
    };
    $scope.goBack = function() {
        $state.go('base.inbox');
    };  
    
    $scope.loadMessages();
}]);
