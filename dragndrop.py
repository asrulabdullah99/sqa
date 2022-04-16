#import webdriver
from selenium import webdriver

# import action chains
from selenium.webdriver.common.action_chains import ActionChains

# create webdriver object
driver = webdriver.Chrome()

# get w3schools.com
driver.get('https://www.w3schools.com/html/html5_draganddrop.asp')

# get element
element_sumber = driver.find_element_by_css_selector('div#div1')

element_tujuan = driver.find_element_by_css_selector('div#div2')

# create action chain object
action = ActionChains(driver)

# drag n drop the item
action.drag_and_drop(element_sumber, element_tujuan)

# perform the operation
action.perform()
