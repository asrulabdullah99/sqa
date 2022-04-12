import time
from selenium import webdriver  # import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()  # choose browser
driver.maximize_window()  # maximize windows
driver.get("https://www.bing.com/")  # navigate given URL
# driver.find_element_by_name("q").send_keys('unmuhpnk')
driver.find_element(By.NAME, "q").send_keys('unmuhpnk')
time.sleep(4)
# driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
driver.find_element(By.ID, "search_icon").send_keys(Keys.ENTER)
time.sleep(3)

driver.close()
print('test case berhasil dengan sempurna')
