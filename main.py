import pyautogui
import time

for x in range(3):
    pyautogui.rightClick(x=400, y=30)
    pyautogui.leftClick(x=480, y =100)
    time.sleep(1)
    pyautogui.leftClick(x=300, y =500)
    pyautogui.leftClick(x=560, y =570)
    pyautogui.leftClick(x=560, y =870)
    time.sleep(1)
    pyautogui.leftClick(x=85, y =65)
    time.sleep(3)
    pyautogui.leftClick(x=1030, y =516)
