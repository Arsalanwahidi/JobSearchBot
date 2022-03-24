from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
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
        self.driver.implicitly_wait(2)

        #Keyword and location search
        search_keyword = self.driver.find_element(By.XPATH, "//input[starts-with(@id, 'jobs-search-box-keyword')]")
        search_keyword.clear()
        search_keyword.send_keys(self.keywords)

        self.driver.implicitly_wait(5)
        search_location = self.driver.find_element(By.XPATH, "//input[starts-with(@id, 'jobs-search-box-location-id')]")
        search_location.clear()
        search_location.send_keys(self.location)
        search_keyword.send_keys(Keys.RETURN)
        
        # search_link = self.driver.find_element(By.XPATH, "//button[starts-with(@class, 'jobs-search-box__submit-button')]")
        # search_link.click()
        
        # second_search_link = self.driver.find_element(By.XPATH, "//a[starts-with(@class, 'app-aware-link')]")
        # second_search_link.click()
    
    def filter(self):
        """Filter the job"""
        
        self.driver.implicitly_wait(2)
        all_filter_button = self.driver.find_element(By.XPATH, "//button[starts-with(@class, 'artdeco-pill artdeco-pill--slate artdeco-pill--choice artdeco-pill--2 search-reusables__filter-pill-button')]")
        all_filter_button.click()
        self.driver.implicitly_wait(2)
        mid_senior_level_button = self.driver.find_element(By.XPATH, "//label[@for='advanced-filter-experience-4']")
        mid_senior_level_button.click()
        self.driver.implicitly_wait(1)
        show_result_button = self.driver.find_element(By.XPATH, "//button[starts-with(@class, 'reusable-search-filters-buttons')]")
        show_result_button.click()

        self.driver.implicitly_wait(5)


if __name__ == '__main__':
    
    with open('config.json') as file:
        data = json.load(file)
    bot = EasyApplyLinkedin(data)
    bot.login_linkedin()
    bot.driver.implicitly_wait(2)
    bot.job_search()
    bot.driver.implicitly_wait(2)
    bot.filter()