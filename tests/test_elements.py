from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from components.components import WebElement
from conftest import browser
from pages.heroku import HerokuPage
import time

def test_elements_page(browser):
    page_check1 = HerokuPage(browser)
    page_check1.visit()
    assert page_check1.btns_first_menu.check_count_elements(9)