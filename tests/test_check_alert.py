from components.components import WebElement
from conftest import browser
from pages.alerts import Alert
import time

def test_alert_timer(browser):
    page_check1 = Alert(browser)
    page_check1.visit()
    assert page_check1.alert4.exist()
    page_check1.alert4.click()
    time.sleep(6)
    assert page_check1.alert()
    page_check1.alert().accept()