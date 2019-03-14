from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import glob
import os
import time
import requests
from bs4 import BeautifulSoup
import lxml.html as LH

class save_feds():
    @staticmethod
    def curyCon(doc_num):
        login = 'sqaappdev'
        password = 'sqaappdev'
        payload = {'RunTool': 'sps.webec.test.TestFormDataToFEDS'
            , 'ID': doc_num}

        url2 = 'http://sqawfweb05.hosted-commerce.net:8080/webec/servlet/sps.webec.server.servlets.admin.Utilities'

        s = requests.Session()

        r = s.post(url2, data=payload, auth=(login, password))

        soup = BeautifulSoup(r.text, 'html.parser')
        start = soup.find('br')
        end = soup.find('/br')
        content = ''
        item = start.nextSibling

        while item != end:
            content += str(item)
            item = item.nextSibling
        file = open("test.feds", "w")
        file.write(content[13:-182])
        file.close()

    @staticmethod
    def qury_Con():
        pp = r'C:/Users/izinovyev/PycharmProjects/WFchecking/phantomjs.exe'
        base_dir = "C:/Users/izinovyev/PycharmProjects/WFchecking/xout.edi"

        driver = webdriver.PhantomJS(pp)
        driver.get('https://www.edivalidation.com')

        driver.find_element_by_xpath('//*[@id="files"]').send_keys(base_dir)
        # driver.find_element_by_xpath('//*[@id="output-type"]/option[3]').click()
        wait = WebDriverWait(driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="downloadify"]')))
        # driver.find_element_by_xpath('//*[@id="downloadify"]').click()
        # time.sleep(2)

        file = open("testHTML.html", "w")
        file.write(driver.page_source)
        file.close()
        driver.close()



    @staticmethod
    def qury(doc_num):


        login = 'sqaappdev'
        password = 'sqaappdev'
        url2='http://' + login + ':' + password + '@' +"sqawfweb05.hosted-commerce.net:8080/webec/servlet/sps.webec.server.servlets.admin.Utilities?ChooseTool=sps.webec.test.TestFormDataToFEDS"
        url = 'http://sqawfweb05.hosted-commerce.net:8080/webec/servlet/sps.webec.server.servlets.admin.Utilities?ChooseTool=sps.webec.test.TestFormDataToFEDS'

        # for mac
        #driver = webdriver.Chrome('//Users/ihorzinoviev/PycharmProjects/WFchecking/hromedriverMac')
        # for Win
        driver = webdriver.Chrome('C:/Users/izinovyev/PycharmProjects/WFchecking/chromedriverWin')
        driver.get(url2)

        elem = driver.find_element_by_name("ID")
        elem.send_keys(doc_num)
        elem.submit()

        body = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/pre[1]");
        file = open("test.feds", "w")
        file.write(body.text)
        file.close()
        driver.close()

    @staticmethod
    def puschInweb():
        '''base_dir = "C:/Users/izinovyev/PycharmProjects/WFchecking/"
               path_to_image = os.path.join(base_dir, "xout.edi")

               response = requests.get("https://www.edivalidation.com/")

               if response.status_code == 200:
                   f = open(path_to_image, 'wb')
                   f.write(response.content)

                   file = open("testHTML.html", "w")
                   file.write(response.text)
                   f.close()'''
        #for Win
        base_dir = "C:/Users/izinovyev/PycharmProjects/WFchecking/xout.edi"
        #for Mac
        #base_dir = "/Users/ihorzinoviev/PycharmProjects/WFchecking/xout.edi"

        path_to_image = os.path.join(base_dir, "xout.edi")
        #global driver

        #for mac
        #driver = webdriver.Chrome('/Users/ihorzinoviev/PycharmProjects/WFchecking/chromedriverWin')
        #for Win
        driver = webdriver.Chrome('C:/Users/izinovyev/PycharmProjects/WFchecking/chromedriverWin')


        driver.get('https://www.edivalidation.com/valid.html')
        driver.find_element_by_xpath('//*[@id="files"]').send_keys(base_dir)
        driver.find_element_by_xpath('//*[@id="output-type"]/option[3]').click()

        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="downloadify"]')))


        '''chrome_options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': 'C:/Users/izinovyev/PycharmProjects/WFchecking/errors'}
        chrome_options.add_experimental_option('prefs', prefs)
        driver = webdriver.Chrome(chrome_options=chrome_options)'''


        driver.find_element_by_xpath('//*[@id="downloadify"]').click()

        time.sleep(2)
        driver.close()
        '''file_names = glob.glob('C:/Users/izinovyev/Downloads/edijson*')

        for name in file_names:
            print(name)

        file = open("C:/Users/izinovyev/Downloads/"+name[29:], "r")
        print(file)'''

        #driver.close()



        #driver.find_elements_by_id('downloadify').click()

        #file = open("testHTML.html", "w")
        #file.write()
        #//*[@id="downloadify"]
        #//*[@id="output-type"]/option[3]
        #// *[ @ id = "output-type"]



