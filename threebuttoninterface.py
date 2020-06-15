from tkinter import *
import time,datetime
import mysql.connector as mc
from tkinter import messagebox
import cv2
import matplotlib.pyplot as  plt
import sys



def Camera():

    try:
       conn = mc.connect(host='localhost', user='root', password='', db='car_park_master')

    except mc.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)
        cursor = conn.cursor()
    cap = cv2.VideoCapture(0)

    x = StringVar()
    x = datetime.datetime.now()

    if cap.isOpened():
        ret, frame = cap.read()
        print(ret)
        print(frame)
    else:
        ret = False

    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    plt.imshow(img1)
    plt.title("Car Image")
    plt.xticks([])
    plt.yticks([])
    plt.show()

    cv2.imwrite("E:/pix/CarTemp.jpg", img1);

def billCalc():
    global EntryTime
    EntryTime =datetime.date.today()

    try:
       conn = mc.connect(host='localhost', user='root', password='', db='car_park_master')

    except mc.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM user")
        record = cursor.fetchall()
        for x in record:
            if (temp.get()) == (x[0]):
                EntryTime = x[1]


    print(EntryTime)
    conn.close()

    #BillTim = EntryTime - exitTime
    #Bill = BillTim * 2
    #messagebox.showinfo(title="BILL",message=Bill.get())



def exitGate():
    global temp
    global exitTime

    temp = StringVar()

    screenExit = Tk()
    screenExit.geometry("300x400")
    screenExit.title("EXIT GATE")
    messagebox.showinfo(title=None,message="Please press the exit button to get your bill")
    exitTime = datetime.datetime.now()

    Label(screenExit,text="Enter User ID:").place(x=50,y=200)
    Entry(screenExit,textvariable=temp).place(x=150,y=200)
    Button(screenExit,text="Go",height='2',width='15',command=billCalc).place(x=150,y=300)







def setCar():


    try:
        conn = mc.connect(host='localhost', user='root', password='', db='car_park_master')

    except mc.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)



    type='C'



    pram = (datetime.datetime.now(),type)

    sql_insert_query = """ INSERT INTO user
                              ( entry_time,`type`) VALUES (%s,%s)"""
    cursor = conn.cursor()


    result = cursor.execute(sql_insert_query, pram)
    conn.commit()
    cursor.close()
    conn.close()


    Camera()



    messagebox.showinfo(title=None,message="Gate is open now")

    exitGate()





def setMotor():
    try:
        conn = mc.connect(host='localhost', user='root', password='', db='car_park_master')

    except mc.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)

    type = 'M'

    pram = ( datetime.datetime.now(), type)

    sql_insert_query = """ INSERT INTO user
                              ( entry_time,`type`) VALUES (%s,%s)"""
    cursor = conn.cursor()

    result = cursor.execute(sql_insert_query, pram)
    conn.commit()
    cursor.close()
    conn.close()

    Camera()

    messagebox.showinfo(title=None, message="Gate is open now")

def setVan():
    try:
        conn = mc.connect(host='localhost', user='root', password='', db='car_park_master')

    except mc.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)

    type = 'V'

    pram = ( datetime.datetime.now(), type)

    sql_insert_query = """ INSERT INTO user
                              ( entry_time,`type`) VALUES (%s,%s)"""
    cursor = conn.cursor()

    result = cursor.execute(sql_insert_query, pram)
    conn.commit()
    cursor.close()
    conn.close()

    Camera()

    messagebox.showinfo(title=None, message="Gate is open now")








def main_screen():
    global userid


    screen = Tk()
    screen.geometry("300x400")
    screen.title("TYPE BUTTON INTERFACE")

    Label(text="PARKING SYSTEM",fg="black").place(x=100,y=20)


    Label(text="Please select the type of your vehicle and wait for the card",fg="Black").place(x=100,y=80)

    id = 0




    Button(text="Car", fg="black",bg="blue",command=setCar).place(x=100,y=140)
    Button(text="Motor Bike",fg="black",bg="red",command=setMotor).place(x=100,y=200)
    Button(text="Van",fg="black",bg="green",command=setVan).place(x=100,y=260)
    Label(text="User ID:", fg="Black").place(x=100,y=300)
    userid=StringVar()
    Entry(screen,textvariable=userid).place(x=150,y=300)

    screen.mainloop()




main_screen()