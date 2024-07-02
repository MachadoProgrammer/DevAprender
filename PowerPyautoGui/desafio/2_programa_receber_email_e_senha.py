# Cria um programa que recebe email e senha e copia e cola a senha dentro do bloco de notas

import pyautogui
import pyperclip
from time import sleep


def main(email, senha):
    pyperclip.copy(email)
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)
    pyautogui.press('enter')
    pyperclip.copy(senha)
    pyautogui.hotkey('ctrl', 'v')


email = pyautogui.prompt(text='Digite seu email', title='Info')
senha = pyautogui.password(text='password', title='password', mask='*')

pyautogui.moveTo(1322, 249, duration=1.3)
pyautogui.click()
main(email, senha)
