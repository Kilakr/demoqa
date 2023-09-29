from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from components.components import WebElement
from conftest import browser
from pages.text_box import TextBox

def test_placeholder(browser):
    page_check1 = TextBox(browser)
    page_check1.visit()
    assert page_check1.full_name.get_dom_attribute('placeholder') == 'Full Name'