import keyboard
import time

stri = "Nous supposons qu'ils B veulent (vouloir) nous faire une surprise."
s=stri.split(" ")
o =[]
for i in s:
    if i.find("(")!=-1:
        o.append(i)
print(o)
