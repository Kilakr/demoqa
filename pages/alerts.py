from pages.base_page import BasePage
from components.components import WebElement

class Alert(BasePage):
    def __init__(self,driver):
        self.base_url = 'https://demoqa.com/alerts'
        self.alert1 = WebElement(driver, '#alertButton')
        self.alert2 = WebElement(driver, '#confirmButton')
        self.alert3 = WebElement(driver, '#promtButton')
        self.confresult = WebElement(driver, '#confirmResult')
        self.promptresult = WebElement(driver, '#promptResult')
        super().__init__(driver, self.base_url)
