from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from components.components import WebElement
from conftest import browser
from pages.text_box import TextBox
import time

def test_flex_menu(browser):
    page_check1 = ElementsPage(browser)
    page_check1.visit()
    assert page_check1.block_menu.check_css('flex', '0 0 25%')
    assert page_check1.block_menu.check_css('max-width', '25%')
    browser.set_window_size(width=360, height=740)
    time.sleep(2)
    assert page_check1.block_menu.check_css('flex', '0 0 100%')
    assert page_check1.block_menu.check_css('max-width', '100%')
    browser.set_window_size(width=1000, height=1000)