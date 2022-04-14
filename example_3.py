from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('https://www.google.com/')
assert 'Google' in browser.title

elem = browser.find_element(By.NAME, 'q')
elem.send_keys('unmuhpnk'+Keys.RETURN)

browser.quit()
