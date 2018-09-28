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
      'ngMaterial',
      'ngTagsInput'
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
    })
    .config(function($mdThemingProvider) {
      $mdThemingProvider.theme('default')
      .primaryPalette('blue');
      //.accentPalette('red');
    });

})();
