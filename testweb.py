import glob
import json
import requests
from bs4 import BeautifulSoup
import lxml.html
login = 'sqaappdev'
password = 'sqaappdev'
payload = {'RunTool': 'sps.webec.test.TestFormDataToFEDS'
    ,'ID':'426974'}

url2='http://sqawfweb05.hosted-commerce.net:8080/webec/servlet/sps.webec.server.servlets.admin.Utilities'

s = requests.Session()

r = s.post(url2,data=payload,auth=(login, password))


soup = BeautifulSoup(r.text, 'html.parser')
start = soup.find('br')
end = soup.find('/br')
content = ''
item = start.nextSibling

while item != end:
  content += str(item)
  item = item.nextSibling




#new_releases = doc.xpath('/html/body/table/tbody/tr/td[1]/pre[1]/br[1]').
#/html/body/table/tbody/tr/td[1]/pre[1]/br[1]
#body > table > tbody > tr > td:nth-child(1) > pre:nth-child(6) > br:nth-child(1)


#print(ee.get_text(separator='<br>'))
file = open("test2.feds", "w")
file.write(content[13:-182])
file.close()

