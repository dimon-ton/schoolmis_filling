import pyautogui
import pyperclip
from time import sleep


pyautogui.moveTo(x=3306, y=96, duration=1)
pyautogui.click()

pyautogui.press('home')
sleep(2)
pyautogui.scroll(clicks=-3000, _pause=True)



msg = 'ผ'
msg_list = ['2565 ชั้นประถมศึกษาปีที่ 6','ก16901','ก16902','ก16903','ก16904']


start_y = 700
for i in range(len(msg_list)):
    if i != 0:
        sleep(2)

    

    pyautogui.moveTo(x=3195, y=start_y, duration=1)
    pyautogui.click()
    start_y+=37

    if i == 0:
        pyautogui.moveTo(x=2851, y=249, duration=1)
        pyautogui.click()
        pyautogui.press('down', interval=1)
        pyautogui.press('enter', interval=1)
        pyautogui.press('tab', interval=1)

        sleep(1)
        pyperclip.copy(msg_list[0])
        pyautogui.hotkey('ctrl', 'v', interval=1)

        

        # click at center
        pyautogui.moveTo(x=3110, y=371, duration=1)
        pyautogui.click()
    elif i == 1:
        pyautogui.moveTo(x=2851, y=249, duration=1)
        pyautogui.click()
        pyautogui.press(['down','down'], interval=1)
        pyautogui.press('enter', interval=1)
        pyautogui.press('tab', interval=1)  
        pyautogui.press('enter', interval=1)
        pyperclip.copy(msg_list[1])
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

        pyautogui.click(x=2942, y=296, duration=1)
        pyperclip.copy(msg)
        pyautogui.hotkey('ctrl', 'v', interval=1)
        pyautogui.moveTo(x=3110, y=371, duration=1)
        pyautogui.click()
    elif i == 2:
        pyautogui.moveTo(x=2851, y=249, duration=1)
        pyautogui.click()
        pyautogui.press(['down','down'], interval=1)
        pyautogui.press('enter', interval=1)
        pyautogui.press('tab', interval=1)  
        pyautogui.press('enter', interval=1)
        pyperclip.copy(msg_list[2])
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

        pyautogui.click(x=2942, y=296, duration=1)
        pyperclip.copy(msg)
        pyautogui.hotkey('ctrl', 'v', interval=1)
        pyautogui.moveTo(x=3110, y=371, duration=1)
        pyautogui.click()
    elif i == 3:
        pyautogui.moveTo(x=2851, y=249, duration=1)
        pyautogui.click()
        pyautogui.press(['down','down'], interval=1)
        pyautogui.press('enter', interval=1)
        pyautogui.press('tab', interval=1)  
        pyautogui.press('enter', interval=1)
        pyperclip.copy(msg_list[3])
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

        pyautogui.click(x=2942, y=296, duration=1)
        pyperclip.copy(msg)
        pyautogui.hotkey('ctrl', 'v', interval=1)
        pyautogui.moveTo(x=3110, y=371, duration=1)
        pyautogui.click()
    elif i == 4:
        pyautogui.moveTo(x=2851, y=249, duration=1)
        pyautogui.click()
        pyautogui.press(['down','down'], interval=1)
        pyautogui.press('enter', interval=1)
        pyautogui.press('tab', interval=1)  
        pyautogui.press('enter', interval=1)
        pyperclip.copy(msg_list[4])
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

        pyautogui.click(x=2860, y=326, duration=1)
        pyperclip.copy(msg)
        pyautogui.hotkey('ctrl', 'v', interval=1)
        pyautogui.moveTo(x=3109, y=405, duration=1)
        pyautogui.click()

sleep(1)
pyautogui.scroll(clicks=-800, _pause=True)

pyautogui.click(x=2865, y=885, interval=1)
pyautogui.press('enter', interval=1)


pyautogui.hotkey('ctrl', 'w')