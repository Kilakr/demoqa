from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from components.components import WebElement
from conftest import browser
import time

def test_seo_page(browser):
    page_check1 = DemoQa(browser)
    page_check1.visit()
    return page_check1.get_title() == 'DEMOQA'