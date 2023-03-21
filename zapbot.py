from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class WhatsappBot:
    def __init__(self):
        self.mensagem = "Mensagem Automatica"
        self.grupos_ou_pessoas = ["Amor♥️","Amor♥️","Amor♥️"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            campo_grupo = self.driver.find_element(By.XPATH,f"//span[@title='{grupo_ou_pessoa}']")
            time.sleep(3)
            campo_grupo.click()
            chat_box = self.driver.find_element(By.CLASS_NAME,'_3Uu1_')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element(By.XPATH,"//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)


bot = WhatsappBot()
bot.EnviarMensagens()
""" py.exe zapbot.py """
