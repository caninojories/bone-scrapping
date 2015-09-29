#!/usr/bin/env python

import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup
import html2text
import sys

# Browser
br = mechanize.Browser()
login_name      = sys.argv[1]
password_name   = sys.argv[2]
username_value  = sys.argv[3]
password_value  = sys.argv[4]
login_url       = sys.argv[5]
url_to_scrap    = sys.argv[6]
form_row        = sys.argv[7]

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Chrome')]

# The site we will navigate into, handling it's session
br.open(login_url)
br.select_form(nr = int(form_row))

br.form[login_name]     = username_value
br.form[password_name]  = password_value

br.submit()

print br.open(url_to_scrap).read()
