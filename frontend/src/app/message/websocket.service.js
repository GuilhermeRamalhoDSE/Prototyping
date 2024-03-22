angular.module('frontend').factory('WebSocketService', ['$rootScope', function($rootScope) {
    var service = {};
    var ws;

    service.connect = function(projectId) {
        if (ws) {
            console.log("Closing existing WebSocket connection.");
            ws.close();
        }
        
        var wsUrl = 'ws://localhost:8000/ws/chat/' + projectId + '/';
        console.log("Connecting to", wsUrl);
        ws = new WebSocket(wsUrl);

        ws.onopen = function() {
            console.log('WebSocket connected');
        };

        ws.onmessage = function(message) {
            var data = JSON.parse(message.data);
            $rootScope.$broadcast('newMessage', data);
            console.log('Message received:', data);
        };

        ws.onclose = function() {
            console.log('WebSocket disconnected');
        };

        ws.onerror = function(event) {
            console.error('WebSocket error observed:', event);
        };
    };

    service.sendMessage = function(message) {
        if (ws && ws.readyState === WebSocket.OPEN) {
            console.log("Sending message:", message);
            ws.send(JSON.stringify(message));
        } else {
            console.log("WebSocket is not open.");
        }
    };

    return service;
}]);
