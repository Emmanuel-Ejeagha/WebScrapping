# from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    config = webdriver.ChromeOptions()
    config.add_argument("disable-infobars")
    config.add_argument('start-maximized')
    config.add_argument('disable-dev-shm-usage')
    config.add_argument("no-sandbox")
    config.add_experimental_option("excludeSwitches", ["enable-automation"])
    config.add_argument("disable-blink-features=AutomationControlled")
    
    # Use Service class to manage the ChromeDriver executable
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=config)
    driver.get("https://dixcoverhub.com.ng/")
    return driver

def main():
    driver = get_driver()
    element = driver.find_element("xpath", "/html/body/div[1]/footer/div/div[1]/div[1]/div/p[2]")
    return element.text  # Return the text of the element

print(main())


# def get_driver():
#     # Set options to make browsing easier
#     config = webdriver.ChromeOptions()
#     config.add_argument("disable-infobars")
#     config.add_argument('start-maximized')
#     config.add_argument('disable-dev-shm-usage')
#     config.add_argument("no-sandbox")
#     config.add_experimental_option("excludeSwitches", ["enable-automation"])
#     config.add_argument("disable-blink-features=AutomationControlled")
    
#     driver = webdriver.Chrome(options=config)
#     driver.get("https://dixcoverhub.com.ng/")
#     return driver

# def main():
#     driver = get_driver()
#     element = driver.find_element_by_xpath("/html/body/div[1]/footer/div/div[1]/div[1]/div/p[2]")
#     return element

# print(main())