# selenium 3
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://google.com/')

''' 
driver.get('https://www.expedia.co.in/')
driver.set_window_size(3000, 1000)
driver.find_element_by_class_name('uitk-fake-input').click()
inp = driver.find_element_by_class_name('uitk-field-input')
inp.send_keys('India')
driver.find_element_by_class_name('uitk-button').click()
https://www.geeksforgeeks.org/interacting-with-webpage-selenium-python/?ref=lbp

'''
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.google.com/')
driver.maximize_window()
input = driver.find_element_by_id('APjFqb')
input.send_keys('NASA')
input.send_keys(Keys.ENTER)
# input = driver.find_element_by_class_name('hds-search-input')
# input.send_keys('Hello NASA')
# input.send_keys(Keys.ENTER)
''' 
driver.get(url): Opens the specified URL in the browser.

driver.find_element(by=, value=): Finds the first element matching the specified selector strategy (by) and value.

element.send_keys(*value): Simulates typing into the element.

element.click(): Clicks the element.

element.clear(): Clears the text from the element.

element.text: Returns the text of the element.

element.get_attribute(attribute_name): Returns the value of the specified attribute of the element.

driver.switch_to.frame(frame_reference): Switches the focus to the specified frame.

driver.switch_to.default_content(): Switches the focus back to the default content (out of any frames).

driver.switch_to.window(window_name): Switches the focus to the specified window.

driver.window_handles: Returns a list of handles for all open windows.

'''