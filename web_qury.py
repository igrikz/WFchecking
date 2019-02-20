from selenium import webdriver
import requests
import os
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys

class save_feds():
    @staticmethod
    def qury(doc_num):

        login = 'sqaappdev'
        password = 'sqaappdev'
        url2='http://' + login + ':' + password + '@' +"sqawfweb05.hosted-commerce.net:8080/webec/servlet/sps.webec.server.servlets.admin.Utilities?ChooseTool=sps.webec.test.TestFormDataToFEDS"
        url = 'http://sqawfweb05.hosted-commerce.net:8080/webec/servlet/sps.webec.server.servlets.admin.Utilities?ChooseTool=sps.webec.test.TestFormDataToFEDS'

        # for mac
        driver = webdriver.Chrome('//Users/ihorzinoviev/PycharmProjects/WFchecking/chromedriver 2')
        # for Win
        # driver = webdriver.Chrome('C:\WORK\chromedriver')
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
        '''base_dir = "C:/Users/izinovyev/PycharmProjects/checkFEDS/"
               path_to_image = os.path.join(base_dir, "xout.edi")

               response = requests.get("https://www.edivalidation.com/")

               if response.status_code == 200:
                   f = open(path_to_image, 'wb')
                   f.write(response.content)

                   file = open("testHTML.html", "w")
                   file.write(response.text)
                   f.close()'''
        #for Win
        #base_dir = "C:/Users/izinovyev/PycharmProjects/checkFEDS/xout.edi"
        #for Mac
        base_dir = "/Users/ihorzinoviev/PycharmProjects/WFchecking/xout.edi"

        path_to_image = os.path.join(base_dir, "xout.edi")
        global driver

        #for mac
        driver = webdriver.Chrome('/Users/ihorzinoviev/PycharmProjects/WFchecking/chromedriver 2')
        #for Win
        #driver = webdriver.Chrome('C:\WORK\chromedriver')

        driver.get('https://www.edivalidation.com/valid.html')

        driver.find_element_by_xpath('//*[@id="files"]').send_keys(base_dir)
        file = open("testHTML.html", "w")








#save_feds.puschInweb()
