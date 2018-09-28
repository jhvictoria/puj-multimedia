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
  }

})();
