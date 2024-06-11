# Como digitar com pyautogui
import pyautogui
import pyperclip


def write_pharse(pharse):
    pyperclip.copy(pharse)
    pyautogui.hotkey('ctrl', 'v')


pyautogui.moveTo(1559, 1046, duration=2)
pyautogui.click()
write_pharse('Olá, bom dia')
pyautogui.click(1873, 1033, duration=1)
