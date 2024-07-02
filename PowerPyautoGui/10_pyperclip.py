# Como digitar com pyautogui
import pyautogui
from time import sleep
import pyperclip


def write_pharse(pharse):
    pyperclip.copy(pharse)
    pyautogui.hotkey('ctrl', 'v')


pyautogui.moveTo(1559, 1046, duration=2)
pyautogui.click()
write_pharse('Olá, bom dia')
pyautogui.click(1873, 1033, duration=1)


# Funcao para imprimir caracteres especiais

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')


# Navegar e clicar no campo Usuario
pyautogui.moveTo(x=994, y=205, duration=2)
pyautogui.click()
sleep(1)
escrever_frase('admin')
sleep(1)
# Apertar tab
pyautogui.press('tab')
sleep(1)
# Digitar minha senha
escrever_frase('123456')
sleep(1)
# apertar tab
pyautogui.press('tab')
sleep(1)
# apertar space
pyautogui.press('space')
