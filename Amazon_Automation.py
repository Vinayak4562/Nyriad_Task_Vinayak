from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# To stay in web browser
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service("C:\\Users\\vinay\\Dropbox\\PC\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj, options=options)

driver.implicitly_wait(20)              # it will wait for 20 sec
driver.maximize_window()                # it will maximise the window
driver.get("https://www.amazon.in/")    # getting the Amazon URL
driver.maximize_window()                # it will maximise the window
driver.implicitly_wait(15)              # it will wait for 20 sec

driver.find_element(By.CLASS_NAME,"nav-line-1-container").click()           # Clicking for login button
driver.find_element(By.ID, "ap_email").send_keys("vinz223665@gmail.com")    # providing IP Credential Username
driver.find_element(By.ID, "continue").click()                              # clicking continue button
driver.find_element(By.NAME, "password").send_keys("vinayak@123")           # providing IP Credential password
driver.find_element(By.ID, "signInSubmit").click()                          # clicking Submit button
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Dell laptop")  # sending key for search
driver.find_element(By.ID, "nav-search-submit-button").click()
driver.find_element(By.CLASS_NAME, "s-image").click()
list_windows = driver.window_handles
driver.switch_to.window(list_windows[1])
driver.find_element(By.ID, "add-to-cart-button").click()
driver.find_element(By.ID, "attach-view-cart-button-form").click()
driver.find_element(By.ID, "desktop-ptc-button-celWidget").click()
driver.find_element(By.XPATH, '//*[@id="shipToThisAddressButton"]/span').click()


# The "driver" object in this line of code refers to the WebDriver instance that is controlling the browser session.
# The "window_handles" method is a built-in method of the WebDriver class in Selenium,
# and it returns a list of all the window handles for the current browser session.
#
# The resulting "list_windows" variable will contain a list of strings,
# where each string represents a window handle for the current browser session.
# This list can be used to switch between different windows or tabs during the Selenium test script.