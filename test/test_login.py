import pytest
from pages.login_page import LoginPage


VALID_EMAIL = "jefefermcshart@gmail.com"
VALID_PASSWORD = "validAndSecurePassword"
INVALID_EMAIL = "invalidemail.com"
INVALID_PASSWORD = "invalidPassword"

@pytest.mark.usefixtures("browser")
class TestLogin:

    def test_login_valid_credentials(self, browser):
        page = LoginPage(browser)
        page.open()
        page.fill_login_email(VALID_EMAIL)
        page.fill_password(VALID_PASSWORD)
        page.click_login()
        assert page.is_logged_in()

    def test_login_invalid_email(self, browser):
        page = LoginPage(browser)
        page.open()
        page.fill_login_email(INVALID_EMAIL)
        page.fill_password(INVALID_PASSWORD)
        page.click_login()
        assert "Invalid email address." in page.get_error_message()

    def test_login_wrong_password(self, browser):
        page = LoginPage(browser)
        page.open()
        page.fill_login_email(VALID_EMAIL)
        page.fill_password(INVALID_PASSWORD)
        page.click_login()
        assert "Authentication failed." in page.get_error_message()
        