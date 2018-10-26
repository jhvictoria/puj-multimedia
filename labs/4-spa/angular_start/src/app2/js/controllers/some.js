'use strict';

(function() {
  angular.module('webApp')
    .controller('SomeCtrl', [
      '$scope',
      SomeCtrl]);

  function SomeCtrl($scope) {
    $scope.title = "Some";
    console.log($scope.title);
  }

})();
