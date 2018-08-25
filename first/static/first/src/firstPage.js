/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


var app = angular.module("app",[]);

app.controller("bankController",['$scope','$window',function($scope, $window){
        var bankController = this;
        bankController.confirmPayment = function(amount){
            $window.open("/FIrst/bank.html");
        };
    
    
}]);

app.controller("loginCtrl",['$scope','$window',function($scope, $window){
    $scope.opacity="opacity(100%)";
    $scope.products = [
        {
            name: "5000 Series",
            price: "77,589.99",
            desc: "Gaming laptops engineered with NVIDIA, 8th Gen Intel® processors and a thin design for a sleek gaming experience."
        },
        {
            name: "G7",
            price: "1,06,090.00",
            desc: "38.1 cm gaming laptop designed for a powerful, immersive in-game experience featuring NVIDIA GeForce GTX 1060 graphics and the latest 8th Gen Intel Quad-and-Hex Core™ CPUs, up to i9."
        },
        {
            name: "XPS 15",
            price: "2,31,499.00",
            desc: "Dell's smallest 39.6cm (15) performance laptop with a stunning InfinityEdge display. Now featuring 8th Gen Intel® Core™ processors with up to 6 cores and 12 threads."
        }
    ];
    $scope.desktop = $scope.products[0];
    $scope.laptop1 = $scope.products[1];
    $scope.laptop2 = $scope.products[2];
    $scope.view = "none";
    $scope.buy = function(name){
    if(name === "5000 Series")
        $scope.amount = $scope.products[0].price;
    else if(name === "G7")
        $scope.amount = $scope.products[1].price;
    else if(name === "XPS 15")
        $scope.amount = $scope.products[2].price;
    $scope.view = "block";
    $scope.opacity = "opacity(30%)";
    };
 
    $scope.cardNo = "1234-5678-0912-3456";
    $scope.cardholderName = "xyz sharma";
    
    $scope.cancel = function(){
        $scope.view = "none";
        $scope.opacity = "opacity(100%)";
    };
    
    $scope.confirmPayment = function(amount){
        $window.open("/FIrst/bank.html");
    };
    
    $scope.signIn = function(){
        
    };
}]);

