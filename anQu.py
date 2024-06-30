import cv2
import numpy as np
import glob
import re
from tkinter import messagebox
import os
import keyboard
import pytesseract
import pyautogui
import time

def corner():
    x,y,w,h =pyautogui.locateOnScreen(f"imgPC/Begin/corn.png", confidence=0.9)
    pyautogui.moveTo(x, y,1)
    im = pyautogui.screenshot(region=(x-120,y, 810,160))
    im.save('temp/an.png')
    
def check_click(name):
    num=pyautogui.locateOnScreen(f"{name}", confidence=0.9)
    pyautogui.moveTo(num.left, num.top,0.5)
    pyautogui.click(num)

def save():
    time.sleep(6)
    if not pyautogui.locateOnScreen(f"imgPC/Begin/corn.png", confidence=0.9):
        lv=pyautogui.locateOnScreen(f"imgPC/END.png", confidence=0.9)
        pyautogui.click(lv)
        # time.sleep(2)
        corner()
    else:
        corner()    

def answearQuestions(data):
    # save area of suggestion answears
    # time.sleep(2)
    save()
    print(f"data is : {data}")
    # read saved image
    img = cv2.imread('temp/an.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to grayscale
    retval, thresh_gray = cv2.threshold(gray, thresh=245, maxval=255, \
                                    type=cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh_gray,cv2.RETR_LIST, \
                                    cv2.CHAIN_APPROX_SIMPLE)
    
    # split all answears into readeable images 
    for i,cont in enumerate(contours):
        x,y,w,h = cv2.boundingRect(cont)
        area = w*h
        if area > 2050:
            roi=img[y:y+h,x:x+w]
            cv2.imwrite(f'imgAn/Image_crop_{i}.jpg', roi)

    word = re.compile(f"{data}") 
    # find image that contain text same as answear
    b=[]
    for name in glob.glob('imgAn/*.jpg'):
        img=cv2.imread(f"{name}")
        lvl_txt= pytesseract.image_to_string(img, lang='fra',config='--oem 1 --psm 11')
        # print(lvl_txt)
        if word.match(lvl_txt.strip()):
            print(f"found it on image {name}")
            b.append(name)
    try:
        check_click(f"{b[0]}")
    except:
        data= data.replace("\s", " ")
        messagebox.showerror(f"Answear Line is empty ", "It look i can't answear this Question ,Check Your Answears.txt file! or imgAn file! \n \n btw: the answear i was loking for is : "+ data)
    b.clear()

def answearQuestionsWriting(data):
    check_click("imgPC/Begin/writing.png")
    s = data
    for i in s:
        time.sleep(0.1)
        keyboard.write(f'{i}')
    