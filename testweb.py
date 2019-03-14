import glob
import json
import requests
from bs4 import BeautifulSoup
import lxml.html as LH

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


pp=r'C:/Users/izinovyev/PycharmProjects/WFchecking/phantomjs.exe'
base_dir = "C:/Users/izinovyev/PycharmProjects/WFchecking/xout.edi"
dow = "C:/Users/izinovyev/PycharmProjects/WFchecking/testHTML.txt"
driver = webdriver.PhantomJS(pp)
driver.get('https://www.edivalidation.com')

driver.find_element_by_xpath('//*[@id="files"]').send_keys(base_dir)
#driver.find_element_by_xpath('//*[@id="output-type"]/option[3]').click()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="downloadify"]')))
#download_link=driver.find_element_by_xpath('//*[@id="downloadify"]').click()




#time.sleep(2)

file = open("testHTMLtest.html", "w")
file.write(driver.page_source)
file.close()



erros=''
'''root = LH.fromstring(driver.page_source)
for elt in root.xpath('//*[@id="results"]/div[2]/div[3]/div[2]'):
    erros+=str(elt.text_content())
    erros+='<br>'


    #print(' $ '.join(elt.text_content().split()))'''
file = open("testHTMLtest.html", "r")
soup = BeautifulSoup(file.read(),features="lxml")
tbody=soup.find_all('tbody')
errros=''

err={}
for i in tbody:

     if i.find_all('tr')[0].find_all('td')[2].text!='EF - Element functional rule failed':
          tr=i.find_all('tr')[2:]
          err=dict(segmentWithError=i.find_all('tr')[0].find_all('td')[1].text,message=i.find_all('tr')[2].find_all('td')[0].text,value=i.find_all('tr')[2].find_all('td')[1].text,data=i.find_all('tr')[4].find_all('td')[0])
          errros += ("<h2>Segment With Error:  {0}</h1>" + i.find_all('tr')[0].find_all('td')[1].text +
                     "<h2>Message:  {0}</h1>" + i.find_all('tr')[2].find_all('td')[0].text +
                     "<h2>Value:  {0}</h1>" + i.find_all('tr')[2].find_all('td')[1].text +
                     "<h2>X12:  {0}</h1>" + i.find_all('tr')[4].find_all('td')[0].text)
if errros=='':
     print("hrennn")
else: print(errros)









file = open("testHTML.html", "w")
file.write(errros)
file.close()
print(erros)



