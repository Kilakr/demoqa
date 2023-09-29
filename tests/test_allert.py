from components.components import WebElement
from conftest import browser
from pages.alerts import Alert
import time

def test_alerts(browser):
    page_check1 = Alert(browser)
    page_check1.visit()
    assert not page_check1.alert()
    page_check1.alert1.click()
    time.sleep(2)
    assert page_check1.alert()
    page_check1.alert().accept()
def test_alert_text(browser):
    page_check1 = Alert(browser)
    page_check1.visit()
    page_check1.alert1.click()
    time.sleep(2)
    assert page_check1.alert().text == 'You clicked a button'
    page_check1.alert().accept()
    assert not page_check1.alert()
def test_confirm(browser):
    page_check1 = Alert(browser)
    page_check1.visit()
    page_check1.alert2.click()
    time.sleep(2)
    page_check1.alert().dismiss()
    assert page_check1.confresult.get_text() == 'You selected Cancel'

def test_prompt(browser):
    page_check1 = Alert(browser)
    page_check1.visit()
    page_check1.alert3.click()
    time.sleep(2)
    page_check1.alert().send_keys('Artem')
    page_check1.alert().accept()
    assert page_check1.promptresult.get_text() == 'You entered Artem'
