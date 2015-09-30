Bone Scrapping
==================

##### npm install bone-scrapping

### Requirements
#### python

#### Then install the following:
##### pip install mechanize
##### pip install BeautifulSoup
##### pip install html2text


```
var bone_scrapping = require('bone-scrapping')(options);
```

```
options = {
  login_name    : 'input name attribute for login input',
  password_name : 'input name attribute for password input',
  username_value: 'value',
  password_value: 'value',
  login_url     : 'Log-in page of the website(URL)',
  url_to_scrap  : 'Page to scrap(URL)',
  form_row      : 'form index where the login is located' - starts with 0
}
```
```
Then call:

bone_scrapping.then(function(data) {
  /*it will return the page source code*/
})
```
