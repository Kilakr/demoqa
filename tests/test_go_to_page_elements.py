from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from conftest import browser

def test_check_elements(browser):
    page_check = DemoQa(browser)
    page_check1 = ElementsPage(browser)

    page_check.visit()
    assert page_check.equal_url()
    page_check.btn_elements.click()
    assert page_check1.equal_url()
