import webbrowser
import pyautogui
from time import sleep


webbrowser.open_new('https://cursoautomacao.netlify.app/')
sleep(1)
pyautogui.click(694, 247, duration=1)
pyautogui.scroll(-1500)
sleep(1)
campo_nome = pyautogui.locateCenterOnScreen('nome.png')
pyautogui.click(campo_nome[0], campo_nome[1], duration=1)
pyautogui.typewrite('Gabriel de Assis Machado')
sleep(1)
campo_alerta = pyautogui.locateCenterOnScreen('alerta.png')
pyautogui.click(campo_alerta[0], campo_alerta[1], duration=1)
sleep(1)
botao_ok = pyautogui.locateCenterOnScreen('ok.png')
pyautogui.click(botao_ok[0], botao_ok[1], duration=1)
sleep(1)
pyautogui.scroll(1600)
sleep(1)
pyautogui.scroll(-3600)
sleep(1.5)
campo_excel = pyautogui.locateCenterOnScreen('excel.png')
pyautogui.click(campo_excel[0], campo_excel[1], duration=1)
pyautogui.move(0, 40, duration=1)
sleep(1)
campo_pdf = pyautogui.locateCenterOnScreen('pdf.png')
pyautogui.click(campo_pdf[0], campo_pdf[1], duration=1)
pyautogui.move(0, 40, duration=1)
sleep(1)
pyautogui.alert(text='VOCÊ TERMINOU')
