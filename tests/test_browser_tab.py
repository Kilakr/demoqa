from components.components import WebElement
from conftest import browser
from pages.browser_tab import BrowserTab
import time

def test_browser_tab(browser):
    page_check1 = BrowserTab(browser)
    page_check1.visit()
    assert len(page_check1.driver.window_handles) == 1
    page_check1.new_tab.click()
    time.sleep(2)
    assert len(page_check1.driver.window_handles) == 2
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)