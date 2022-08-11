import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# welcome

print('Robot initiated')

# initiate web drive
options = webdriver.ChromeOptions()
options.add_argument("--disable-logging")
options.add_argument("--log-level-3")

# internet access
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)
driver.get('https://www.registro.br')

domains = ['brunacrespomello.com', 'hotmart.com', 'uol.com', 'globo.com']

for domain in domains:
    # search local to input
    search = driver.find_element(By.ID, 'is-avail-field')
    search.clear()
    search.send_keys(domain)
    search.send_keys(Keys.RETURN)
    time.sleep(5)
    # getting bolder
    driver.find_element(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong')
    print('Domain: %s %s' % (domains, driver.find_element(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong')))


driver.close()
