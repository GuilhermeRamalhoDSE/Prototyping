angular.module('frontend').controller('ClientController', ['$scope', 'ClientService', '$state', 'AuthService', function($scope, ClientService, $state, AuthService) {
    $scope.clients = [];
    $scope.newClient = {
        name: "",
        email: "",
        address: "",
        phone: "",
        license_id: AuthService.getLicenseId()
    };

    $scope.loadClients = function() {
        ClientService.getAll().then(function(response) {
            $scope.clients = response.data;
        });
    };

    $scope.goToNewClient = function() {
        $state.go('base.client-new');
    };
    
    $scope.createClient = function() {
        ClientService.create($scope.newClient).then(function(response) {
            alert('Client created successfully!');
            $state.go('base.client-view'); 
        }).catch(function(error) {
            console.error('Error creating client:', error);
        });
    };

    $scope.editClient = function(clientId) {
        $state.go('base.client-update', { clientId: clientId });
    };

    $scope.cancelCreate = function() {
        $state.go('base.client-view');
    };

    $scope.goBack = function() {
        $state.go('base.home');
    };

    $scope.viewProjects = function(clientId) {
        $state.go('base.project-view', { clientId: clientId });
    };
   
    $scope.deleteClient = function(clientId) {
        if (confirm('Are you sure you want to delete this client?')) {
            ClientService.delete(clientId).then(function(response) {
                alert('Client deleted successfully!');
                $scope.loadClients();
            }).catch(function(error) {
                console.error('Error deleting client:', error);
            });
        }
    };
    

    $scope.loadClients();
}]);
