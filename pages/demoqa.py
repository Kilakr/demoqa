from pages.base_page import BasePage
from components.components import WebElement


class DemoQa(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        self.icon = WebElement(driver,'#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        super().__init__(driver, self.base_url)
    #def exist_icon(self):
        #try:
            #self.icon.find_element()
        #except NoSuchElementException:
            #return False
        #return True
