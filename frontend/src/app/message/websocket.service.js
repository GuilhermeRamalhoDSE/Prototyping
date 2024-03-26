angular.module('frontend').factory('WebSocketService', ['$rootScope', function($rootScope) {
    var service = {};
    var ws;

    service.connect = function(projectId) {
        if (ws) {
            console.log("Closing existing WebSocket connection.");
            ws.close();
        }
        
        var wsUrl = 'ws://localhost:8000/ws/chat/' + projectId + '/';
        ws = new WebSocket(wsUrl);

        ws.onopen = function() {
            console.log('WebSocket connected', ws.readyState);
        };

        ws.onmessage = function(message) {
            var data = JSON.parse(message.data);
            console.log("Received message:", data);
            $rootScope.$broadcast('newMessage', data);
        };

        ws.onclose = function() {
            console.log('WebSocket disconnected', ws.readyState);
        };

        ws.onerror = function(event) {
            console.error('WebSocket error observed:', event, 'State:', ws.readyState);
        };
    };

    service.sendMessage = function(message) {
        if (ws) {
            if (ws.readyState === ws.OPEN) {
                const messageString = JSON.stringify(message);
                ws.send(messageString);
            } else {
                console.log("WebSocket is not open. Current state:", ws.readyState);
            }
        } else {
            console.log("WebSocket connection does not exist.");
        }
    };

    return service;
}]);
