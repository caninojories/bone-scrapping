(function() {
  'use strict';

  module.exports = function(options) {
    spawn_process();

    function spawn_process() {
      var cp = require('child_process').spawn,
          spw = cp('python', ['scrap.py', options.login_name, options.password_name,
          options.username_value, options.password_value,
          options.login_url, options.url_to_scrap, options.form_row]);
      spw.stdout.on('data', function (data) {
        console.log(data.toString());
        spw.kill();
      });
    }
  };
}());
