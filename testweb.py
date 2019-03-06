import glob
import json
import requests
from bs4 import BeautifulSoup

login = 'sqaappdev'
password = 'sqaappdev'
payload = {'RunTool': 'sps.webec.test.TestFormDataToFEDS'
    ,'ID':'424735'}

url2='http://sqawfweb05.hosted-commerce.net:8080/webec/servlet/sps.webec.server.servlets.admin.Utilities'

s = requests.Session()

r = s.post(url2,data=payload,auth=(login, password))
soup = BeautifulSoup(r.content, 'html.parser')
html=

body > table > tbody > tr > td:nth-child(1) > pre:nth-child(6) > br:nth-child(1)

print(row)
#print(ee.get_text(separator='<br>'))
file = open("test.feds", "w")
file.write(r.text)
file = open("testHTML.html", "w")
file.write(r.text)
file.close()

