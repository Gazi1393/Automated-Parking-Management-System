
from tkinter import *
from tkinter import messagebox
import mysql.connector as mc

def searchdb():
    screen6.destroy()
    screen5 = Tk()
    screen5.geometry("1086x1024")
    screen5.title("Admin Panel/User/Search Results")

    try:
        conn = mc.connect(host='localhost', user='root', password='', db='car_park_master')

    except mc.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    record = cursor.fetchall()


    for x in record:
        if(searchx.get() == x[0]):
            Label(screen5, text="ID", font=("Calibri", 8)).place(x=20, y=5)
            Label(screen5, text=(x[0]), font=("Calibri", 8)).place(x=20, y=5)
            Label(screen5, text="Entry_time", font=("Calibri", 8)).place(x=40, y=5)
            Label(screen5, text=(x[1]), font=("Calibri", 8)).place(x=40, y=5)
            Label(screen5, text="Exit_time", font=("Calibri", 8)).place(x=200, y=5)
            Label(screen5, text=(x[2]), font=("Calibri", 8)).place(x=200, y=5)
            Label(screen5, text="Type", font=("Calibri", 8)).place(x=400, y=5)
            Label(screen5, text=(x[3]), font=("Calibri", 8)).place(x=400, y=5)
            Label(screen5, text="Photo", font=("Calibri", 8)).place(x=600, y=5)
            Label(screen5, text=(x[4]), font=("Calibri", 8)).place(x=600, y=5)
            Label(screen5, text="Bill", font=("Calibri", 8)).place(x=800, y=5)
            Label(screen5, text=(x[5]), font=("Calibri", 8)).place(x=800, y=5)
            print(x[0])
            print(x[1])
            print(x[2])
            print(x[3])
            print(x[4])
            print(x[5])


        else:
            print("No match")




def permanent_table():
    screen2.destroy()
    global screen6
    screen6 = Tk()
    screen6.geometry("1086x1024")
    screen6.title("Admin Panel/User Table")
    Button(screen6, text="Back", height="2", width="9", command=back).place(x=1000, y=900)
    try:
        conn = mc.connect(host='localhost', user='root', password='', db='car_park_master')

    except mc.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM permanent_user_info")
    record = cursor.fetchall()
    b = 20

    for x in record:
        Label(screen6, text="ID", font=("Calibri", 8)).place(x=20, y=5)
        Label(screen6, text=(x[0]), font=("Calibri", 8)).place(x=20, y=b)
        b = b + 20

    b = 20
    for x in record:
        Label(screen6, text="Name", font=("Calibri", 8)).place(x=40, y=5)
        Label(screen6, text=(x[1]), font=("Calibri", 8)).place(x=40, y=b)
        b = b + 20
    b = 20
    for x in record:
        Label(screen6, text="Address", font=("Calibri", 8)).place(x=200, y=5)
        Label(screen6, text=(x[2]), font=("Calibri", 8)).place(x=200, y=b)
        b = b + 20
    b = 20
    for x in record:
        Label(screen6, text="Phone", font=("Calibri", 8)).place(x=400, y=5)
        Label(screen6, text=(x[3]), font=("Calibri", 8)).place(x=400, y=b)
        b = b + 20
    b = 20
    for x in record:
        Label(screen6, text="Car Plate", font=("Calibri", 8)).place(x=600, y=5)
        Label(screen6, text=(x[4]), font=("Calibri", 8)).place(x=600, y=b)
        b = b + 20
    b = 20
    for x in record:
        Label(screen6, text="Due", font=("Calibri", 8)).place(x=800, y=5)
        Label(screen6, text=(x[5]), font=("Calibri", 8)).place(x=800, y=b)
        b = b + 20
    cursor.close()
    conn.close()




def user_table():


    screen2.destroy()

    global screen6
    global searchx






    screen6 = Tk()
    screen6.geometry("1086x1024")
    screen6.title("Admin Panel/User Table")
    Button(screen6,text="Back", height="2", width="9", command=back).place(x=1000, y=900)
    searchx = StringVar()
    Entry(screen6, textvariable=searchx).place(x=500, y=900)
    Button(screen6,text="Search",height="2",width="9",command=searchdb).place(x=700,y=900)



    try:
        conn = mc.connect(host='localhost', user='root', password='', db='car_park_master')

    except mc.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)

    cursor=conn.cursor()
    cursor.execute("SELECT * FROM user")
    record = cursor.fetchall()
    b=20

    for x in record:
        Label(screen6,text="ID",font=("Calibri",8)).place(x=20,y=5)
        Label(screen6,text=(x[0]),font=("Calibri",8)).place(x=20,y=b)
        b=b+20

    b=20
    for x in record:
        Label(screen6, text="Entry_time", font=("Calibri", 8)).place(x=40, y=5)
        Label(screen6, text=(x[1]), font=("Calibri", 8)).place(x=40, y=b)
        b = b + 20
    b = 20
    for x in record:
        Label(screen6, text="Exit_time", font=("Calibri", 8)).place(x=200, y=5)
        Label(screen6, text=(x[2]), font=("Calibri", 8)).place(x=200, y=b)
        b = b + 20
    b = 20
    for x in record:
        Label(screen6, text="Type", font=("Calibri", 8)).place(x=400, y=5)
        Label(screen6, text=(x[3]), font=("Calibri", 8)).place(x=400, y=b)
        b = b + 20
    b = 20
    for x in record:
        Label(screen6, text="Photo", font=("Calibri", 8)).place(x=600, y=5)
        Label(screen6, text=(x[4]), font=("Calibri", 8)).place(x=600, y=b)
        b = b + 20
    b = 20
    for x in record:
        Label(screen6, text="Bill", font=("Calibri", 8)).place(x=800, y=5)
        Label(screen6, text=(x[5]), font=("Calibri", 8)).place(x=800, y=b)
        b = b + 20
    cursor.close()
    conn.close()



def back():
    screen6.destroy()
    login()




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


    screen.destroy()

    for x in record:
        if((username.get()==x[0]) and (password.get()==x[1])):
            print("Username correct")
            print("Success")

            global screen2
            screen2 = Tk()
            screen2.geometry("1080x1024")
            screen2.title("Admin Panel")
            Button(screen2,text="Register User", height="8", width="60", command=register).place(x=512, y=500)
            Button(screen2, text="User Table", height="8", width="60", command=user_table).place(x=512, y=700)
            Button(screen2, text="Permanent User", height="8", width="60", command=permanent_table).place(x=512, y=900)


        #else:
            #messagebox.showinfo(title="Error",message="Incorrect username or password")
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
    global aa
    global ab
    global ac
    global ad
    global af

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

    sql_insert_query = """ INSERT INTO permanent_user_info
                                  (ID, name, address, phone,`car_plate`) VALUES (%s,%s,%s,%s,%s)"""
    cursor = conn.cursor()

    result = cursor.execute(sql_insert_query, pram)
    conn.commit()
    cursor.close()
    conn.close()




def main_screen():

        global count
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