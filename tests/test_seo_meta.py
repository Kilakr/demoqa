from pages.demoqa import DemoQa
import pytest
from pages.elements_page import ElementsPage
from components.components import WebElement
from conftest import browser
from pages.alerts import Alert
from pages.browser_tab import BrowserTab
import time
@pytest.mark.parametrize("pages", [Alert, DemoQa, BrowserTab])
def test_seo_meta(browser,pages):
    page = pages(browser)
    page.visit()
    assert page.meta.exist()
    assert page.meta.get_dom_attribute('name') == 'viewport'
    assert page.meta.get_dom_attribute('content') == 'width=device-width,initial-scale=1'