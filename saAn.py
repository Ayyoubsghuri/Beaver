import pyautogui
import cv2
import pytesseract
import time
import os
import glob
from tkinter import messagebox


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
)

def check_click(num):
    num=pyautogui.locateOnScreen(f"imgPC/{num}.png", confidence=0.9)
    pyautogui.moveTo(num.left, num.top,0.5)
    pyautogui.click(num)

def saveOneAnswer():
    pyautogui.hotkey('ctrl', "+")
    nu=pyautogui.locateOnScreen(f"imgPC/Begin/green_corn.png", confidence=0.9)
    pyautogui.moveTo(nu.left, nu.top,0.5)
    pyautogui.click(nu)
    # time.sleep(2)
    num=pyautogui.locateOnScreen(f"imgPC/Begin/green_end_corn.png", confidence=0.9)
    left = num.left - nu.left
    top = num.top - nu.top
    im = pyautogui.screenshot(region=(nu.left,num.top, left+20,top+70))
    im.save('temp/new.jpg')
    time.sleep(3)
    m=cv2.imread("temp/new.jpg")
    gray = cv2.cvtColor(m, cv2.COLOR_BGR2GRAY) # convert to grayscale
    retval, thresh_gray = cv2.threshold(gray, thresh=245, maxval=10, \
                                    type=cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh_gray,cv2.RETR_LIST, \
                                    cv2.CHAIN_APPROX_SIMPLE)
    I = 0
    for cont in contours:
        x,y,w,h = cv2.boundingRect(cont)
        area = w*h
        
        if 1000 < area:
            roi=m[y+5:y+h,x+5:x+w]
            cv2.imwrite(f'temp/An_crop_{I}.png', roi)
            I += 1
    # 2
    try:
        m=cv2.imread("temp/An_crop_0.png")
    except:
        messagebox.showerror("Message", "Something Went Wrong when saving answear")
    lvl_txt= pytesseract.image_to_string(m, lang='fra',config='--psm 7')
    if lvl_txt != "":
        oneAn= f"B {lvl_txt}"
    else:
        lvl_txt= pytesseract.image_to_string(m, lang='eng',config='--psm 7')
        oneAn= f"B {lvl_txt}"
    with open("answears.txt", "a") as file_object:
        file_object.write(f"{oneAn}")
    pyautogui.hotkey('ctrl', "num0")
    # time.sleep(3)
    files = glob.glob('temp/*.png')
    for f in files:
        os.remove(f)
    try:
        check_click("Begin/continue")
    except:
        check_click("Begin/continue2")


def saveAnswears():
    if not pyautogui.locateOnScreen(f"imgPC/Begin/X.png", confidence=0.9):
        time.sleep(2)
        if pyautogui.locateOnScreen(f"imgPC/END.png", confidence=0.9):
            check_click("END")
        time.sleep(3)
        check_click("Begin/confirm")
        if pyautogui.locateOnScreen(f"imgPC/Begin/green_corn.png", confidence=0.9):
            saveOneAnswer()
            return True
        else:    
            lvl=pyautogui.locateOnScreen(f"imgPC/Begin/corn_long.png", confidence=0.9)
            pyautogui.moveTo(lvl.left, lvl.top,0.5)
            im = pyautogui.screenshot(region=(lvl.left,lvl.top, 690,210))
            im.save('temp/an.jpg')
            m=cv2.imread("temp/an.jpg")
            lvl_txt= pytesseract.image_to_string(m, lang='fra',config='--psm 7')
            with open("answears.txt", "a") as file_object:
                file_object.write(f"{lvl_txt}")
            time.sleep(5)
            try:
                check_click("Begin/continue")
            except:
                check_click("Begin/continue2")
            return False

    