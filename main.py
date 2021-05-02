from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import date
import time

def launchScreener(browser):
    browser.get('https://covid-19.ontario.ca/screening/worker/')

    browser.find_element_by_xpath('//button[normalize-space()="Start screening"]').click()
    time.sleep(0.2)
    browser.find_element_by_xpath('//input[contains(@id,"18+")]').click()
    browser.find_element_by_xpath('//button[normalize-space()="Continue"]').click()
    time.sleep(0.2)
    browser.find_element_by_xpath('//input[contains(@id,"none_of_the_above")]').click()
    browser.find_element_by_xpath('//button[normalize-space()="Continue"]').click()
    time.sleep(0.2)
    for i in range(5):
        browser.find_element_by_xpath('//button[normalize-space()="No"]').click()
        time.sleep(0.2)
    time.sleep(0.3)
    browser.find_element_by_xpath('//*[@id="reach-skip-nav"]/div[2]/div[2]/a/div').click()
    while(True):
        pass

def lauchGmail(browser):
    browser.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    email = browser.find_element_by_xpath('//*[@id="identifierId"]')
    email.send_keys('mohammadadil301')
    email.send_keys(Keys.ENTER)
    today = date.today()

    while(True):
        pass
browser = webdriver.Chrome(executable_path=r"/Users/adilmohammad/Desktop/Covid19_Screener/chromedriver")

lauchGmail(browser)
'''from datetime import date
today = date.today()

d2 = today.strftime("%B %d, %Y")
print(d2)'''

