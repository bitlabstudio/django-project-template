// Install npm, then `cd` into this directory and run `npm install`.
// Then start the watcher with `grunt watch`
//
module.exports = function(grunt) {
    grunt.initConfig({
        less: {
            development: {
                options: {
                    paths: ["var_project_name/static/css"],
                },
                files: {"var_project_name/static/css/bootstrap.css": "var_project_name/static/css/bootstrap.less"}
            }
        },
        watch: {
            less: {
                files: ['var_project_name/static/css/**/*.less'],
                tasks: ['less'],
                options: {
                    // Start a live reload server on the default port 35729
                    livereload: true,
                    livereloadOnError: false
                }
            },
            html: {
                files: ['**/*.html'],
                options: {
                    livereload: true
                }
            }
        }
    });
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-shell');
};
