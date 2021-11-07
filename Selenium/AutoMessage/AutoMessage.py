import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


# variable to store the name of the contact
contact = "Wahda"
#variable to store message
message = "hello Allah"
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=chrome-data")
options.add_experimental_option("detach", True)
# url = "https://web.whatsapp.com"
url="https://web.whatsapp.com"
PATH="/Users/howangleung/Desktop/Projects/Python/Selenium/AutoMessage/chromedriver"
driver = webdriver.Chrome(PATH,options=options)
wait = WebDriverWait(driver, 10)
 
driver.get(url)
print("Scan QR Code and press Enter")
search = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@role='textbox']")))
search.click()
#time.sleep(3)
#title = 'FLAT 403! '
title = 'MySelf'
search.send_keys(title)
search_result = wait.until(EC.visibility_of_element_located((By.XPATH,f"//*[@title='{title}']")))
search_result.click()
textBox = wait.until(EC.visibility_of_element_located((By.XPATH,f"//*[@role='textbox' and @data-tab='9']")))
textBox.send_keys("Hi")
textBox.send_keys(Keys.ENTER)

#"//*[@role='textbox']"