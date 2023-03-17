import pyautogui
from time import sleep
import pyperclip


def insertData():
    date_txt = '31/03/2566'

    msg1 = 'ผู้เรียนรายวิชาพื้นฐาน จำนวน 5,040 ชั่วโมง และรายวิชาเพิ่มเติม/กิจกรรมเพิ่มเติม จำนวน 240 ชั่วโมง'
    msg2 = 'ผู้เรียนมีผลการประเมินรายวิชาพื้นฐานระดับ 1 ขึ้นไปทุกวิชา'

    pyautogui.click(x=3112, y=89, interval=1)
    pyautogui.press('home', interval=1)

    pyautogui.vscroll(clicks=-3900, _pause=True)

    # option1
    pyautogui.click(x=3090, y=209, duration=1)
    pyautogui.press('down')
    pyautogui.press('enter')

    # option2
    pyautogui.click(x=3096, y=275, duration=1)
    pyautogui.press(['up', 'up'])
    pyautogui.press('enter')

    # option3
    pyautogui.click(x=3075, y=338, duration=1)
    pyautogui.press(['up', 'up'])
    pyautogui.press('enter')

    # option4
    pyautogui.click(x=3108, y=398, duration=1)
    pyautogui.press(['up', 'up'])
    pyautogui.press('enter')

    # input date
    pyautogui.tripleClick(x=2185, y=496, duration=1)
    pyperclip.copy(date_txt)
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)
    pyautogui.press('esc')

    pyautogui.tripleClick(x=2750, y=496, duration=1)
    pyperclip.copy(date_txt)
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)
    pyautogui.press('esc')

    # insert text
    pyautogui.tripleClick(x=2206, y=596, duration=1)
    pyperclip.copy(msg1)
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.tripleClick(x=2207, y=644, duration=1)
    pyperclip.copy(msg2)
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.click(x=2812, y=801, duration=1)
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'w')

def schoolmis_main():
    pyautogui.click(x=2859, y=799, duration=1)
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.click(x=3318, y=794, duration=1)
    sleep(1)


if __name__ == '__main__':


    schoolmis_main()
    insertData()
