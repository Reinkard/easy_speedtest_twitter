from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from dotenv import load_dotenv
import time
import os

load_dotenv()
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
nickname = os.getenv("NICKNAME")

chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(), options=options)

driver.maximize_window()
driver.get("https://www.speedtest.net/ru/")

start_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
start_button.click()
time.sleep(80)

try:
    close_svg = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a/svg')
    close_svg.click()
except NoSuchElementException:
    pass
time.sleep(5)
download_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
upload_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

driver.get('https://twitter.com/i/flow/login')
time.sleep(2)
login_field = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
login_field.send_keys(login)
login_field.send_keys(Keys.ENTER)
time.sleep(2)
nickname_field = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
nickname_field.send_keys(nickname)
nickname_field.send_keys(Keys.ENTER)
time.sleep(2)
password_field = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)

try:
    close_window = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div/div/svg/g/path')
    close_window.click()
except NoSuchElementException:
    pass

time.sleep(10)
entry_field = driver.find_element(By.XPATH, "//div[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div/div/div/div/div/div/div[2]/div/div/div/div")
entry_field.click()
entry_field.send_keys(f'Привіт! Провайдер soho.net, сьогоднішня швидкість: {download_speed}Mbps / {upload_speed}Mbps.\n\n#selenium #webdriver #learning')
entry_field.send_keys(Keys.ENTER)
send_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
send_button.click()

driver.quit()
