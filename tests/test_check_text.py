from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from components.components import WebElement
from conftest import browser

def test_page_elements(browser):
    page_check1 = DemoQa(browser)
    page_check2 = ElementsPage(browser)
    page_check2.visit()
    assert page_check2.text_elements.get_text() == 'Elements'
    assert page_check1.icon.exist()
    assert page_check2.btn_sidebar_first.exist()
    assert page_check2.btn_sidebar_first_textbox.exist()