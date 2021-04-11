import pyautogui as pt
from time import sleep
import pyperclip

sleep(3)
def check_green_mark():
    s = None
    while s is None:
        s = pt.locateOnScreen('msg.png')
        
        if s != None:
            print("greenee")
            pt.click(s)

def out():
    pt.click(310,310)



def new_print(Text):
    pt.typewrite(Text)
    pt.press("enter")
def get_msg():
    check_green_mark()
    sleep(2)
    pt.moveTo(807,877)
    sleep(2)
    pt.tripleClick()
    sleep(2)
    pt.click(button='right')
    sleep(2)
    pt.moveTo(885,717,duration=2)
    sleep(2)
    pt.click(815,672)
    


def display (values):

    pt.typewrite("-------------\n")
    pt.typewrite(f"/ {values[0]} / {values[1]} / {values[2]} /\n")
    pt.typewrite("-------------\n")
    pt.typewrite(f"/ {values[3]} / {values[4]} / {values[5]} /\n")
    pt.typewrite("-------------\n")
    pt.typewrite(f"/ {values[6]} / {values[7]} / {values[8]} /\n")
    pt.typewrite("-------------\n")


