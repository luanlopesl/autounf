# Créditos para www.youtube.com/MaxCodez

from selenium import webdriver
from time import sleep
from getpass import getpass

user = input("Digite seu nome de usuário: ")
passwd = getpass("Digite sua senha: ")

driver = webdriver.Chrome(executable_path="D:/Usuários/Desenvolvimento/Downloads/chromedriver_win32/chromedriver")

driver.get("https://www.instagram.com/")

sleep(4)

driver.find_element_by_xpath("//input[@name=\"username\"]")\
    .send_keys(user)
driver.find_element_by_xpath("//input[@name=\"password\"]")\
    .send_keys(passwd)
driver.find_element_by_xpath('//button[@type="submit"]')\
    .click()
sleep(4)

driver.get(f"https://www.instagram.com/{user}/")

following = driver.find_element_by_partial_link_text("seguindo")
following.click()

sleep(4)

for i in range(5):
    driver.find_element_by_xpath('//button[text()="Seguindo"]')\
        .click()
    driver.find_element_by_xpath('//button[text()="Deixar de seguir"]')\
        .click()
    sleep(2)
