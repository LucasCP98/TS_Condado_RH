import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Service import dados_login


class Next:

    def __init__(self):
        # Url licitações.
        self.url = "https://www.saucedemo.com/v1/"

        # Opções do Chrome.
        self.options = webdriver.ChromeOptions()

        # Maximinizar.
        self.options.add_argument("start-maximized")

        # Previne deteção do Selenium.
        self.options.add_argument("--disable-blink-features=AutomationControlled")

        # Tratativa do erro DevToolsActivePort file doesn't exist.
        self.options.add_argument("--no-sandbox")

        # Tratativa do erro DevToolsActivePort file doesn't exist.
        self.options.add_argument("--disable-dev-shm-usage")

        # Ir pelo browser anonimo.
        self.options.add_argument("incognito")

        # Capacidades Desejadas.
        self.caps = DesiredCapabilities().CHROME

        # Driver para utilzar o Selenium.
        self.driver = webdriver.Chrome(options=self.options, desired_capabilities=self.caps)

    def acessando(self):
        # Abre a url do site.
        self.driver.get(self.url)
        time.sleep(1000)

        # Captura dados do arquivo csv
        login, senha = dados_login.dados_loguin_senha(self)

        # Login e Senha
        self.driver.find_element(By.XPATH, '//*[@id="Email"]').send_keys(f"{login}")
        self.driver.find_element(By.XPATH, '//*[@id="Senha"]').send_keys(f"{senha}")
        self.driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]').click()

        # X
        WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located(
            (By.XPATH, '//a[@class="close-modal "]')))
        self.driver.find_element(By.XPATH,
                                 '//a[@class="close-modal "]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]').click()

        # Entrando na Empresa.
        WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@class="lista-menu"]//a[@href="/empresa/index"]')))

        self.driver.find_element(By.XPATH,
                                 '//*[@class="lista-menu"]//a[@href="/empresa/index"]').click()
