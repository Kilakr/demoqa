from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from components.components import WebElement
from conftest import browser
from pages.text_box import TextBox
from pages.heroku import HerokuPage
from pages.heroku_add import HerokuPageAdd
import time

def test_button_add(browser):
    page_check1 = HerokuPage(browser)
    page_check2 = HerokuPageAdd(browser)
    page_check1.visit()
    assert page_check1.link_elements.get_text() == 'Add/Remove Elements'
    page_check1.link_elements.click()
    assert page_check1.get_url() == 'http://the-internet.herokuapp.com/add_remove_elements/'
    time.sleep(2)
    assert page_check2.add_elements.get_text() == 'Add Element'
    assert page_check2.add_elements.get_dom_attribute('onclick') == 'addElement()'
    for c in range(4):
        page_check2.add_elements.click()
        time.sleep(1)
    assert len(page_check2.delete_element.find_elements()) == 4
    for c in range(4):
        assert page_check2.delete_element.find_elements()[c].text == 'Delete'
    while not len(page_check2.delete_element.find_elements()) == 0:
        page_check2.delete_element.click()
        time.sleep(1)
    time.sleep(2)
    assert len(page_check2.delete_element.find_elements()) == 0
