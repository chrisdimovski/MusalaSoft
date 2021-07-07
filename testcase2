from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import os


PATH = r"C:\Users\Kristijan\Desktop\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.implicitly_wait(1)
BaseURL = "https://www.musala.com/"
JoinUsURL = "https://www.musala.com/careers/join-us/"
driver.get(BaseURL)

driver.execute_script("document.getElementsByClassName('main-link')[4].click();")

driver.find_element(By.XPATH, "//span[@data-alt='Check our open positions']").click()

CurrentURL = driver.current_url
if JoinUsURL == CurrentURL:
    print("'Join us' page URL is correct")

driver.find_element(By.XPATH, "//option[@value='Anywhere']").click()

driver.find_element(By.XPATH, "//h2[@data-alt='Experienced Automation QA Engineer']").click()

if (driver.find_element_by_xpath("//div[@class='square square-requirements']").is_displayed()):
    print("General description section is present")

if (driver.find_element_by_xpath("//div[@class='square square-advantages']").is_displayed()):
    print("Requirements section is present")

if (driver.find_element_by_xpath("//div[@class='square square-expectations']").is_displayed()):
    print("Requirements section is present")

if (driver.find_element_by_xpath("//div[@class='square square-offer']").is_displayed()):
    print("'What we offer' section is present")

if (driver.find_element_by_xpath("//input[@value='Apply']").is_displayed()):
    print("'Apply' button is present")

driver.find_element(By.XPATH, "//input[@value='Apply']").click()


def clearForm():
    if driver.find_element_by_class_name('message-form-content').is_displayed():
        if driver.find_element_by_class_name('close-form').is_displayed():
            driver.execute_script("document.getElementsByClassName('close-form')[0].click();")

def uploadFile():
    if driver.find_element_by_id("uploadtextfield").is_displayed():
        driver.find_element_by_id("uploadtextfield").clear()
        upload = driver.find_element_by_id("uploadtextfield")
        upload.send_keys(os.getcwd() + '/data/qa.pdf')


        driver.execute_script(
            "document.getElementsByClassName('wpcf7-form-control wpcf7-submit btn-cf-submit')[0].click();");
    if driver.find_element_by_class_name('close-form').is_displayed():
        driver.execute_script("document.getElementsByClassName('close-form')[0].click();")


with open('./data/test2data.json') as json_file:
    data = json.load(json_file)

    for i in data['users']:
        clearForm()
        driver.find_element_by_id("uploadtextfield").clear()
        driver.execute_script(
            "document.getElementsByClassName('wpcf7-form-control wpcf7-submit btn-cf-submit')[0].click();");
        driver.execute_script("document.getElementsByClassName('wpcf7-form-control wpcf7-submit btn-join-us btn-apply')[0].click();")
        if driver.find_element_by_id("cf-1").is_displayed():
            driver.find_element_by_id("cf-1").clear()
        clearForm()
        driver.find_element_by_id("cf-1").send_keys(i['firstName'] + " " + i['lastName'])
        if driver.find_element_by_id("cf-2").is_displayed():
            driver.find_element_by_id("cf-2").clear()
        driver.find_element_by_id("cf-2").send_keys(i['emailAddress'])
        if driver.find_element_by_id("cf-3").is_displayed():
            driver.find_element_by_id("cf-3").clear()
        driver.find_element_by_id("cf-3").send_keys(i['phoneNumber'])


        if driver.find_element_by_class_name("wpcf7-not-valid-tip").is_displayed():
            print("Error Message Verified")
        clearForm()
        uploadFile()

driver.close()
driver.quit()
