#import webdriver
from selenium import webdriver

# import action chains
from selenium.webdriver.common.action_chains import ActionChains

# create webdriver object
driver = webdriver.Chrome()

# get w3schools.com
driver.get('https://www.w3schools.com/')

# get element
element = driver.find_element_by_link_text('Learn HTML')

# create action chain object
action = ActionChains(driver)

# click the item
action.click(on_element=element)

# perform
action.perform()
