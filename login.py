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
        if(username.get()==x[0]):
            print("Username correct")
            if(password.get()==x[1]):
                print("Success")


        else:
            print("Incorrect Password/Username")
    cursor.close()
    conn.close()
    print(username.get())
    print(password.get())



def main_screen():

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


        Button(text="Login",height = "2",width = "15",command=lambda :login()).place(x=100,y=200)

        screen.mainloop()

main_screen()




