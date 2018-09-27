'use strict';

/**
 * @ngdoc function
 * @name webApp.service:TestService
 * @description
 * # LinksService
 * Service of the webApp
 */

(function() {
  angular.module('webApp')
    .factory('TestService', [function() {
      var links = [];

      links = [
        {id: 0, title:'google', url:'www.google.com', date: new Date(Date.now())},
        {id: 1, title:'facebook', url:'www.facebook.com', date: new Date(Date.now())},
        {id: 2, title:'whatsapp', url:'www.whatsapp.com', date: new Date(Date.now())},
        {id: 3, title:'netflix', url:'www.netflix.com', date: new Date(Date.now())}
      ];

      function getLinks(){
        return links;
      };

      return {
        getLinks: getLinks
      };
    }]
  );

})();
