from pages.base_page import BasePage
from components.components import WebElement

class HerokuPageAdd(BasePage):
    def __init__(self, driver):
        self.base_url = 'http://the-internet.herokuapp.com/add_remove_elements/'
        self.add_elements = WebElement(driver, '#content > div > button')
        self.delete_element = WebElement(driver, '#elements > button')
        super().__init__(driver, self.base_url)