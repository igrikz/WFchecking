import glob
import json
'''import requests
login = 'sqaappdev'
password = 'sqaappdev'
payload = {'ID':'424735'}
url = 'http://sqawfweb05.hosted-commerce.net:8080/webec/servlet/sps.webec.server.servlets.admin.Utilities?ChooseTool=sps.webec.test.TestFormDataToFEDS'
s = requests.Session()
r=s.get(url)
r = s.post(url,data=payload ,auth=(login, password))

file = open("testHTML.html", "w")
file.write(r.text)
file.close()'''
file_names = glob.glob('C:/Users/izinovyev/Downloads/edijson*')

for name in file_names:
    name
#file = open("C:/Users/izinovyev/Downloads/" + name[29:], "r")

dicts_from_file = {}

print(name[29:])
with open("C:/Users/izinovyev/Downloads/" + name[29:], 'r') as inf:
    for line in inf:
        dicts_from_file = json.loads(line)
        print(dicts_from_file["segmentWithError"]+': '+dicts_from_file["message"] + " Value: "+ dicts_from_file["value"] + " Path: "+dicts_from_file["errorHashCode"])

#print(file.read())
