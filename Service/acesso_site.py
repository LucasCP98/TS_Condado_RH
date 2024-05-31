import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Service import dados_login
import pyautogui


class SwagLabs:

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

        # Driver para utilzar o Selenium.
        self.servico = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(options=self.options, service=self.servico)

        # Dados de Envio.
        self.primeiro_nome = "Lucas"
        self.segundo_nome = "Costa"
        self.cep = "88317-340"

    def acessando(self):
        # Abre a url do site.
        self.driver.get(self.url)

        # Captura dados do arquivo csv
        login, senha, adicionar_ao_carrinho_os_itens = dados_login.dados_loguin_senha(self)

        # Login e Senha
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(f"{login[0]}")
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(f"{senha[0]}")
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

        # 1 ---- Test.allTheThings() T-Shirt (Red)
        # 2 ---- Sauce Labs Bolt T-Shirt
        # 3 ---- Sauce Labs Bike Light
        for itens in adicionar_ao_carrinho_os_itens:
            WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located(
                (By.LINK_TEXT, f"{itens}")))
            procurando = self.driver.find_element(By.LINK_TEXT, f"{itens}")

            if procurando:
                if itens == "Test.allTheThings() T-Shirt (Red)":
                    # clica para adicionar ao carrinho.
                    WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="inventory_container"]/div/div[6]/div[3]/button')))
                    self.driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[6]/div[3]/button').click()

                if itens == "Sauce Labs Bolt T-Shirt":
                    # clica para adicionar ao carrinho.
                    WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="inventory_container"]/div/div[3]/div[3]/button')))
                    self.driver.find_element(By.XPATH,
                                             '//*[@id="inventory_container"]/div/div[3]/div[3]/button').click()
                if itens == "Sauce Labs Bike Light":
                    # clica para adicionar ao carrinho.
                    WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[3]/button')))
                    self.driver.find_element(By.XPATH,
                                             '//*[@id="inventory_container"]/div/div[2]/div[3]/button').click()

        # Clica no carrinho
        WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        self.driver.find_element(By.XPATH,
                                 '//*[@id="shopping_cart_container"]/a/span').click()

        # CHECKOUT
        WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="cart_contents_container"]/div/div[2]/a[2]')))
        self.driver.find_element(By.XPATH,
                                 '//*[@id="cart_contents_container"]/div/div[2]/a[2]').click()

        # Primeiro nome.
        WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="first-name"]')))
        self.driver.find_element(By.XPATH,
                                 '//*[@id="first-name"]').send_keys(f"{self.primeiro_nome}")

        # Segundo nome.
        WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="last-name"]')))
        self.driver.find_element(By.XPATH,
                                 '//*[@id="last-name"]').send_keys(f"{self.segundo_nome}")

        # CEP.
        WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="postal-code"]')))
        self.driver.find_element(By.XPATH,
                                 '//*[@id="postal-code"]').send_keys(f"{self.cep}")

        # Continue
        WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[2]/input')))
        self.driver.find_element(By.XPATH,
                                 '//*[@id="checkout_info_container"]/div/form/div[2]/input').click()

        # Print da tela inteira contendo o valor, salvo no arquivo de captura de tela do seu computador.
        pyautogui.hotkey('end')
        time.sleep(5)
        pyautogui.hotkey('win', 'printscreen')
        time.sleep(5)

        # Finish
        WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]/a[2]')))
        self.driver.find_element(By.XPATH,
                                 '//*[@id="checkout_summary_container"]/div/div[2]/div[8]/a[2]').click()

        self.driver.close()


if __name__ == '__main__':
    run = SwagLabs()
    run.acessando()
