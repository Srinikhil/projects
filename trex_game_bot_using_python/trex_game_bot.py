from PIL import ImageGrab, ImageOps
import pyautogui
import time      
from numpy import *
 
class Cordinates():
     replayBtn = (215,356)
     dinosaur = (168,412)#395-y,168-x
     
def restartGame():
    pyautogui.click(Cordinates.replayBtn)
    pyautogui.keyDown('down')
    
def pressSpace():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    #time.sleep(0.05) 
    print("Jump") 
    time.sleep(0.18)
    pyautogui.keyUp ('space')
    pyautogui.keyDown('down')
     
def imageGrab():
    box = (Cordinates.dinosaur[0]+70,Cordinates.dinosaur[1],Cordinates.dinosaur[0]+110,
           Cordinates.dinosaur[1]+15)#32
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return(a.sum())

def main():
    restartGame()
    while True:
        if(imageGrab()!=930):
            pressSpace()
            time.sleep(0.1)  
main() 
 
# while True:
 #      imageGrab()