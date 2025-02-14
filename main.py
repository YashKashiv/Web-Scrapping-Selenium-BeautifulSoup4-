# https://selenium-python.readthedocs.io/getting-started.html

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
file = 0
for i in range (1, 20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=AF3XJAA5C7OS&sprefix=lap%2Caps%2C295&ref=nb_sb_ss_pltr-sample-20_1_3")
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} items found")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"Data/{query}_{file}.html", "w",encoding="utf-8") as f:
            f.write(d)
            file +=1
    time.sleep(2)
driver.close()