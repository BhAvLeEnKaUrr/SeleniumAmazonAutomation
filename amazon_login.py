from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
#chrome
driver=webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32 (1)\C:\drivers\chromedriver_win32 (1)\chromedriver.exe")
#amazon site
driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
print(driver.title)#returns the title of the page
print(driver.current_url)#returns url of the page
#amazon sign in
driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]").click()
time.sleep(10)   #sleep mode
print(driver.title)
#enter password
driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input").click()
time.sleep(25)
print(driver.title)
# signing in7
driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div/form/div/div[2]/span/span/input").click()
time.sleep(25)
print(driver.title)
#searching
searchBox=driver.find_element("xpath","/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
searchBox.click()
searchBox.send_keys('microphone')#change ur search here
time.sleep(10)
print(driver.title)
#cart
inCart=driver.find_element("xpath","/html/body/div[1]/header/div/div[1]/div[3]/div/a[5]/div[1]/span[2]")
inCart.click()
time.sleep(5)
print(driver.title)
#language
driver.find_element("xpath","/html/body/div[1]/header/div/div[1]/div[3]/div/a[1]/span/span[2]/span[1]").click()
time.sleep(5)
print(driver.title)
#amazon pay
driver.find_element("xpath","/html/body/div[1]/header/div/div[4]/div[2]/div[2]/div/a[3]").click()
time.sleep(5)
print(driver.title)
#closing the tab
driver.close()
