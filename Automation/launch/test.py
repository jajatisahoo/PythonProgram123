
import unittest
from selenium.webdriver import chrome

from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https:\\google.com")

driver.maximize_window()
search_Field=driver.find_element(By.XPATH,"//input[@id='lst-ib']")
search_Field.send_keys("testing ideas")
#search_Field.submit();
driver.execute_script("document.getElementById('lst-ib').click();");
sText=driver.execute_script("return document.title;")

print (sText)
if __name__ == "__main__":
    unittest.main()