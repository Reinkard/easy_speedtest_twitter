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
TWITTER_LOGIN = os.getenv("LOGIN")
TWITTER_PASSWORD = os.getenv("PASSWORD")
TWITTER_NICKNAME = os.getenv("NICKNAME")

class InternetSpeedTwitterBot():
    def __init__(self):
        self.chromedriver = chromedriver_autoinstaller.install()
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(), options=self.options)
        self.driver.maximize_window()
        self.get_internet_speed()
        time.sleep(80)
        self.download_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.upload_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.my_provider = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[4]/div/div/div[1]/div[3]/div[2]').text
        time.sleep(5)
        self.tweet_at_provider()
        
        
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/ru/")
        start_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start_button.click()
        try:
            close_svg = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a/svg')
            close_svg.click()
        except NoSuchElementException:
            pass
    
    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/i/flow/login')
        time.sleep(2)
        login_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        login_field.send_keys(TWITTER_LOGIN)
        login_field.send_keys(Keys.ENTER)

        time.sleep(2)
        try:
            nickname_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            nickname_field.send_keys(TWITTER_NICKNAME)
            nickname_field.send_keys(Keys.ENTER)
        except NoSuchElementException:
            pass
        
        time.sleep(2)
        password_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_field.send_keys(TWITTER_PASSWORD)
        password_field.send_keys(Keys.ENTER)

        try:
            close_window = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div/div/svg/g/path')
            close_window.click()
        except NoSuchElementException:
            pass

        time.sleep(10)
        entry_field = self.driver.find_element(By.XPATH, "//div[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div/div/div/div/div/div/div[2]/div/div/div/div")
        entry_field.click()
        entry_field.send_keys(f'Привіт! Провайдер {self.my_provider}, сьогоднішня швидкість: {self.download_speed}Mbps / {self.upload_speed}Mbps.\n\n#selenium #webdriver #learning')
        entry_field.send_keys(Keys.ENTER)
        send_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        send_button.click()
        self.driver.quit()