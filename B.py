from tkinter import *
import time,datetime
import mysql.connector as mc
from tkinter import messagebox
import cv2
import matplotlib.pyplot as  plt
import sys
import time



def Camera():
    global timestampStr
    cap = cv2.VideoCapture(0)

    x = StringVar()
    x= datetime.datetime.now()

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

    datetime_obj = datetime.datetime.now()

    timestampStr = datetime_obj.strftime("%d%b%Y_%H_%M_%S_%f")


    cv2.imwrite("C:/Users/Fahim/PycharmProjects/CarPark/" +timestampStr+ ".jpg", img1);
    return timestampStr

def ExitVar():
    global f
    f = StringVar()
    ScreenBill = Tk()
    ScreenBill.geometry("300x400")
    ScreenBill.title("EXIT GATE")
    Entry(ScreenBill, textvariable=f).place(x=150, y=200)

    print(f.get())
    return f

def billCalc():

    global srstr
    srstr = StringVar()
    srstr = ExitVar()
    print(srstr.get())

    global EntryTime
    try:
        conn = mc.connect(host='localhost', user='root', password='', db='car_park_master')

    except mc.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM user")
        record = cursor.fetchall()
        for x in record:
            if (srstr.get() == x[0]):
                EntryTime == x[2]

    print(EntryTime)
    conn.close()

    BillTim = EntryTime - exitTime
    Bill = BillTim * 2
    messagebox.showinfo(title="BILL",message=Bill.get())




def exitGate():

    global exitTime



    screenExit = Tk()
    screenExit.geometry("300x400")
    screenExit.title("EXIT GATE")
    messagebox.showinfo(title=None,message="Please press the exit button to get your bill")
    exitTime = datetime.datetime.now()

    Button(screenExit,text="Exit",height='2',width='15',command=billCalc).place(x=150,y=300)








def setCar():


    try:
        conn = mc.connect(host='localhost', user='root', password='', db='car_park_master')

    except mc.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)



    type='C'
    picturename = Camera()
    pram = (datetime.datetime.now(),type,picturename)

    sql_insert_query = """ INSERT INTO user
                              ( entry_time,`type`,`picture`) VALUES (%s,%s,%s)"""
    cursor = conn.cursor()


    result = cursor.execute(sql_insert_query, pram)
    conn.commit()
    cursor.close()
    conn.close()





    messagebox.showinfo(title=None,message="Gate is open now")







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


    screen = Tk()
    screen.geometry("300x400")
    screen.title("TYPE BUTTON INTERFACE")

    Label(text="PARKING SYSTEM",fg="black").place(x=100,y=20)


    Label(text="Please select the type of your vehicle and wait for the card",fg="Black").place(x=100,y=80)

    id = 0




    Button(text="Car", fg="black",bg="blue",command=setCar).place(x=100,y=140)
    Button(text="Motor Bike",fg="black",bg="red",command=setMotor).place(x=100,y=200)
    Button(text="Van",fg="black",bg="green",command=setVan).place(x=100,y=260)


    screen.mainloop()




main_screen()