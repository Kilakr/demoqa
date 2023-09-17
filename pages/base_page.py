from selenium.webdriver.common.by import By
import time


class BasePage:
    def __init__(self, driver,base_url):
        self.driver = driver
        self.base_url = base_url

    def visit(self):

        return self.driver.get(self.base_url)
    def equal_url(self):
        return self.get_url() == self.base_url

    #def find_element(self, locator):
        #return self.driver.find_element(By.CSS_SELECTOR, locator)
    def get_url(self):
        return self.driver.current_url