from selenium import webdriver
from pynput.keyboard import Key, Controller
import time
from account import username, psswd

keyboard = Controller()

class Tinderbot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://tinder.com")
        login_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        login_btn.click()
        time.sleep(1)
        more_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/button')
        more_btn.click()
        time.sleep(1)
        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_btn.click()
        time.sleep(1)
        #input email, password
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        email = self.driver.find_element_by_xpath('//*[@id="email"]')
        email.send_keys(username)
        password = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password.send_keys(psswd)
        time.sleep(1)
        login = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login.click()
        time.sleep(5)
        #deal with some pop_up windows
        self.driver.switch_to_window(base_window)
        allow_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_btn.click()
        time.sleep(1)
        enable_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span')
        enable_btn.click()
        time.sleep(10)
        later_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div[3]/button[2]/span')
        later_btn.click()

    def like(self):
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(base_window)
        #like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button')
        #like_btn.click()
        keyboard.press(Key.right)
        keyboard.release(Key.right)

    def auto_like(self):
        while True:
            time.sleep(2)
            self.like()

bot = Tinderbot()
bot.login()
time.sleep(2)
bot.auto_like()