angular.module('frontend').controller('MessageController', ['$scope', 'MessageService', '$stateParams', 'AuthService', function($scope, MessageService, $stateParams, AuthService) {
    $scope.messages = [];
    $scope.newMessage = "";
    $scope.currentUser = {
        id: parseInt(AuthService.getUserId(), 10)
    };

    $scope.projectId = $stateParams.projectId;

    $scope.loadMessages = function() {
        MessageService.getMessagesForProject($scope.projectId).then(function(response) {
            $scope.messages = response.data;
        }, function(error) {
            console.error("Error loading messages:", error.statusText);
        });
    };

    $scope.sendMessage = function() {
        if ($scope.newMessage.trim() !== "") {
            var messageData = {
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

    $scope.loadMessages();
}]);
