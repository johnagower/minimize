// Include Gulp
var gulp = require('gulp');

// Include Our Plugins
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var rename = require('gulp-rename');
var autoprefixer = require('autoprefixer');
var postcss = require('gulp-postcss');

// Compile Our Sass
gulp.task('sass', function() {
	return gulp.src('inventory/static/scss/*.scss')
		.pipe(sass())
		.pipe(gulp.dest('inventory/static/css'));
});

// Concatenate
gulp.task('scripts', function() {
	return gulp.src('inventory/static/js/*.js')
		.pipe(concat('all.js'))
		.pipe(gulp.dest('inventory/static/js'));
});

// PostCSS processor
gulp.task('css', function () {
	var processors = [
		autoprefixer({browsers: ['last 1 version']}),
	];
	return gulp.src('inventory/static/css/*.css')
		.pipe(postcss(processors))
		.pipe(gulp.dest('inventory/static/css'))
});

// Watch Files For Changes
gulp.task('watch', function() {
	gulp.watch('inventory/static/js/*.js', ['scripts']);
	gulp.watch('inventory/static/scss/*.scss', ['sass']);
	gulp.watch('inventory/static/css/*.css', ['css']);
});

// Default Task
gulp.task('default', ['sass', 'css', 'scripts', 'watch']);