module.exports = function (grunt) {
  var app = grunt.option('app');
  console.log("Running app:" + app);
  
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
              connect.static('src/app' + app)
            ];
          }
        }
      }
    },
    watch: {
      project: {
        files: ['src/app' + app + '/**/*.js',
                'src/app' + app + '/**/*.html',
                'src/app' + app + '/**/*.json',
                'src/app' + app + '/**/*.css'],
        options: {
          livereload: true
        }
      }
    },
  });

  grunt.loadNpmTasks('grunt-contrib-connect');
  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask('default', ['connect', 'watch']);

};
