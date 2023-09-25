from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from components.components import WebElement
from conftest import browser
import time
def test_visible_btn_sidebar(browser):
    page_check1 = ElementsPage(browser)
    page_check1.visit()
    #page_check1.btn_sidebar_first.click()
    # time.sleep(3)
    #assert page_check1.btn_sidebar_first_textbox.exist()
    assert page_check1.btn_sidebar_first_textbox.visible()
def test_not_visible_btn_sidebar(browser):
    page_check2 = ElementsPage(browser)
    page_check2.visit()
    assert page_check2.btn_sidebar_first_checkbox.visible()
    page_check2.btn_sidebar_first.click()
    time.sleep(2)
    assert not page_check2.btn_sidebar_first_checkbox.visible()

