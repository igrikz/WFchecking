import glob
import json
import requests
from bs4 import BeautifulSoup
import lxml.html
url='https://www.edivalidation.com/load'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
data={'release':'4010','tsNum':'810'}
files = {'value': open('xout.edi', 'rb')}

s = requests.Session()
r = s.get(url, files=files,params=data,headers=headers)

print(r.text)
file = open("testHTML.html", "w")
file.write(r.text)
file.close()

from mechanize import Browser, urlopen, Request

