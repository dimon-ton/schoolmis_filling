import pyautogui
from time import sleep
import pyperclip


# p = pyautogui.position()
# print(p)

pyautogui.moveTo(x=1359, y=383, duration=1)
pyautogui.click()

pyautogui.press('home')
sleep(1)
pyautogui.scroll(-1666)

# insert data



# data

msg1 = "2565 ชั้นประถมศึกษาปีที่ 6"
msg2 = "ท16"
msg3 = "ค16"
msg4 = "ว16"
msg5 = "ส16101"
msg6 = "ส16102"
msg7 = "พ16"
msg8 = "ศ16"
msg9 = "ง16"
msg10 = "อ16"


# fiscal year
start_y = 135
for i in range(14):
    if i != 0:
        sleep(4)
    pyautogui.moveTo(x=902, y=start_y, duration=1)
    pyautogui.click()
    start_y+=43

    if i == 0:
        pyautogui.moveTo(x=654, y=212, duration=1)
        pyautogui.click()
        pyautogui.press('down', interval=1)
        pyautogui.press('enter', interval=1)
        pyautogui.press('tab', interval=1)
        pyperclip.copy(msg1)
        pyautogui.hotkey('ctrl', 'v')
        # click at center
        pyautogui.moveTo(x=910, y=339, duration=1)
        pyautogui.click()

    elif i == 1:
        pyautogui.moveTo(x=654, y=212, duration=1)
        pyautogui.click()
        pyautogui.press(['down','down','down'])
        pyautogui.press('enter')
        pyautogui.moveTo(x=910, y=339, duration=1)
        pyautogui.click()
    elif i == 2:
        pyautogui.moveTo(x=654, y=212, duration=1)
        pyautogui.click()
        pyautogui.press(['down','down'], interval=1)
        pyautogui.press('enter', interval=1)
        pyautogui.press('tab', interval=1)  
        pyautogui.press('enter', interval=1)
        sleep(1)
        pyperclip.copy(msg2)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyautogui.moveTo(x=910, y=339, duration=1)
        pyautogui.click()
    elif i == 3:
        pyautogui.moveTo(x=654, y=212, duration=1)
        pyautogui.click()
        pyautogui.press(['down','down'], interval=1)
        pyautogui.press('enter', interval=1)
        pyautogui.press('tab', interval=1)  
        pyautogui.press('enter', interval=1)
        sleep(1)
        pyperclip.copy(msg3)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyautogui.moveTo(x=910, y=339, duration=1)
        pyautogui.click()
    elif i == 4:
        pyautogui.moveTo(x=654, y=212, duration=1)
        pyautogui.click()
        pyautogui.press(['down','down'], interval=1)
        pyautogui.press('enter', interval=1)
        pyautogui.press('tab', interval=1)  
        pyautogui.press('enter', interval=1)
        sleep(1)
        pyperclip.copy(msg4)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyautogui.moveTo(x=910, y=339, duration=1)
        pyautogui.click()
    elif i == 5:
        pyautogui.moveTo(x=654, y=212, duration=1)
        pyautogui.click()
        pyautogui.press(['down','down'], interval=1)
        pyautogui.press('enter', interval=1)
        pyautogui.press('tab', interval=1)  
        pyautogui.press('enter', interval=1)
        sleep(1)
        pyperclip.copy(msg5)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyautogui.moveTo(x=910, y=339, duration=1)
        pyautogui.click()
    elif i == 6:
        pyautogui.moveTo(x=654, y=212, duration=1)
        pyautogui.click()
        pyautogui.press(['down','down'], interval=1)
        pyautogui.press('enter', interval=1)
        pyautogui.press('tab', interval=1)  
        pyautogui.press('enter', interval=1)
        sleep(1)
        pyperclip.copy(msg6)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyautogui.moveTo(x=910, y=339, duration=1)
        pyautogui.click()
    elif i == 7:
        pyautogui.moveTo(x=654, y=212, duration=1)
        pyautogui.click()
        pyautogui.press(['down','down'], interval=1)
        pyautogui.press('enter', interval=1)
        pyautogui.press('tab', interval=1)  
        pyautogui.press('enter', interval=1)
        sleep(1)
        pyperclip.copy(msg7)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyautogui.moveTo(x=910, y=339, duration=1)
        pyautogui.click()
    elif i == 8:
        pyautogui.moveTo(x=654, y=212, duration=1)
        pyautogui.click()
        pyautogui.press(['down','down'], interval=1)
        pyautogui.press('enter', interval=1)
        pyautogui.press('tab', interval=1)  
        pyautogui.press('enter', interval=1)
        sleep(1)
        pyperclip.copy(msg8)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyautogui.moveTo(x=910, y=339, duration=1)
        pyautogui.click()
    elif i == 9:
        pyautogui.moveTo(x=654, y=212, duration=1)
        pyautogui.click()
        pyautogui.press(['down','down'], interval=1)
        pyautogui.press('enter', interval=1)
        pyautogui.press('tab', interval=1)  
        pyautogui.press('enter', interval=1)
        sleep(1)
        pyperclip.copy(msg9)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyautogui.moveTo(x=910, y=339, duration=1)
        pyautogui.click()
    elif i == 10:
        pyautogui.moveTo(x=654, y=212, duration=1)
        pyautogui.click()
        pyautogui.press(['down','down'], interval=1)
        pyautogui.press('enter', interval=1)
        pyautogui.press('tab', interval=1)  
        pyautogui.press('enter', interval=1)
        sleep(1)
        pyperclip.copy(msg10)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyautogui.moveTo(x=910, y=339, duration=1)
        pyautogui.click()


    



'''
# popup
pyautogui.moveTo(x=1359, y=383, duration=1)
pyautogui.tripleClick()
# click button
pyautogui.moveTo(x=1359, y=383, duration=1)
pyautogui.click()

'''



