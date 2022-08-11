import time

import xlrd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# welcome

print('Robot initiated')

# open and reading Excel file
workbook = xlrd.open_workbook('Files/sites.xls')
sheet = workbook.sheet_by_name('Plan1')
rows = sheet.nrows
cols = sheet.ncols


# initiate web drive
options = webdriver.ChromeOptions()
options.add_argument("--disable-logging")
options.add_argument("--log-level-3")

# internet access
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)
driver.get('https://www.registro.br')


for curr_row in range(0, rows):
    # initiate reading
    x = sheet.cell_value(curr_row, 0)
    # search local to input
    search = driver.find_element(By.ID, 'is-avail-field')
    time.sleep(1)
    search.clear()
    time.sleep(1)
    search.send_keys(x)
    time.sleep(1)
    search.send_keys(Keys.RETURN)
    time.sleep(1)
    # getting bolder
    driver.find_element(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong')
    time.sleep(1)
    print('Domain: %s %s' % (x, driver.find_element(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong')))


driver.close()
