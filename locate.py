import pyautogui, sys
import time
import cv2
import os
import glob



def Locate():
    files = glob.glob('temp/*.png')
    for f in files:
        os.remove(f)
    x,y,w,h =pyautogui.locateOnScreen(f"imgPC/ROWS/corn.png", confidence=0.9)
    pyautogui.moveTo(x, y,0.5)
    im = pyautogui.screenshot(region=(x,y, 980,450))
    im.save('temp/an.jpg')
    time.sleep(2)
    img = cv2.imread('temp/an.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to grayscale
    retval, thresh_gray = cv2.threshold(gray, thresh=245, maxval=10, \
                                    type=cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh_gray,cv2.RETR_LIST, \
                                    cv2.CHAIN_APPROX_SIMPLE)
    I = 0
    for cont in contours:
        x,y,w,h = cv2.boundingRect(cont)
        area = w*h
        
        if 6100 > area > 4900:
            roi=img[y:y+h,x:x+w]
            cv2.imwrite(f'temp/ROW_crop_{I}.png', roi)
            I += 1