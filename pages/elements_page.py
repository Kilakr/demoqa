from pages.base_page import BasePage
from components.components import WebElement

class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        self.btn_sidebar_first = WebElement(driver, 'div:nth-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElement(driver, 'div:nth-child(1) > div > ul > #item-0 > span')

        super().__init__(driver, self.base_url)
        self.text_elements = WebElement(driver,'#app > div > div > div.pattern-backgound.playgound-header > div')