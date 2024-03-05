module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        cssmin: {
            target: {
                files: [{
                    expand: true,
                    cwd: 'src/css', // Seu diretório de CSS fonte
                    src: ['*.css', '!*.min.css'],
                    dest: 'dist/css', // Seu diretório de destino para CSS minificado
                    ext: '.min.css'
                }]
            }
        },

        uglify: {
            options: {
                manage: false
            },
            my_target: {
                files: {
                    'dist/js/app.min.js': ['src/js/**/*.js'] // Adapte as pastas ao seu projeto
                }
            }
        },

        watch: {
            scripts: {
                files: ['src/js/**/*.js', 'src/css/**/*.css'],
                tasks: ['uglify', 'cssmin'],
                options: {
                    spawn: false,
                },
            },
        }
    });

    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');

    grunt.registerTask('default', ['cssmin', 'uglify']);
};
