import mouse
import random 
import time
from pynput.mouse import Button, Controller
import os, subprocess
import pyautogui

CWD = os.path.dirname(os.path.realpath(__file__))
firemaker = [1459, 937]
firstspot = [1460, 721] # on item grid, 0,0
middle = [270, 230]

def makeRandom(arr):
    arr[0] = (random.random() * 4) + (arr[0] - 2)
    arr[1] = (random.random() * 4) + (arr[1] - 2)
    return arr

def makeBuyTime(arr):
    arr[0] = (random.random() * 40) + (arr[0] - 20)
    arr[1] = (random.random() * 60) + (arr[1] - 30)
    return arr

class RuneController:
    def __init__(self):
        self.curLoc = firstspot

    def focus_tab(self):
        pynput = Controller()
        pynput.position = (36,36)
        pynput.click(Button.left, 1)

    #start = mouse.connected_bez([[545,525],makeRandom(firemaker)], 62, 1)
    #for i in start:
    #    mouse.move(i)
    def mouse_move(self, fromCor, toCor):
        fromm = makeRandom(fromCor)
        to = makeRandom(toCor)
        next = mouse.connected_bez([fromm, to], 62, 1)
        for b in next:
            mouse.move(b)

    # okay now its on the firestarter do_inventory([1459, 937], 6, 4)
    def do_inventory(firemakerloc, cols, rows):
        for i in range(cols):
            for z in range(rows):
                fromm = makeRandom(firemakerloc)
                to = makeRandom([firstspot[0] + (42 * z), firstspot[1] + (37 * i)])
                next = mouse.connected_bez([fromm, to], 62, 1)
                for b in next:
                    mouse.move(b)
                time.sleep(4.5)
                nextback = mouse.connected_bez([to, fromm], 62, 1)
                for b in nextback:
                    mouse.move(b)
                self.curLoc = firemakerloc
            
    def move_item(startrow, startcol, endrow, endcol):
        fromm = makeRandom([firstspot[0] + (42 * startrow), firstspot[1] + (37 * startcol)])
        to = makeRandom([firstspot[0] + (42 * endrow), firstspot[1] + (37 * endcol)])

    def get_coord_of_image(self, imgname, conf):
        pyautogui.locateOnScreen(CWD + '/img/' + imgname + '.png', confidence=conf,grayscale=True)
    
    def move_character(self, dir, length=1):
        self.mouse_move(self.curLoc, middle)
        loc = ()
        if dir == 'right':
            loc = [middle[0] + length * 20, middle[1]]
        if dir == 'left':
            loc = [middle[0] - length * 20, middle[1]]
        if dir == 'down':
            loc = [middle[0], middle[1] - length * 20]
        if dir == 'up':
            loc = [middle[0], middle[1] + length * 20]
        self.mouse_move(middle, loc)
        mouse.click()
        self.curLoc = loc
        time.sleep(2)

    def find_available_actions():
        # scan screen by going up and down to determine what tooltips show up