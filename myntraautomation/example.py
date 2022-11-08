from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.google.com")
# driver.find_element_by_xpath('//*[@id="input"]').send_keys("lagnesh meaning")
# driver.maximize_window()
driver=webdriver.Firefox(executable_path='/home/lagnesh/Downloads/geckodriver-v0.31.0-linux64/geckodriver')
driver.get("https://www.javatpoint.com")
# driver.find_element_by_xpath('//*[@id="input"]').send_keys("lagnesh meaning")
driver.close