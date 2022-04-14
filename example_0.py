from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://unmuhpnk.ac.id/beranda")
assert "UM Pontianak" in driver.title
elem = driver.find_element_by_name("um pontianak")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
