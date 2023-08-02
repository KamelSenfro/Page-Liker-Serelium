from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

# set up the webdriver
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login")

# enter email and password
email = driver.find_element(By.NAME, "session_key")
password = driver.find_element(By.NAME, "session_password")
email.send_keys("Email Address")     # enter your email address
password.send_keys("Password")       # enter your password
password.send_keys(Keys.RETURN)

# wait for the page to load 7 seconds cuz my internet is slow
time.sleep(7)

# search for "Page name"
search_bar = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
search_bar.send_keys("page name") # enter the name of the page you want to like its posts
search_bar.send_keys(Keys.RETURN)
# navigate to the URL
driver.get("page URL") # enter the URL of the page you want to like its posts

"""ignore this part
# paste the URL in the Search bar
address_bar = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
address_bar.clear()
address_bar.send_keys("")
address_bar.send_keys(Keys.RETURN)"""



# go to the company page
"""company_page = driver.find_element(By.XPATH, "//span[text()='name']")
company_page.click()"""

# scroll down to load all the posts
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# locate all the like buttons and click them
like_buttons = driver.find_elements(By.XPATH, "//button[@aria-label='post the aria-label of the button you want to click']")
for button in like_buttons:
    try:
        driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()
        time.sleep(2)
    except:
        pass

# locate all the like buttons and click them
"""like_buttons = driver.find_elements(By.XPATH, "//button[@aria-label='Like']")
for button in like_buttons:
    try:
        button.click()
        time.sleep(2)
    except:
        pass"""
