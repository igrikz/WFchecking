import glob
import json
import requests
from bs4 import BeautifulSoup
import lxml.html
'''url='https://www.edivalidation.com/load'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
data={'release':'4010','tsNum':'810'}
files = {'accept': open('xout.edi', 'rb')}

s = requests.Session()
r = s.get(url, files=files,params=data)

print(r)
file = open("testHTML.html", "w")
file.write(r.text)
file.close()'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


pp=r'C:/Users/izinovyev/PycharmProjects/WFchecking/phantomjs.exe'
base_dir = "C:/Users/izinovyev/PycharmProjects/WFchecking/xout.edi"

driver = webdriver.PhantomJS('C:/Users/izinovyev/PycharmProjects/WFchecking/phantomjs.exe')
driver.get('https://www.edivalidation.com/valid.html')

driver.find_element_by_xpath('//*[@id="files"]').send_keys(base_dir)
driver.find_element_by_xpath('//*[@id="output-type"]/option[3]').click()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="downloadify"]')))
driver.find_element_by_xpath('//*[@id="downloadify"]').click()
time.sleep(2)
driver.save_screenshot('screen.png')
file = open("testHTML.html", "w")
file.write(driver.page_source)



from bs4 import BeautifulSoup
