from tkinter import *
import time,datetime

root =Tk()

def setCar():
    type = 'C'
    tim = datetime.datetime.now()
    print(type,tim)






def setMotor():
    type = 'M'
    tim = datetime.datetime.now()
    print(type,tim)

def setVan():
    type = 'V'
    tim = datetime.datetime.now()
    print(type,tim)







TopFrame = Frame(root)
TopFrame.pack()
BottomFrame = Frame(root)
BottomFrame.pack(side=BOTTOM)

Label1=Label(TopFrame,text="PARKING SYSTEM",fg="black")
Label1.pack(fill=X)

Label2=Label(TopFrame,text="Please select the type of your vehicle and wait for the card",fg="Black")
Label2.pack(fill=X)

button1= Button(BottomFrame, text="Car", fg="black",bg="blue",command=setCar)
button2= Button(BottomFrame,text="Motor Bike",fg="black",bg="red",command=setMotor)
button3= Button(BottomFrame,text="Van",fg="black",bg="green",command=setVan)

button1.pack(side=RIGHT,fill=X)
button2.pack(side=RIGHT,fill=X)
button3.pack(side=RIGHT,fill=X)




root.mainloop()
