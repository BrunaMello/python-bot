from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# internet access
driver = webdriver.Chrome('chromedriver/chromedriver')
driver.get('https://www.registro.br')

search = driver.find_element(By.ID, 'is-avail-field')
search.clear()
search.send_keys('brunacrespomello')
search.send_keys(Keys.RETURN)


time.sleep(8000)
driver.close()



