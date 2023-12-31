from pages.demoqa import DemoQa
import pytest
from pages.elements_page import ElementsPage
from components.components import WebElement
from conftest import browser
from pages.alerts import Alert
from pages.browser_tab import BrowserTab
import time

def test_seo_page(browser):
    page_check1 = DemoQa(browser)
    page_check1.visit()
    return page_check1.get_title() == 'DEMOQA'
@pytest.mark.parametrize("pages", [Alert, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'