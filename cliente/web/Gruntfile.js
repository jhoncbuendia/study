module.exports = function(grunt) {
  // Do grunt-related things in here
  grunt.initConfig({
    stylus: {
            release: {
                files: { 'index/css/index.css': ['index/css/index.styl'],


                        },
                options: { compress: true, linenos: false },

            }
        },
    watch: {
        options: { livereload: true },
        styles: {
            files: ['index/css/index.styl',
                  
            ],
            tasks: ['stylus']
        },
        html: {
            files: ['index.html'] // no tasks, just live reload
        }
    },
    connect: {
      server: {
        options: {
          port: 8000,
          base: './',
          keepalive:true
        }
      },
    }
  });


  grunt.loadNpmTasks('grunt-contrib-connect');
  grunt.loadNpmTasks('grunt-contrib-stylus');
  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask("tarea", function(){
    console.log("ejecutando una tarea");
  });


};
