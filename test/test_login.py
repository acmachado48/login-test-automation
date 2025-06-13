import pytest
import time
from pages.login_page import LoginPage

# Credenciais de teste
VALID_EMAIL = "jefefermcshart@gmail.com"
VALID_PASSWORD = "validAndSecurePassword"
INVALID_EMAIL = "invalidemail.com"
INVALID_PASSWORD = "invalidPassword"

@pytest.mark.usefixtures("browser")
class TestLogin:
    # Testa login com credenciais válidas
    def test_login_valid_credentials(self, browser):
        page = LoginPage(browser)
        page.open()
        page.fill_login_email(VALID_EMAIL)
        page.fill_password(VALID_PASSWORD)
        page.click_login()
        time.sleep(3) # Aguarda o carregamento da página após o login
        assert page.is_logged_in() # Verifica se o usuário está autenticado

    # Testa login com email inválido e senha inválida
    def test_login_invalid_email(self, browser):
        page = LoginPage(browser)
        page.open()
        page.fill_login_email(INVALID_EMAIL)
        page.fill_password(INVALID_PASSWORD)
        page.click_login()
        assert "Invalid email address." in page.get_error_message() # Verifica a mensagem de erro esperada
        
    # Testa login com email válido e senha incorreta
    def test_login_invalid_password(self, browser):
        page = LoginPage(browser)
        page.open()
        page.fill_login_email(VALID_EMAIL)
        page.fill_password(INVALID_PASSWORD)
        page.click_login()
        assert "Authentication failed." in page.get_error_message() # Verifica se a autenticação falhou corretamente
        