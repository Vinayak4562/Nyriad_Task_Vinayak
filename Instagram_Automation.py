from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# To stay in web browser
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service("C:\\Users\\vinay\\Dropbox\\PC\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj, options=options)

driver.implicitly_wait(20)  # it will wait for 20 sec
driver.maximize_window()   # it will maximise the window

driver.get("https://www.instagram.com/")    # by using this link web driver will hit the link

driver.find_element(By.NAME, "username").send_keys("vinz223665")    # providing her login credentials username
driver.find_element(By.NAME, "password").send_keys("vinayak@123")   # providing her login credentials password
driver.find_element(By.XPATH, "//div[text()='Log in']").click()     # Hitting the Login button

driver.find_element(By.XPATH, "(//*[name()='svg'][@aria-label='Search'])[1]").click()   # clicking the search option
driver.find_element(By.CLASS_NAME, "_aauy").send_keys("pramod4562")  # passing here friend name
driver.find_element(By.XPATH, "(//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk "
                              "x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1cy8zhl x1oa3qoh "
                              "x1nhvcw1'])[1]").click() # Clicking on friend profile

# driver.find_element(By.XPATH, "(//ul[@class='_abpo'])[1]").click()  # Clicking on he's post
# driver.find_element(By.CLASS_NAME, "x1lliihq x1n2onr6").click()     # hitting the like button

driver.find_element(By.XPATH, "(//*[name()='line'][@fill='none'])[8]").click()  # selecting Logout option
driver.find_element(By.XPATH, "(//span[normalize-space()='Log out'])[1]").click()  # Clicking the Logout Button
