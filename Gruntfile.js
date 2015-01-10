// Source: http://24ways.org/2013/grunt-is-not-weird-and-hard/
module.exports = function(grunt) {

    // 1. All configuration goes here 
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        concat: {
        // 2. Configuration for concatinating files goes here.
        js: {
            src: [
        // JS libraries
        'static/bower_components/jquery/dist/jquery.min.js',
        'static/bower_components/jquery-ui/jquery-ui.min.js',
        'static/bower_components/moment/min/moment.min.js',
        'static/bower_components/moment-timezone/builds/moment-timezone-with-data.min.js',
        'static/bower_components/bootstrap/dist/js/bootstrap.min.js',
        ],
        dest: 'static/js/libraries.js',
    },
    css: {
        src: [
        // CSS libraries
        'static/bower_components/bootstrap/dist/css/bootstrap.min.css',
        'static/bower_components/jquery-ui/themes/smoothness/jquery-ui.min.css'
        ],
        dest: 'static/css/libraries.css'
    }
},
cssmin: {
  target: {
    files: [{
    // Minify all contents of a release directory and add a .min.css extension
      expand: true,
      cwd: 'static/css',
      src: ['*.css', '!*.min.css'],
      dest: 'static/css',
      ext: '.min.css'
  }]
}
},

uglify: {
    build: {
        //  Minify js files
        src: 'static/js/libraries.js',
        dest: 'static/js/libraries.min.js'
    }
},

watch: {
    scripts: {
        files: ['static/js/*.js', 'static/css/*.css'],
        tasks: ['concat', 'uglify', 'cssmin'],
        options: {
            spawn: false,
        },
    } 
}

});

    // 3. Where we tell Grunt we plan to use this plug-in.
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-cssmin');

    // 4. Where we tell Grunt what to do when we type "grunt" into the terminal.
    grunt.registerTask('default', ['concat', 'uglify', 'cssmin']);

};