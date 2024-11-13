from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")


for i in range(5):
    add_btn = driver.find_element(By.XPATH, '//button[text()="Add Element"]').click()
sleep(5)

del_btns = driver.find_elements(By.XPATH, '//button[text()="Delete"]')
print("Размер списка кнопок Delete:", len(del_btns))

sleep(5)

driver.quit()
