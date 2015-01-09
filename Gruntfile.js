// Source: http://24ways.org/2013/grunt-is-not-weird-and-hard/
module.exports = function(grunt) {

    // 1. All configuration goes here 
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        concat: {
            // 2. Configuration for concatinating files goes here.
            dist: {
                src: [
            // JS libraries
            'static/bower_components/jquery/dist/jquery.min.js',
            'static/bower_components/jquery-ui/jquery-ui.min.js',
            'static/bower_components/moment/min/moment.min.js',
            'static/bower_components/moment-timezone/builds/moment-timezone-with-data.min.js',
            'static/bower_components/bootstrap/dist/js/bootstrap.min.js',
            ],
            dest: 'static/js/libraries.js',
        }
    }

});

    // 3. Where we tell Grunt we plan to use this plug-in.
    grunt.loadNpmTasks('grunt-contrib-concat');

    // 4. Where we tell Grunt what to do when we type "grunt" into the terminal.
    grunt.registerTask('default', ['concat']);

};