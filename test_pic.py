import pyautogui
from time import sleep


m = pyautogui.locateOnScreen('label.png', confidence=0.9)

center = pyautogui.center(m)
pyautogui.moveTo(center, duration=1)

print(type(m))
print(m)