from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from components.components import WebElement
from conftest import browser
from pages.webtables import WebTables
import time

def test_webtables(browser):
    page_check1 = WebTables(browser)
    page_check1.visit()
    browser.set_window_size(width=1000, height=1000)
    assert page_check1.table_elements.get_text()!=''
    assert not page_check1.no_rows.exist()
    while page_check1.delete_button.exist():
        page_check1.delete_button.click()
        time.sleep(1)
    assert page_check1.no_rows.get_text() == 'No rows found'
