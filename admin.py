from tkinter import *

root=Tk()


class AdminForm(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('PARKING MANAGEMENT : ADMIN PANEL')
        self.geometry('600x500')
        container= Frame(root)
        container.winfo_geometry('200x200')
        container.pack()
        self.Frames= {
            'Admin Registration' : AdminReg(self),
            'Login' : AdminLogin(self)

        }

    def show_frame(self, name):
        frame = self.frames[name]
        frame.place(width=500, height=600, relx=0.5, rely=0.5, anchor=CENTER)
        frame.tkraise()
        c=Button(container,text="get started",command=show_frame)
        b=Button(container,text="Registration Form", command= show_reg_frame)
        c.pack()
        a.pack()
        b.pack()


    def show_reg_frame(self):
        self.show_frame('Admin Registration')
    def show_login_frame(self):
        self.show_frame('Login')

class AdminReg(Frame):
    def __init__(self,form ):
        Frame.__init__(self,form)
        Label(self, text='Admin Registration Form').grid(row=0,column=0)

class AdminLogin(Frame) :
    def __init__(self,form):
        Frame.__init__(self,form)
        Label(self, text='Login form').grid(row=2,column=2)


if __name__ == "__main__" :
 f1=AdminForm()
 f1.mainloop()

