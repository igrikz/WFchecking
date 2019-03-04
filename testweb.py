import requests
login = 'sqaappdev'
password = 'sqaappdev'
payload = {'ID':'424735'}
url = 'http://sqawfweb05.hosted-commerce.net:8080/webec/servlet/sps.webec.server.servlets.admin.Utilities?ChooseTool=sps.webec.test.TestFormDataToFEDS'
s = requests.Session()
r=s.get(url)
r = s.post(url,data=payload ,auth=(login, password))

file = open("testHTML.html", "w")
file.write(r.text)
file.close()
