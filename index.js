(function() {
  'use strict';

  module.exports = function(options) {
    return new Promise(function(resolve, reject) {
      var path      =  require('path'),
          rootPath  = path.normalize(__dirname + '/'),
          cp        = require('child_process').exec,
          cmd       = 'python ' + rootPath + 'scrap.py ' + options.login_name + ' ' + options.password_name + ' ' +
          options.username_value + ' ' + options.password_value + ' ' + options.login_url + ' ' +
          options.url_to_scrap + ' ' + options.form_row;

        cp(cmd, {maxBuffer : 500 * 1024}, function(error, stdout, stderr) {
          if (error) {
            console.log('Erorr: ' + error);
            return reject(error);
          }
          return resolve(stdout);
        });
    });
  };
}());
