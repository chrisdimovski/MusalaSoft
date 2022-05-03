from selenium import webdriver
import json

PATH = r"C:\Users\Kristijan\Desktop\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.implicitly_wait(1)
BaseURL = "https://www.musala.com/"
driver.get(BaseURL)

name_field = driver.find_element_by_id("cf-1")
email_field = driver.find_element_by_id("cf-2")
phone_field = driver.find_element_by_id("cf-3")
subject_field = driver.find_element_by_id("cf-4")
message_field = driver.find_element_by_id("cf-5")
form_submit = driver.find_element_by_xpath("//input[@class='wpcf7-form-control wpcf7-submit btn-cf-submit']")
invalid_email_text = 'The e-mail address entered is invalid.'

# Opening JSON file
with open('./data/test1data.json') as json_file:
    data = json.load(json_file)

    for i in data['users']:
        driver.execute_script("document.getElementsByClassName('contact-label btn btn-1b')[0].click();")
        name_field.clear()
        name_field.send_keys(i['firstName'] + " " + i['lastName'])
        email_field.clear()
        email_field.send_keys(i['emailAddress'])
        phone_field.clear()
        phone_field.send_keys(i['phoneNumber'])
        form_submit.click()
        subject_field.send_keys(i['subject'])
        form_submit.click()
        message_field.send_keys(i['message'])
        form_submit.click()
        invalid_email = driver.find_element_by_xpath("//span[@class='wpcf7-not-valid-tip']")
        if invalid_email.is_displayed() and invalid_email.text == invalid_email_text:
            print("Error Message '" + invalid_email.text + "'")


driver.close()
driver.quit()
