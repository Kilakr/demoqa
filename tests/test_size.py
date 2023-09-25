from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from components.components import WebElement
from conftest import browser
import time

def test_size_page(browser):
    page_check1 = DemoQa(browser)
    page_check1.visit()
    browser.set_window_size(width=1000, height=300)
    time.sleep(2)
    browser.set_window_size(width=1000, height=1000)