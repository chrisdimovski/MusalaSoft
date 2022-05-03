from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PATH = r"C:\Users\Kristijan\Desktop\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.implicitly_wait(1)
BaseURL = "https://www.musala.com/"
CompanyURL = "https://www.musala.com/company/"
FaceBookURL = "https://www.facebook.com/MusalaSoft?fref=ts"
driver.get(BaseURL)

driver.execute_script("document.getElementsByClassName('main-link')[0].click();")

currentURL = driver.current_url
if CompanyURL == currentURL:
    print("'Company' page URL is correct")

if (driver.find_element_by_xpath("//div[@class='cm-content']").is_displayed()):
    print("'Leadership' section present")

driver.find_element(By.XPATH, "//a[@href='https://www.facebook.com/MusalaSoft?fref=ts']").click()
print("FaceBook button selected")

alltabs = driver.window_handles
print("Changing tab")

for tab in alltabs:
    driver.switch_to.window(tab)
    if(driver.current_url=="//a[@href='https://www.facebook.com/MusalaSoft?fref=ts']"):
        driver.find_element_by_xpath("//a[@aria-label='aovydwv3 j83agx80 wkznzc2l dlu2gh78']").click()


    print("Current URL is: " + driver.current_url)

time.sleep(5)

driver.find_element_by_xpath("//div[@class='_6taw']").click()

if (driver.find_element_by_xpath("//div[@class='_6taw']").is_displayed()):
    print("MusalaSoft profile picture is present")


driver.close()
driver.quit()

