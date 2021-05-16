from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import date
import time

def template():
    today = date.today()
    dates = today.strftime("%B %d, %Y")

    subject = 'COVID-19 worker and employee screening | passed | {}'.format(dates)
    message = """{}

    COVID-19 worker and employee screening result: passed

    =====================

    This result is no longer valid if your situation changes during the day (for example, you start experiencing symptoms).

    https://covid-19.ontario.ca/screening/worker/

    ====================

    This email is your personal record to archive or share. Please do not alter, modify or delete any of the content.
    The Government of Ontario does not record or retain your responses to our COVID-19 self-assessments, and we are not able to confirm the accuracy or authenticity of individual results.
    """.format(dates)
    return subject, message

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
    
def launchGmail(browser):
    subject, message = template()
    today = date.today()
    dates = today.strftime("%B %d, %Y")

    browser.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    email = browser.find_element_by_xpath('//*[@id="identifierId"]')
    email.send_keys('abdul.hafeezm02')
    email.send_keys(Keys.ENTER)
    time.sleep(2)
    password = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    password.send_keys('')
    password.send_keys(Keys.ENTER)
    time.sleep(4)

    browser.find_element_by_xpath('//*[@id=":kr"]/div/div').click()
    time.sleep(2)
    #receiver = browser.find_element_by_xpath('//*[@id=":qe"]').click()
    #receiver.send_keys('mohammadadil301@gmail.com')
    
    
    subjectLine = browser.find_element_by_xpath('//*[@id=":pn"]').click()
    subjectLine.send_keys(subject)

    messageLine = browser.find_element_by_xpath('//*[@id=":qs"]"]').click()
    messageLine.send_keys(message)

    browser.find_element_by_xpath('//*[@id=":pd"]').click()


driverPath = '/Users/adilmohammad/Desktop/VS_CODE/chromedriver'
binaryPath = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
options = webdriver.ChromeOptions()
options.binary_location = binaryPath
browser = webdriver.Chrome(executable_path=driverPath, chrome_options=options)

launchGmail(browser)
