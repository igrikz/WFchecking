import requests
from requests import request

import web_qury
import File_x12
wc=web_qury.save_feds()
conv=File_x12.creats_x12()




wc.qury("425448")
conv.spFeds()
wc.puschInweb()

'''login = 'sqaappdev'
password = 'sqaappdev'
payload = {'ID':'424735'}

s = requests.Session()
r = s.post(url,data=payload ,auth=(login, password))

file = open("testHTML.html", "w")
file.write(r.text)
file.close()'''







