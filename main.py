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


def launchGmail(browser):
    today = date.today()
    dates = today.strftime("%B %d, %Y")

    browser.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    email = browser.find_element_by_xpath('//*[@id="identifierId"]')
    email.send_keys('REDACTED')
    email.send_keys(Keys.ENTER)
    time.sleep(2)
    password = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    password.send_keys('REDACTED')
    password.send_keys(Keys.ENTER)
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id=":bg"]/div/div[2]')
    browser.send_keys(Keys.SHIFT + "d")

    receiver = browser.find_element_by_xpath('//*[@id=":gs"]')
    receiver.send_keys('REDACTED')
    receiver.send_keys(Keys.ENTER)

    subject = browser.find_element_by_xpath('//*[@id=":ga"]')
    header = 'COVID-19 worker and employee screening | passed | {}'.format(dates)
    subject.send_keys(header)
    

    while(True):
        pass

browser = webdriver.Chrome(executable_path=r"/Users/REDACTED/Desktop/VS_CODE/chromedriver")

launchScreener(browser)
browser.quit()
