from pages.demoqa import DemoQa
from conftest import browser


def test_site_visit(browser):
    DP = DemoQa(browser)
    DP.visit()
    DP.click_on_the_icon()
    assert DP.equal_url()
    assert DP.exist_icon()

