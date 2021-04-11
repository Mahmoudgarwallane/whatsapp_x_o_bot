
def check_green_mark():
    #this function check for new messages 
    s = None
    while s is None:
    
        if keyboard.is_pressed("q"):
            quit()
        s = pt.locateOnScreen('m.png',grayscale=True,confidence=.9)
        

        if s != None:
            x,y = pt.center(s)
            pt.click(x-50,y)

def out():
    #this function get out of the conversation to get new messages
    pt.click(216,216)



def new_print(Text):
    #this function write messages
    pt.typewrite(Text)
    pt.press("enter")
def get_msg():
    #this function read messages 
    check_green_mark()
    pt.moveTo(712,906)
    pt.tripleClick()
    pt.click(button='right')
    pt.moveTo(754,928)
    pt.click(754,928)
    
    return pyperclip.paste()
    
    
