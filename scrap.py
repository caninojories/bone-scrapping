#!/usr/bin/env python

import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup
import html2text
import sys

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
# br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Chrome')]

# The site we will navigate into, handling it's session
br.open(sys.argv[5])
br.select_form(nr = int(sys.argv[7]))

br.form[sys.argv[1]] = sys.argv[3]
br.form[sys.argv[2]] = sys.argv[4]

br.submit()

print(br.open(sys.argv[6]).read())
