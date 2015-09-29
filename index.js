(function() {
  'use strict';

  module.exports = function(options) {
    return new Promise(function(resolve, reject) {
      var cp = require('child_process').exec,
          spw = cp('python', ['scrap.py', options.login_name, options.password_name,
          options.username_value, options.password_value,
          options.login_url, options.url_to_scrap, options.form_row]);

          var cmd = 'python scrap.py ' + options.login_name + ' ' + options.password_name + ' ' +
          options.username_value + ' ' + options.password_value + ' ' + options.login_url + ' ' +
          options.url_to_scrap + ' ' + options.form_row;

        cp(cmd, function(error, stdout, stderr) {
          spw.kill();
          return resolve(console.log(stdout));
        });
    });
  };
}());
