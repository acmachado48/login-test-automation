from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://automationpractice.pl/index.php?controller=authentication&back=my-account"

    def open(self):
        self.driver.get(self.url)

    def fill_login_email(self, email):
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_input.send_keys(email)

    def fill_sign_up_email(self, email):
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "email_create"))
        )
        email_input.send_keys(email)    

    def fill_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "passwd"))
        ).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "SubmitLogin"))
        ).click()

    def click_create(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "SubmitCreate"))
        ).click()
  
    def get_error_message(self):
      try:
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger"))
        )
        return element.text
      except:
        return ""


    def is_logged_in(self):
        return "my-account" in self.driver.current_url
    
