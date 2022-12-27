from keys.xpath_keys import *
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent


def get_chromedriver(use_proxy=False, user_agent=None):
    chrome_options = webdriver.ChromeOptions()
    if use_proxy:
        plugin_file = ''

    if user_agent:
        chrome_options.add_argument(f'--user-agent={user_agent}')

    # chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path=".chromedriver")
    driver = webdriver.Chrome(options=chrome_options, service=service)
    return driver

def login():
    try:
        user_agent = UserAgent()
        user_agent.update()
        driver = get_chromedriver()
        driver.maximize_window()
        driver.get("https://visa.vfsglobal.com/tur/en/pol/login")
        # driver.get('https://pr-cy.ru/browser-details/')
        # driver.delete_all_cookies()
        # sleep(15)
        WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, x))).click()
        WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.ID, gmail))).send_keys("zafardavlatov2003@gmail.com")
        WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.ID, password))).send_keys('Davlatov3107!')
        WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, sign_in))).click()
        WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, important))).click()
        element = driver.find_element(By.XPATH, important)
        driver.execute_script("arguments[0].click();", element)
        # action = ActionChains(driver)
        # action.click(on_element=el)
        # action.perform()
        driver.delete_all_cookies()
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    login()

