from tkinter import *

def login():
    import sys
    import mysql.connector as mc

    try:
        conn = mc.connect(host='localhost',user='root',password='',db='car_park_master')

    except mc.Error as e:
        print("Error %d: %s" %(e.args[0],e.args[1]))
        sys.exit(1)
    cursor= conn.cursor()

    cursor.execute("SELECT * FROM admin")
    record = cursor.fetchall()
    for x in record:
        if((username.get()==x[0]) and (password.get()==x[1])):
            print("Username correct")
            screen.destroy()
            global screen2
            print("Success")
            global screen2
            screen2 = Tk()
            screen2.geometry("300x250")
            screen2.title("Admin Panel")
            Button(screen2,text="Register User", height="2", width="15", command=register).place(x=100, y=200)


        else:
            print("Incorrect Password/Username")
    cursor.close()
    conn.close()
    print(username.get())
    print(password.get())

def register():
    screen2.destroy()
    global screen3
    screen3 = Tk()
    screen3.geometry("300x400")
    screen3.title("Permanent User Registration Form")

    Label(screen3,text="ID", font=("Calibri", 16)).place(x=100, y=20)
    Label(screen3,text="FULL NAME", font=("Calibri", 16)).place(x=100, y=80)
    Label(screen3,text="Address", font=("Calibri", 16)).place(x=100, y=140)
    Label(screen3,text="Phone Number", font=("Calibri", 16)).place(x=100, y=200)
    Label(screen3,text="Plate Number", font=("Calibri", 16)).place(x=100, y=260)

    global aa
    global ab
    global ac
    global ad
    global af

    aa = StringVar()
    ab = StringVar()
    ac = StringVar()
    ad = StringVar()
    af = StringVar()

    Entry(screen3,textvariable=aa).place(x=100, y=50)
    Entry(screen3,textvariable=ab).place(x=100, y=110)
    Entry(screen3,textvariable=ac).place(x=100, y=170)
    Entry(screen3,textvariable=ad).place(x=100, y=230)
    Entry(screen3,textvariable=af).place(x=100, y=290)

    Button(screen3,text="Register", height="2", width="15", command=registeruser).place(x=100, y=350)

def registeruser():

    print(aa.get())
    print(ab.get())
    print(ac.get())
    print(ad.get())
    print(af.get())

    import sys
    import mysql.connector as mc

    try:
        conn = mc.connect(host='localhost', user='root', password='', db='car_park_master')

    except mc.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)

    pram = (aa.get(), ab.get(), ac.get(), ad.get(), af.get())

    sql_insert_query = """ INSERT INTO `permanent_user_info`
                                  (`ID`, `name`, `address`, `phone`,`car_plate`) VALUES (%s,%s,%s,%s,%s)"""
    cursor = conn.cursor()

    result = cursor.execute(sql_insert_query, pram)
    conn.commit()
    cursor.close()
    conn.close()


def main_screen():

        global screen

        screen = Tk()
        screen.geometry("300x250")
        screen.title("Admin Login")
        Label(text="USERNAME",font=("Calibri",16)).place(x=100,y=20)
        Label(text="PASSWORD", font=("Calibri", 16)).place(x=100, y=80)

        global username
        global password

        username = StringVar()
        password = StringVar()
        Entry(textvariable= username).place(x=100,y=50)
        Entry(textvariable= password).place(x=100,y=110)


        Button(text="Login",height = "2",width = "15",command=login).place(x=100,y=200)

        screen.mainloop()

main_screen()




