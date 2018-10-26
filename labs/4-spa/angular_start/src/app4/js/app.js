'use strict';

(function() {
  /**
   * @ngdoc overview
   * @name webApp
   * @description
   * # webApp
   *
   * Main module of the application.
   */
  angular
    .module('webApp', [
      'ngAnimate',
      'ngCookies',
      'ngResource',
      'ngRoute',
      'ngSanitize',
      //'ngTouch',
      'ngMaterial'
    ])
    .config(function($routeProvider) {
      $routeProvider
        .when('/', {
          templateUrl: 'views/main.html',
          controller: 'MainCtrl',
          controllerAs: 'main'
        })
        .otherwise({
          redirectTo: '/'
        });
    });

})();
