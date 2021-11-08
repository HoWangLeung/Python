import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import pandas as pd
import numpy as np
from datetime import date
PATH="/Users/howangleung/Desktop/Projects/Python/Selenium/AutoMessage/chromedriver"
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=chrome-data")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(PATH,options=options)

def main():
    path = "./Rubbish Disposal Schedule.xlsx"
    message = getFromExcel(path)
    sendMessage(message)

def getFromExcel(path):
    df = pd.read_excel(path,index_col=False)
    df["Date"] = df["Date"].dt.strftime("%d/%m/%y")
    today = date.today()
    today = today.strftime("%d/%m/%y")
    result_mark = df["Date"]==today
    pos = np.flatnonzero(result_mark)
    result = df.iloc[pos]
    message =f"Hi, *{result['Person'][0]}*, today is *{result['Date'][0]}*, this is your turn to take out the trash and to handle the recycling according to the schedule, thank you very much ! _This is an automated message, do not reply/quote._"
    return message



def sendMessage(message):
    url="https://web.whatsapp.com"
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    search = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@role='textbox']")))
    search.click()
    #title = 'FLAT 403! '
    title = 'MySelf'
    search.send_keys(title)
    search_result = wait.until(EC.visibility_of_element_located((By.XPATH,f"//*[@title='{title}']")))
    search_result.click()
    textBox = wait.until(EC.visibility_of_element_located((By.XPATH,f"//*[@role='textbox' and @data-tab='9']")))
    print(message)
    textBox.send_keys(message)
    textBox.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.quit()

if __name__ == "__main__":
    main()