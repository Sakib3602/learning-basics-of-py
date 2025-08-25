import pyautogui
import time
time.sleep(5)
pyautogui.write('?', interval=0.25)
pyautogui.press('enter')
pyautogui.alert('This is the message to display.')


