#import webdriver
from selenium import webdriver

# import action chains
from selenium.webdriver.common.action_chains import ActionChains

# create webdriver object
driver = webdriver.Chrome()

# get w3schools.com
driver.get('https://www.w3schools.com/')

# get element by link_text
#element = driver.find_element_by_link_text('Learn HTML')

# get element by name
element = driver.find_element_by_css_selector('h1.learntocodeh1')


# # create action chain object
# action = ActionChains(driver)

# # double click the item
# action.click(on_element=element)

# # perform the operation
# action.perform()

# print complete element
print(element)
