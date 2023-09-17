from pages.demoqa import DemoQa
from conftest import browser


def test_site_visit(browser):
    DP = DemoQa(browser)
    DP.visit()
    DP.icon.click()
    assert DP.equal_url()
    assert DP.icon.exist()

