from tkinter import *



def register():
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

    pram= (aa.get() , ab.get() , ac.get() , ad.get() , af.get())

    sql_insert_query = """ INSERT INTO permanent_user_info
                              (ID, name, address, phone,`car_plate`) VALUES (%s,%s,%s,%s,%s)"""
    cursor = conn.cursor()


    result = cursor.execute(sql_insert_query, pram)
    conn.commit()
    cursor.close()
    conn.close()





def main_screen():
    screen=Tk()
    screen.geometry("300x400")
    screen.title("Permanent User Registration Form")


    Label(text="ID", font=("Calibri", 16)).place(x=100, y=20)
    Label(text="FULL NAME", font=("Calibri", 16)).place(x=100, y=80)
    Label(text="Address", font=("Calibri", 16)).place(x=100, y=140)
    Label(text="Phone Number", font=("Calibri", 16)).place(x=100, y=200)
    Label(text="Plate Number", font=("Calibri",16)).place(x=100,y=260)


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

    Entry(textvariable=aa).place(x=100, y=50)
    Entry(textvariable=ab).place(x=100, y=110)
    Entry(textvariable=ac).place(x=100, y=170)
    Entry(textvariable=ad).place(x=100, y=230)
    Entry(textvariable=af).place(x=100, y=290)






    Button(text="Register", height="2", width="15", command=register).place(x=100, y=350)




    screen.mainloop()

main_screen()
