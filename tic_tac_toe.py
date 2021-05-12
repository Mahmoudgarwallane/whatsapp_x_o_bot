import pi
import pyautogui as pt
from time import sleep
import pyperclip
import keyboard

def check_green_mark():
    
    s = None
    while s is None:
    
        if keyboard.is_pressed("q"):
            quit()
        s = pt.locateOnScreen('m.png',grayscale=True,confidence=.9)
        

        if s != None:
            print("green mark is here")
            x,y = pt.center(s)
            pt.click(x-50,y)

def out():
    pt.click(216,216)



def new_print(Text):
    pt.typewrite(Text)
    pt.press("enter")
def get_msg():
    print("we've got the message ")
    check_green_mark()
    pt.moveTo(712,906)
    sleep(1)
    pt.tripleClick()
    pt.keyDown('ctrl')
    pt.press('c')
    pt.keyUp('ctrl')
    print("text > ")
    text = pyperclip.paste()
    print(text)
    return text
    
    


def display (values):
    pt.typewrite(f"/ {values[0]} / {values[1]} / {values[2]} /\n/ {values[3]} / {values[4]} / {values[5]} /\n/ {values[6]} / {values[7]} / {values[8]} /\n")
def check_winner(values,player1,player2):
    if values[0] == "O" and values[1] == "O" and values[2] == "O" or values[0] == "O" and values[3] == "O" and values[6] == "O" or values[6] == "O" and values[7] == "O" and values[8] == "O" or values[2] == "O" and values[5] == "O" and values[8] == "O" or values[0] == "O" and values[4] == "O" and values[8] == "O" or values[2] == "O" and values[4] == "O" and values[6] == "O" or values[3] == "O" and values[4] == "O" and values[5] == "O" or values[1] == "O" and values[4] == "O" and values[7] == "O":
        new_print(f"{player1} win ")
        return True
    elif values[0] == "X" and values[1] == "X" and values[2] == "X" or values[0] == "X" and values[3] == "X" and values[6] == "X" or values[6] == "X" and values[7] == "X" and values[8] == "X" or values[2] == "X" and values[5] == "X" and values[8] == "X" or values[0] == "X" and values[4] == "X" and values[8] == "X" or values[2] == "X" and values[4] == "X" and values[6] == "X" or values[3] == "X" and values[4] == "X" and values[5] == "X" or values[1] == "X" and values[4] == "X" and values[7] == "X":
        new_print(f"{player2} win ")  
        return True
    else:
        return False   


def play(values,player1,player2) :   
    display(values)
    for i in range(1,20):
        who_is_playing = player2 if i%2 == 0 else player1
        new_print(f"{who_is_playing} type  a number  ")
        out()
        inp = int(str(get_msg()))
        if values[inp - 1] == inp:
            if i % 2  == 0 :
                values[inp - 1 ] = "X"
            else : values[inp - 1 ] = "O"
        print(values)
        display(values)
        if check_winner(values,player1,player2) == True:
            break
        if i == 10 :
            new_print("Draw ") 
            break    
                                                                                                                                                                                                                                                                                   #win_pos = [[1,2,3],[1,4,7],[7,8,9],[3,6,9],[1,5,9],[3,5,7]]
while True: 
    print("I'm here")
    if  get_msg() == "play":
        print("1")
        text2 = "player 1  enter your name "
        new_print(text2)
        out()
        print("2")
        player1 = get_msg()
        print("3")
        
        print(player1)
        new_print("player 2  enter your name ")
        out()
        player2 = get_msg()
        values = [i+1 for i in range(9)]
        play(values,player1,player2)
        out()
        break
    else :

        out()
        continue
        
