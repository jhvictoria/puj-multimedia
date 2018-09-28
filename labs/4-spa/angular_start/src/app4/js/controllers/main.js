'use strict';

(function() {

  /**
   * @ngdoc function
   * @name webApp.controller:MainCtrl
   * @description
   * # MainCtrl
   * Controller of the webApp
   */
  angular.module('webApp')
    .controller('MainCtrl', [
      '$scope',
      '$mdMedia',
      '$mdSidenav',
      MainCtrl]);

  function MainCtrl($scope, $mdMedia, $mdSidenav) {
    $scope.title = "Hola!!";

    $scope.getMinRes = function(){
      return $mdMedia('gt-xs');
    };

    $scope.openLeftMenu = function() {
      console.log("left");
      $mdSidenav('left').toggle();
    };

    $scope.clickMenu = function(menu){
      console.log("clicked " + menu)
    };

    $scope.$watch(function() { 
      console.log($mdMedia('gt-xs'));
      return $mdMedia('gt-xs'); 
    });
  }

})();
