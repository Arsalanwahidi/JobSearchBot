from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import json

class EasyApplyLinkedin:

    def __init__(self, data):
        """Parameter Initialization"""

        self.email = data['email']
        self.password = data['password']
        self.keywords = data['keywords']
        self.location = data['location']
        s = Service(data['driver_path'])
        self.driver = webdriver.Chrome(service=s)
    
    def login_linkedin(self):
        """Login Function for linkedIn"""

        #Login to this url
        self.driver.get('https://www.linkedin.com/login')

        #Email and Password of your user

        login_email = self.driver.find_element(By.NAME, 'session_key')
        login_email.clear()
        login_email.send_keys(self.email)

        login_password = self.driver.find_element(By.NAME, 'session_password')
        login_password.clear()
        login_password.send_keys(self.password)
        login_password.send_keys(Keys.RETURN)
    
    def job_search(self):
        """Search the job function"""
        #Job Section 
        job_link = self.driver.find_element(By.LINK_TEXT, 'Jobs')
        job_link.click()
        time.sleep(3)

        #Keyword and location search
        search_keyword = self.driver.find_element(By.XPATH, "//input[starts-with(@id, 'jobs-search-box-keyword')]")
        search_keyword.clear()
        search_keyword.send_keys(self.keywords)

        search_location = self.driver.find_element(By.XPATH, "//input[starts-with(@id, 'jobs-search-box-location')]")
        search_location.clear()
        search_location.send_keys(self.location)
        search_location.send_keys(Keys.RETURN)
        
        
        search_link = self.driver.find_element(By.XPATH, "//button[starts-with(@class, 'jobs-search-box__submit-button')]")
        search_link.click()
    
    def filter(self):
        """Filter the job"""
        time.sleep(5)
        all_filter_button = self.driver.find_element(By.XPATH, "//button[starts-with(@aria-label, 'Show all filters')]")
        all_filter_button.click()
        time.sleep(2)
        mid_senior_level_button = self.driver.find_element(By.XPATH, "//label[@for='advanced-filter-experience-5']")
        mid_senior_level_button.click()
        time.sleep(2)
        show_result_button = self.driver.find_element(By.XPATH, "//li-icon[@class='artdeco-button__text']")
        show_result_button.click()
        # time.sleep(2)
        # close_button = self.driver.find_element(By.XPATH, "//li-icon[@class='artdeco-button__icon']")
        # close_button.click()




if __name__ == '__main__':
    
    with open('config.json') as file:
        data = json.load(file)
    bot = EasyApplyLinkedin(data)
    bot.login_linkedin()
    time.sleep(4)
    bot.job_search()
    time.sleep(2)
    bot.filter()