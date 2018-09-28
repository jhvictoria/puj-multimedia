module.exports = function (grunt) {

  grunt.initConfig({
    connect: {
      options: {
        port: 8000,
        hostname: '0.0.0.0',
        livereload: 35729
      },
      livereload: {
        options: {
          open: true,
          middleware: function (connect) {
            return [
              connect().use(
                '/bower_components',
                connect.static('./bower_components')
              ),
              connect.static('src/ui')
            ];
          }
        }
      }
    },
    watch: {
      project: {
        files: ['src/ui/**/*.js',
                'src/ui/**/*.html',
                'src/ui/**/*.json',
                'src/ui/**/*.css'],
        options: {
          livereload: true
        }
      },
      express: {
        files:  [ 'src/server/app.js' ],
        tasks:  [ 'express' ],
        options: {
          spawn: false
        }
      }
    },
    express: {
      options: {
        port: 3000,
        debug: true
      },
      server: {
        options: {
          script: 'src/server/app.js'
        }
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-connect');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-express-server');

  grunt.registerTask('default', ['connect', 'express', 'watch']);

};
