from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from components.components import WebElement
from conftest import browser
import time

def test_navigation(browser):
    page_check1 = DemoQa(browser)
    page_check2 = ElementsPage(browser)
    page_check1.visit()
    page_check1.btn_elements.click()
    page_check2.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    assert page_check2.equal_url()
