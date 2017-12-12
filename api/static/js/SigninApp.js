angular.module('SigninApp', [])
  .controller('SigninController', ['$scope', '$http', function($scope, $http) {
    $scope.message = 'I love JavaScript!';

    $scope.signin = function (user){
      credentials = JSON.stringify({"userEmail": user.email, "password": user.password});
	   // Submit the credentials
     $http.post('http://lists.hopto.org:61340/signin', credentials ).then(function(data) {
        // Success here means the transmission was successful - not necessarily the login.
        // The data.status determines login success
        if(data.status == 201) {
          // You're in!
          // But does the session carry? Let's try some other endpoint that requires a login
           $http.get('https://info3103.cs.unb.ca:61340/hello').then( function(data){
                           $scope.message = data.data.message;
            });
       }
    });
}}]);
