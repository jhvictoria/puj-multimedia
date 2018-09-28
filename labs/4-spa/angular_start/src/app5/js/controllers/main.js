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
      'TestService',
      MainCtrl]);

  function MainCtrl($scope, $mdMedia, $mdSidenav, TestService) {
    $scope.links = TestService.getLinks();

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
  }

})();
