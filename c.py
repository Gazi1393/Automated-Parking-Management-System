from tkinter import *
import datetime
import mysql.connector as mc
from tkinter import messagebox
import cv2
import matplotlib.pyplot as  plt
import sys
import time


def billCalc():
    global exitTime
    global EntryTime
    EntryTime = datetime.datetime
    exitTime = datetime.datetime.now()
    try:
        conn = mc.connect(host='localhost', user='root', password='', db='car_park_master')

    except mc.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)

    cursor = conn.cursor()

    cursor.execute("SELECT entry_time FROM user where user_id=" + f.get())
    record = cursor.fetchone()
    EntryTime = (record[0])

    conn.close()
    print(exitTime)
    print(EntryTime)
    print(f.get())

    BillTime = exitTime - EntryTime

    print(BillTime)


def main_screen():
    screen = Tk()
    screen.geometry("300x400")
    screen.title("EXIT GATE")

    global f
    f = StringVar()

    Entry(screen, textvariable=f).place(x=150, y=200)

    print(f.get())

    Button(screen, text="Exit", height='2', width='15', command=billCalc).place(x=150, y=300)
    screen.mainloop()


main_screen()