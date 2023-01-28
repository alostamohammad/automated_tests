import pytest
from selenium import webdriver
from pages.loginpage import Guru99LoginPage


@pytest.fixture
def browser():
    br = webdriver.Chrome(executable_path='chromedriver')
    br.implicitly_wait(30)
    yield br
    br.quit()


def test_success_login(browser):
    login_page = Guru99LoginPage(browser)
    login_page.load()
    login_page.login('mngr473903', 'UvAsUze')
    page_title, source = login_page.title_source()
    assert 'GTPL Bank Manager HomePage' in page_title
    assert "Welcome To Manager's Page of GTPL Bank" in source


def test_fail_login(browser):
    login_page = Guru99LoginPage(browser)
    login_page.load()
    login_page.login('mngr473903', 'randomPassword')
    alert_text = login_page.browser.switch_to.alert.text
    assert 'User is not valid' in alert_text
