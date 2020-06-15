import socket
from tkinter import *
import time,datetime






HOST='127.0.0.1'
PORT = 1024





root =Tk()


def setCar():
    data = 'C'
    tim = datetime.datetime.now()
    print(type,tim)
    time.strftime("%S")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        s.sendto(b"5",(HOST,PORT))


def setMotor():
    type = 'M'
    tim = datetime.datetime.now()
    print(type,tim)
    s.send(1024)

def setVan():
    type = 'V'
    tim = datetime.datetime.now()
    print(type,tim)

    s.send(1024)







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
