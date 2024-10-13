from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# driver configuration
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
    driver.get("https://www.timeanddate.com/worldclock/")
    return driver

# Cleans some text
def clean_text(text):
    """Extract only the dynamic text only"""

# The call of driver function
def main():
    driver = get_driver()
    # time.sleep(2) ## Sleep for 2 seconds
    element = driver.find_element("xpath", "/html/body/div[5]/section[1]/div/div[1]/div[1]/div/div[1]/span/span")
    return element.text  # Return the text of the element

print(main())

