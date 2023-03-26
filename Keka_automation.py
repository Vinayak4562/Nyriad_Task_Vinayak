from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\vinay\\Dropbox\\PC\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=service_obj, options=options)
driver.get("https://msys.keka.com/")

driver.maximize_window()
driver.implicitly_wait(35)

driver.find_element(By.CLASS_NAME, "ps-2").click()

driver.find_element(By.ID, "identifierId").send_keys("vhavannavar@msystechnologies.com")

driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button/span").click()

driver.find_element(By.CLASS_NAME, "whsOnd zHQkBf").send_keys("123@vinayakH")

driver.find_element(By.XPATH,'//*[@id="passwordNext"]/div').click()

# Still i am Working on it