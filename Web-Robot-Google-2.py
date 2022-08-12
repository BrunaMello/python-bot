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

# getting information about the search
results = driver.find_element(By.XPATH, '//*[@id="result-stats"]').text
print(results)

# getting number of pages in the result
result_numbers = int(results.split("About ")[1].split(" results")[0].replace(',', ''))
max_page = result_numbers/10

print('Page number: %s pages' % max_page)

# navigate between pages of results
url_page = driver.find_element(By.XPATH, '//*[@aria-label="Page 2"]').get_attribute('href')

current_page = 0
start = 10
result_list = []

while current_page <= 10:
    if not current_page == 0:
        url_page = url_page.replace("start=%s" % start, "start=%s" % (start+10))
        start = start + 10
        driver.get(url_page)
    current_page = current_page + 1


    # getting link pages
    divs = driver.find_elements(By.XPATH, "//div[@class='g']")
    for div in divs:
        name = div.find_element(By.TAG_NAME, "h3")
        link = div.find_element(By.TAG_NAME, "a")
        result = "%s; %s" % (name.text, link.get_attribute("href"))
        # add result to txt
        result_list.append(result)

with open("google-robot-result.txt", "w") as file:
    for result in result_list:
        file.write("%s\n" % result)
    file.close()

print("%s found results from Google and successfully saved on txt file" % len(result_list))








