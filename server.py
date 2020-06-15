from tkinter import *
import time,datetime
import mysql.connector as mc









def setCar():



    try:
        conn = mc.connect(host='localhost', user='root', password='', db='car_park_master')

    except mc.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)



    type='C'


    pram = (datetime.datetime.now(),type)




    sql_insert_query = """ INSERT INTO user
                              ( `user_id`,`entry_time`,`type`) VALUES (%s,%s.%s)"""
    cursor = conn.cursor()

    result = cursor.execute(sql_insert_query, pram)
    conn.commit()
    cursor.close()
    conn.close()






def setMotor():
    try:
        conn = mc.connect(host='localhost', user='root', password='', db='car_park_master')

    except mc.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)

    type = 'M'



    pram = (datetime.datetime.now(), type)


    sql_insert_query = """ INSERT INTO user
                              ( `user_id``entry_time`,`type`) VALUES (%s,%s,%s)"""
    cursor = conn.cursor()

    result = cursor.execute(sql_insert_query, pram)
    conn.commit()
    cursor.close()

    conn.close()

def setVan():
    try:
        conn = mc.connect(host='localhost', user='root', password='', db='car_park_master')

    except mc.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)

    type = 'V'

    pram = ( datetime.datetime.now(), type)

    sql_insert_query = """ INSERT INTO user
                              ( `entry_time`,`type`) VALUES (%s,%s)"""
    cursor = conn.cursor()

    result = cursor.execute(sql_insert_query, pram)
    conn.commit()
    cursor.close()
    conn.close()






def main_screen():
    global userid

    userid = ['0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009', '0010']

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
