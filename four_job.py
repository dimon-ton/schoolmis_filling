import pyautogui
from time import sleep
import pyperclip

###########################################
msg1 = 'ว11101 วิทยาศาสตร์และ'

msg2 = 'ง11101'


msg3 = 'ว13101 วิทยาศาสตร์และ'

msg4 = 'ง13101'

msg5 = 'ว15101 วิทยาศาสตร์และ'

msg6 = 'ง15101'

###############################################

msg7 = 'ว12101 วิทยาศาสตร์และ'

msg8 = 'ง12101'

msg9 = 'ว14101 วิทยาศาสตร์และ'

msg10 = 'ง14101'

msg11 = 'ว16101 วิทยาศาสตร์และ'

msg12 = 'ง16101'


pyautogui.click(x=796, y=93, interval=1)
pyautogui.press('home', interval=1)

pyautogui.vscroll(clicks=-890, _pause=True)



###################### page1 ###########################

# sec1
pyautogui.click(x=31, y=309, interval=1, duration=1)

pyautogui.click(x=524, y=258, interval=1)
pyperclip.copy(msg1)
pyautogui.hotkey('ctrl', 'v', interval=2)
pyautogui.press('enter')

pyautogui.click(x=913, y=369, interval=1)

sleep(2)


# sec2


pyautogui.click(x=31, y=522, interval=1, duration=1)

pyautogui.click(x=622, y=264, interval=1)

pyperclip.copy(msg2)
pyautogui.hotkey('ctrl', 'v', interval=2)
pyautogui.press('down')
pyautogui.press('enter')

pyautogui.click(x=910, y=340, interval=1)

sleep(2)

# sec3
pyautogui.click(x=467, y=310, interval=1, duration=1)

pyautogui.click(x=524, y=258, interval=1)
pyperclip.copy(msg3)
pyautogui.hotkey('ctrl', 'v', interval=1)
pyautogui.press('enter')

pyautogui.click(x=913, y=369, interval=1)

sleep(2)


# sec4


pyautogui.click(x=468, y=523, interval=1, duration=1)

pyautogui.click(x=622, y=264, interval=1)

pyperclip.copy(msg4)
pyautogui.hotkey('ctrl', 'v', interval=1)
pyautogui.press('down')
pyautogui.press('enter')

pyautogui.click(x=910, y=340, interval=1)

sleep(2)


# sec5
pyautogui.click(x=902, y=309, interval=1, duration=1)

pyautogui.click(x=524, y=258, interval=1)
pyperclip.copy(msg5)
pyautogui.hotkey('ctrl', 'v', interval=1)
pyautogui.press('enter')

pyautogui.click(x=913, y=369, interval=1)

sleep(2)

# sec6


pyautogui.click(x=903, y=523, interval=1, duration=1)

pyautogui.click(x=622, y=264, interval=1)

pyperclip.copy(msg6)
pyautogui.hotkey('ctrl', 'v', interval=1)
pyautogui.press('down')
pyautogui.press('enter')

pyautogui.click(x=910, y=340, interval=1)

sleep(2)


################################## page2 #################################

pyautogui.vscroll(clicks=-800, _pause=True)

# sec1
pyautogui.click(x=32, y=289, interval=1, duration=1)

pyautogui.click(x=524, y=258, interval=1)
pyperclip.copy(msg7)
pyautogui.hotkey('ctrl', 'v', interval=1)
pyautogui.press('enter')

pyautogui.click(x=913, y=369, interval=1)

sleep(2)

# sec2

pyautogui.click(x=30, y=502, interval=1, duration=1)

pyautogui.click(x=622, y=264, interval=1)

pyperclip.copy(msg8)
pyautogui.hotkey('ctrl', 'v', interval=1)
pyautogui.press('down')
pyautogui.press('enter')

pyautogui.click(x=910, y=340, interval=1)

sleep(2)

# sec3
pyautogui.click(x=467, y=288, interval=1, duration=1)

pyautogui.click(x=524, y=258, interval=1)
pyperclip.copy(msg9)
pyautogui.hotkey('ctrl', 'v', interval=1)
pyautogui.press('enter')

pyautogui.click(x=913, y=369, interval=1)

sleep(2)

# sec4

pyautogui.click(x=467, y=503, interval=1, duration=1)

pyautogui.click(x=622, y=264, interval=1)

pyperclip.copy(msg10)
pyautogui.hotkey('ctrl', 'v', interval=1)
pyautogui.press('down')
pyautogui.press('enter')

pyautogui.click(x=910, y=340, interval=1)

sleep(2)

# sec5
pyautogui.click(x=903, y=286, interval=1, duration=1)

pyautogui.click(x=524, y=258, interval=1)
pyperclip.copy(msg11)
pyautogui.hotkey('ctrl', 'v', interval=1)
pyautogui.press('enter')

pyautogui.click(x=913, y=369, interval=1)

sleep(2)


# sec6

pyautogui.click(x=904, y=503, interval=1, duration=1)

pyautogui.click(x=622, y=264, interval=1)


pyperclip.copy(msg12)
pyautogui.hotkey('ctrl', 'v', interval=1)
pyautogui.press('down')
pyautogui.press('enter')

pyautogui.click(x=910, y=340, interval=1)

sleep(2)


pyautogui.vscroll(clicks=-950, _pause=True)

pyautogui.click(x=672, y=623, duration=1)
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'w')