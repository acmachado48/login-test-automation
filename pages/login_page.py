from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Classe representando a página de login
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # URL da página de autenticação
        self.url = "http://automationpractice.pl/index.php?controller=authentication&back=my-account"

    # Método para abrir a página de login
    def open(self):
        self.driver.get(self.url)

    # Preenche o campo de email para login
    def fill_login_email(self, email):
        # Aguarda até que o campo de email esteja presente na página
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_input.send_keys(email)

    # Preenche o campo de email para criação de conta
    def fill_sign_up_email(self, email):
        # Aguarda até que o campo de criação de email esteja presente
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "email_create"))
        )
        email_input.send_keys(email)    

    # Preenche o campo de senha
    def fill_password(self, password):
        # Aguarda até que o campo de senha esteja presente e envia a senha
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "passwd"))
        ).send_keys(password)

    # Clica no botão de login
    def click_login(self):
        # Aguarda até que o botão esteja clicável
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "SubmitLogin"))
        ).click()

    # Clica no botão de criação de conta
    def click_create(self):
        # Aguarda até que o botão esteja clicável
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "SubmitCreate"))
        ).click()

    # Retorna a mensagem de erro exibida após falha no login
    def get_error_message(self):
        try:
            # Aguarda até que a mensagem de erro esteja visível
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger"))
            )
            return element.text
        except:
            # Retorna string vazia se não encontrar a mensagem (exceção silenciosa)
            return ""

    # Verifica se o usuário foi autenticado com sucesso
    def is_logged_in(self):
        # Confirma a navegação para a página da conta como sinal de sucesso
        return "my-account" in self.driver.current_url
