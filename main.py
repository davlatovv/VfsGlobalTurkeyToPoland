import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service(executable_path=".chromedriver")

driver = webdriver.Chrome(options=options, service=service)
driver.get("https://visa.vfsglobal.com/tur/en/pol/login")

gmail = 'mat-input-0'
password = 'mat-input-1'
x = '//*[@id="onetrust-close-btn-container"]/button'
important = '//*[@id="mat-checkbox-1-input"]'
warning = '//*[@id="mat-checkbox-2"]'
sign_in = '//*[@class="ng-invalid ng-dirty ng-touched"]/button'
sign_in1 = '//form[@class="ng-invalid ng-dirty ng-touched"]/button'
recaptcha = '//*[@class="ng-star-inserted"]'

try:
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, x))).click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, gmail))).send_keys("zafardavlatov2003@gmail.com")
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, password))).send_keys('Davlatov3107!')
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, sign_in))).click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, important)))
    el = driver.find_element(By.XPATH, important)
    action = ActionChains(driver)
    action.click(on_element=el)
    action.perform()
    print('success')
    print('success')
    time.sleep(15)





    # driver.find_element(By.XPATH, '//*[@id="g-recaptcha-response"]').send_keys(captha_token)

    # driver.find_element(by=By.XPATH, value=create_account_button).click()
    # number_of_person = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME,  'broneering[isikute_arv]')))
    # number_of_person.send_keys('1')
    # number_of_person.send_keys(Keys.ENTER)
    # choose_city = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME,  'broneering[esindus_id]'))))
    # choose_city.select_by_value('3')
    # WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
    # driver.implicitly_wait(10)
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="submit"]'))).click()

except Exception as ex:
    print(ex)

