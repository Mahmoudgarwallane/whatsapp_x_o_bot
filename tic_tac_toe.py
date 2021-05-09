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
            print("greenee")
            x,y = pt.center(s)
            pt.click(x-50,y)

def out():
    pt.click(216,216)



def new_print(Text):
    pt.typewrite(Text)
    pt.press("enter")
def get_msg():
    print("eyoo")
    check_green_mark()
    pt.moveTo(712,906)
    pt.tripleClick()
    pt.click(button='right')
    pt.moveTo(754,928)
    pt.click(754,928)
    
    return pyperclip.paste()
    
    


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
        new_print(f"{who_is_playing} entrer  un nombre ")
        out()
        inp = int(get_msg())
        if values[inp - 1] == inp:
            if i % 2  == 0 :
                values[inp - 1 ] = "X"
            else : values[inp - 1 ] = "O"
        print(values)
        display(values)
        if check_winner(values,player1,player2) == True:
            break
        if i == 10 :
            new_print("equality") 
            break                                                                                                                                                                                                                                                                                       #win_pos = [[1,2,3],[1,4,7],[7,8,9],[3,6,9],[1,5,9],[3,5,7]]
while 1: 
    if get_msg() == "play":
        print("1")
        text = "le joueur1 enter votre nom "
        new_print(text)
        out()
        print("2")
        player1 = get_msg()
        print("3")
        
        print(player1)
        new_print("le joueur 2 enter votre nom")
        out()
        player2 = get_msg()
        values = [i+1 for i in range(9)]
        play(values,player1,player2)
        out()
        break
    else :

        out()
        continue
        
