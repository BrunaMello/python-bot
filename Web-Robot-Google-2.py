from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


search = input('Type to search: ')

# initiate web drive
options = webdriver.ChromeOptions()
options.add_argument("--disable-logging")
options.add_argument("--log-level-3")

# internet access
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)

# go to web site
driver.get('https://www.google.com/')

# accept cookies
driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div').click()


# field to search
field = driver.find_element(By.XPATH, '//input[@aria-label="Search"]')
field.send_keys(search)
field.send_keys(Keys.ENTER)

#getting information about the search
results = driver.find_element(By.XPATH, '//*[@id="result-stats"]').text
print(results)





