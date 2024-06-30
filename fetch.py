import pyautogui
import time
from locate import Locate
from anQu import save,answearQuestions,answearQuestionsWriting
from saAn import saveAnswears
import os
import glob
import pytesseract
import cv2
import numpy as np

pyautogui.FAILSAFE = True
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
)
def check_click(num):
    num=pyautogui.locateOnScreen(f"imgPC/{num}.png", confidence=0.9)
    pyautogui.moveTo(num.left, num.top,0.5)
    pyautogui.click(num)
    
def already_completed(name):
    Locate()
    check = cv2.imread('imgPC/ROWS/check.png')
    img = cv2.imread(f'{name}')
    w, h = check.shape[:-1]
    res = cv2.matchTemplate(img, check, cv2.TM_CCOEFF_NORMED)
    threshold = .8
    loc = np.where(res >= threshold)
    pt = None
    for pt in zip(*loc[::-1]):
        pass
    if pt is None:
        return False
    else:
        return True
    
    
def rows_click():
    files = glob.glob('temp/*.png')
    for f in files:
        os.remove(f)
    Locate()
    # time.sleep(2)
    b=[]
    for name in glob.glob('temp/*.png'):
        if already_completed(f"{name}") is False:
            b.append(name)
    if len(b)!= 0:
        print(b)
        num=pyautogui.locateOnScreen(f"{b[len(b)-1]}", confidence=0.9)
        pyautogui.moveTo(num.left, num.top,0.5)
        pyautogui.click(num)
        return True
    else:
        return False

def ex():
    time.sleep(2)
    if pyautogui.locateOnScreen(f"imgPC/Begin/end.png", confidence=0.9):
        check_click("Begin/end")
    elif pyautogui.locateOnScreen(f"imgPC/Begin/video.png", confidence=0.9):
        check_click("Begin/video")
        time.sleep(10)
        check_click("Begin/end")
        time.sleep(7)
        check_click("Begin/play")
        time.sleep(5)
        check_click("Begin/V")
        time.sleep(4)
        check_click("Begin/continue3")
    elif pyautogui.locateOnScreen(f"imgPC/Begin/ex.png", confidence=0.9) or pyautogui.locateOnScreen(f"imgPC/Begin/ex2.png", confidence=0.9) or pyautogui.locateOnScreen(f"imgPC/Begin/grade.png", confidence=0.9):
        try:
            check_click("Begin/ex")
        except:
            try:
                check_click("Begin/ex2")
            except:
                check_click("Begin/grade")
                time.sleep(2)
                check_click("Begin/start")
                time.sleep(2)
        while True:
            time.sleep(3)
            if pyautogui.locateOnScreen(f"imgPC/Begin/X.png", confidence=0.9):
                break
            else:
                checkOneAn=saveAnswears()
        time.sleep(2)
        check_click("Begin/repeat")
        time.sleep(4)
        try:
            check_click("Begin/start")
            time.sleep(2)
        except:
            pass
        while True:
            time.sleep(6)
            if pyautogui.locateOnScreen(f"imgPC/Begin/V.png", confidence=0.9):
                try:
                    check_click("Begin/continue")
                except:
                    try:
                        check_click("Begin/continue2")
                    except:
                        check_click("Begin/continue3")
                with open("answears.txt", 'r+') as f:
                    f.truncate(0)
                break 
            else:
                time.sleep(3)
                if not pyautogui.locateOnScreen(f"imgPC/Begin/V.png", confidence=0.9):
            # open line of answear ans get data
                    s=""
                    backslash ="\s"
                    with open('answears.txt', 'r') as myfile:
                        data=myfile.read()
                        dt=data.split('\n')
                    for line in dt:
                        li=line.split(" ")
                        save = []
                        if checkOneAn:
                            if li[0] != "" and len(li) > 1:
                                save = []
                                for count,ele in enumerate(li):
                                    if ele =="B" or ele =="E" or ele =="Ü" or ele=="Ü]":
                                        save.append(count+1)
                                print(f"save is : {save}")
                                for i in li[save[len(save)-1]:len(li)]:
                                    s += f"{i} "
                                s_strip=s.strip()
                                s_new=s_strip.replace(" ", f"{backslash}")
                                print(f"The One Answear is : {s_new}")
                                time.sleep(2)
                                if not pyautogui.locateOnScreen(f"imgPC/Begin/V.png", confidence=0.9):
                                    answearQuestions(f"{s_new}")
                        elif pyautogui.locateOnScreen(f"imgPC/Begin/endline.png", confidence=0.9):
                            time.sleep(2)
                            num=pyautogui.locateOnScreen(f"imgPC/Begin/endline.png", confidence=0.9)
                            im = pyautogui.screenshot(region=(num.left+25,num.top, 120,70))
                            txt= pytesseract.image_to_string(im, lang='fra',config='--psm 7')
                            new=txt.split(" ")
                            if new[0].find("\n")!=-1:
                                new[0]=new[0].replace("\n","")
                            for count,ele in enumerate(li):
                                if ele =="B" or ele =="E" or ele =="Ü" or ele=="Ü]" or ele=="[|" or ele=="D" or ele=="b" or ele=="ü":
                                    save.append(count+1)
                            New =[]
                            if new[0]== "|":
                                for i in li:
                                    if i.find("(")!=-1:
                                        New.append(i)
                                new[0]=New[0]
                            if new[0]== ":":
                                for i in li:
                                    if i.find(".")!=-1:
                                        New.append(i)
                                if len(New) > 1:
                                    new[0]=New[1]
                                else:
                                    new[0]=New[0]
                            print(new[0])
                            for i in li[save[len(save)-1]:li.index(new[0])]:
                                s += f"{i} "
                            s_strip=s.strip()
                            answearQuestionsWriting(f"{s_strip}")
                        else:
                            for count,ele in enumerate(li):
                                if ele =="B" or ele =="E" or ele =="Ü" or ele=="Ü]" or ele=="[|" or ele=="D" or ele=="b" or ele=="ü":
                                    save.append(count+1)
                            time.sleep(5)
                            try:
                                answearQuestions(f"{li[save[0]]}")
                            except:
                                print(f"i couldn't Answear this Question so i pass it!")
                                pass
                        if not pyautogui.locateOnScreen(f"imgPC/Begin/V.png", confidence=0.9):
                            try:
                                check_click("Begin/corn_long")
                            except:
                                try:
                                    check_click("Begin/corn2")
                                except:
                                    pass
                            files = glob.glob('imgAn/*.jpg')
                            for f in files:
                                os.remove(f)
                            # time.sleep(4)
                            s=""
                            if len(save) > 1:
                                for i in li[save[1]:len(li)]:
                                    if i == ".":
                                        s += f"{i}* "
                                    else:
                                        s += f"{i} "
                                s_strip=s.strip()
                                s_new=s_strip.replace(" ", f"{backslash}")
                                print(f"save is : {s_new}")
                                answearQuestions(f"{s_new}")
                            check_click("Begin/confirm")
                            try:
                                check_click("Begin/continue")
                            except:
                                check_click("Begin/continue2")
            save.clear()
    elif pyautogui.locateOnScreen(f"imgPC/Begin/wr.png", confidence=0.9):
        time.sleep(7)
        check_click("Begin/wr")
        time.sleep(4)
        check_click("Begin/continue")
        time.sleep(4)
        check_click("Begin/confirm")
        time.sleep(4)
        check_click("Begin/min-confirm")
        time.sleep(4)
        check_click("Begin/continue")
        time.sleep(4)
        check_click("Begin/main")
        time.sleep(3)
    else:
        # time.sleep(6)
        try:
            check_click("Begin/main")
            return "Done"
        except:
            return "Done"

def all(num):
    # matnsach dir while hna
    check_click(num)
    while True:
        row=rows_click()
        while True:
            check = ex()
            if check == "Done":
                break
        if row is False:
            break
        time.sleep(8)
        

def run():
    i=0
    while True:
        if pyautogui.locateOnScreen(f"imgPC/Pone.png", confidence=0.9):
            all("Pone")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Ptwo.png", confidence=0.9):
            all("Ptwo")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Pthree.png", confidence=0.9):
            all("Pthree")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Pfour.png", confidence=0.9):
            all("Pfour")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Pfive.png", confidence=0.9):
            all("Pfive")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Psix.png", confidence=0.9):
            all("Psix")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Pseven.png", confidence=0.9):
            all("Pseven")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Peight.png", confidence=0.9):
            all("Peight")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Pnine.png", confidence=0.9):
            all("Pnine")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Pten.png", confidence=0.9):
            all("Pten")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Peleven.png", confidence=0.9):
            all("Peleven")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Ptwelve.png", confidence=0.9):
            all("Phtwelve")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Pthirteen.png", confidence=0.9):
            all("Pthirteen")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Pfourteen.png", confidence=0.9):
            all("Pfourteen")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Pfiveteen.png", confidence=0.9):
            all("Pfiveteen")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Psixteen.png", confidence=0.9):
            all("Psixteen")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Pseventeen.png", confidence=0.9):
            all("Pseventeen")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Peightteen.png", confidence=0.9):
            all("Peightteen")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Pnineteen.png", confidence=0.9):
            all("Pnineteen")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Ptwenty.png", confidence=0.9):
            all("Ptwenty")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Ptwentyone.png", confidence=0.9):
            all("Ptwentyone")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Ptwentytwo.png", confidence=0.9):
            all("Ptwentytwo")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Ptwentythree.png", confidence=0.9):
            all("Ptwentythree")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Ptwentyfour.png", confidence=0.9):
            all("Ptwentyfour")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Ptwentysix.png", confidence=0.9):
            all("Ptwentysix")
            break
        elif pyautogui.locateOnScreen(f"imgPC/Ptwentyseven.png", confidence=0.9):
            all("Ptwentyseven")
            break
        else:
            end=pyautogui.locateOnScreen(f"imgPC/END.png", confidence=0.9)
            pyautogui.moveTo(end.left, end.top,0.5)
            pyautogui.click(end)
            i+=1
            if i == 3:
                break     