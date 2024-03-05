module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        cssmin: {
            target: {
                files: [{
                    expand: true,
                    cwd: 'src/assets/css',
                    src: ['*.css', '!*.min.css'],
                    dest: 'dist/assets/css',
                    ext: '.min.css'
                }]
            }
        },

        uglify: {
            my_target: {
                files: {
                    'dist/app/app.min.js': ['src/app/**/*.js'],
                    'dist/libs/libs.min.js': ['src/libs/**/*.js'] 
                }
            }
        },

        watch: {
            css: {
                files: ['src/assets/css/**/*.css'],
                tasks: ['cssmin']
            },
            js: {
                files: ['src/app/**/*.js', 'src/libs/**/*.js'],
                tasks: ['uglify']
            }
        },

        connect: {
            server: {
                options: {
                    port: 8080,
                    base: 'src',
                    open: true,
                    livereload: true,
                    hostname: 'localhost'
                }
            }
        }
    });

 
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-connect'); 
    grunt.registerTask('default', ['cssmin', 'uglify']);
    grunt.registerTask('serve', ['connect:server', 'watch']); 
    grunt.registerTask('build', ['cssmin', 'uglify']);
};
