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
      MainCtrl]);

  function MainCtrl($scope) {
    $scope.title = "Hola!";
    console.log($scope);

    $scope.clickMenu = function(menu){
      console.log(menu)
    };

    $scope.show = true;

    $scope.hide = true;

    $scope.toggleShow = function(){
      $scope.show = !$scope.show;
    }

    $scope.toggleHide = function(){
      $scope.hide = !$scope.hide;
    }
  }

})();
