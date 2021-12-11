from controller import RuneController
import time
import pyautogui

rune = RuneController()
rune.focus_tab()
rune.move_character('up', 3)
rune.move_character('right')
rune.move_character('down', 3)
rune.move_character('left')

#time.sleep(2)
#print(rune.get_coord_of_image('bank', .5))
