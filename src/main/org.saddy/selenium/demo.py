from selenium import webdriver;

driver = webdriver.Firefox()
driver.get('https://qa.itinstruct.com')
title = driver.title
print('Title of the page: ' + title)

driver.close()