import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="sneha123",
    database="cab"
    )
mycursor=mydb.cursor()
#mycursor.execute("CREATE DATABASE Cab")
#mycursor.execute("CREATE TABLE user(Name VARCHAR(200),Email_address VARCHAR(200),Age INTEGER(10),Username VARCHAR(200) PRIMARY KEY,Password VARCHAR(200),Confirm_password VARCHAR(200))")
#mycursor.execute("CREATE TABLE booking(name VARCHAR(200),age INTEGER(10),gender VARCHAR(200),location VARCHAR(200),schedule_time VARCHAR(200),phone int(12))")
#mycursor.execute("CREATE TABLE drivers(name VARCHAR(200),age INTEGER(10),gender VARCHAR(200),location VARCHAR(200),phone int(12), car_no VARCHAR(200))")
import tkinter
from tkinter import *
from tkinter import messagebox



def init_login_screen(master):
    master = master
    master.title("Book Your Cab")
    master.geometry('600x600') #size of box
    master.configure(background="#F4C2C2")

    l=Label(master,text="LOG IN TO YOUR ACCOUNT",font=("bold"))
    l.place(x=130,y=110) #distance from box boundry

    l1=Label(master,text="Username")
    l1.place(x=150,y=200)

    e1=Entry(master)
    e1.place(x=220,y=200)

    l2=Label(master,text="Password")
    l2.place(x=150,y=250)

    e2=Entry(master,show="*")
    e2.place(x=220,y=250)

    logbutton=Button(master,text="LOG IN",fg="blue",bg="pink",command=lambda:login(e1.get(),e2.get(),master)).place(x=250,y=300,width=70)
    clearbutton=Button(master,text="Exit",fg="blue",bg="pink",command=lambda:clr(master)).place(x=250,y=350,width=70)

def login(a,b,master):
    a =a
    b =b
    if(a=="carbooking" and b=="car123"):
       master.destroy()
       root  = Tk()
       loggui = init_Welcome(root)
    else:
        msg="Your Username and Passaword are incorrect"
        messagebox.showinfo("Access denied",msg)
def clr(master):
    master.destroy()
    # e1.delete(0,'end')
    # e2.delete(0,'end')


# class Welcome:
def init_Welcome(master):
    master = master
    master.geometry("600x600")
    master.title("Book Your Cab")
    master.configure(background="#F4C2C2")
    title=Label(master,text="Welcome to Book Your Cab",font=("Matura MT Script Capitals",22),bg="red",fg="black").place(x=100,y=50)
    book=Button(master,text="Cab Booking",bg="pink",fg="white",command=lambda:book1(master),width=30).place(x=200,y=100)
    reg=Button(master,text="Cab Registration",bg="pink",fg="white",command=lambda:reg2(master),width=30).place(x=200,y=150)
    info=Button(master,text="About",bg="pink",fg="white",command=info1,width=30).place(x=200,y=200)
    feed=Button(master,text="Feedback",bg="pink",fg="white",command=lambda:feed1(master),width=30).place(x=200,y=250)
    exit2=Button(master,text="Exit",bg="pink",fg="white",command=lambda:exit1(master),width=30).place(x=200,y=300)



def book1(master):
    master.destroy()
    root2=Tk()
    bookgui=init_application_screen(root2)

def reg2(master):
    master.destroy()
    root3=Tk()
    reggui=init_register(root3)

def info1():
    msg="About BOOK YOUR CAB SYSTEM"
    messagebox.showinfo(msg,"IT an system where you are book your cab")

def feed1(master):
    master.destroy()
    root4=Tk()
    feedgui=init_feed(root4)

def exit1(master):
    master.destroy()



def init_application_screen( master):
    master = master
    master.geometry("600x600")
    master.title("Book Your Cab")
    master.configure(background="#F4C2C2")

        # labels for the window
    title=Label(master,text="Book Your Cab",font=("Matura MT Script Capitals",22),bg="red",fg="black").place(x=100,y=50)

        #  name
    name = Label(master, text=" Name", font=(
            'georgia 18 bold'), fg='black', bg='grey')
    name.place(x=100, y=100)

        # age
    age = Label(master, text="Age", font=(
            'georgia 18 bold'), fg='black', bg='grey')
    age.place(x=100, y=150)

        # gender
    gender = Label(master, text="Gender", font=(
            'georgia 18 bold'), fg='black', bg='grey')
    gender.place(x=100, y=200)

        # location
    location = Label(master, text="Location", font=(
            'georgia 18 bold'), fg='black', bg='grey')
    location.place(x=100, y=250)

        # appointment time
    time = Label(master, text="Entry Time", font=(
            'georgia 18 bold'), fg='black', bg='grey')
    time.place(x=100, y=300)

        # phone
    phone = Label(master, text="Phone No", font=(
            'georgia 18 bold'), fg='black', bg='grey')
    phone.place(x=100, y=350)

        # Entries for all labels============================================================
    name_ent = Entry(master, width=30)
    name_ent.place(x=250, y=100)

    age_ent = Entry(master, width=30)
    age_ent.place(x=250, y=150)

    gender_ent = Entry(master, width=30)
    gender_ent.place(x=250, y=200)

    location_ent = Entry(master, width=30)
    location_ent.place(x=250, y=250)

    time_ent = Entry(master, width=30)
    time_ent.place(x=250, y=300)

    phone_ent = Entry(master, width=30)
    phone_ent.place(x=250, y=350)

        # button to perform a command
    submit = Button(master, text="Add Booking", width=20,
                             height=2, bg='white', command=lambda:add_appointment( name_ent.get(), age_ent.get(), gender_ent.get(), location_ent.get(), time_ent.get(), phone_ent.get()))
    submit.place(x=150, y=400)

    clear1 = Button(master, text="Exit", width=20,
                             height=2, bg='white', command="")
    clear1.place(x=150, y=450)

    back = Button(master, text="Back", width=20,
                             height=2, bg='white', command=lambda:back_appointment(master))
    back.place(x=150, y=500)


def add_appointment(val1,val2,val3,val4,val5,val6):
        # getting the user inputs
    val1 = val1
    val2 = val2
    val3 = val3
    val4 = val4
    val5 = val5
    val6 = val6

        # checking if the user input is empty
    if val1 == '' or val2 == '' or val3 == '' or val4 == '' or val5 == ''or val6=='':
        messagebox.showinfo("Warning", "Please Fill Up All Boxes")
    else:
        # now we add to the database
        messagebox.showinfo("Success", "Booking for " + str(val1) + " has been created")
       
def back_appointment(master):
    master.destroy()
    root5 = Tk()
    backland = init_Welcome(root5)


def init_register(master):
    master = master
    master.geometry("600x600")
    master.title("Book Your Cab")
    master.configure(background="#F4C2C2")
    title=Label(master,text="Register Your Car ",font=("Matura MT Script Capitals",22),bg="red",fg="black").place(x=100,y=50)
           #  name
    name = Label(master, text=" Owner Name", font=(
           'georgia 18 bold'), fg='black', bg='grey')
    name.place(x=100, y=100)
        # age
    age = Label(master, text="Age", font=(
            'georgia 18 bold'), fg='black', bg='grey')
    age.place(x=100, y=150)

         # gender
    gender = Label(master, text="Gender", font=(
             'georgia 18 bold'), fg='black', bg='grey')
    gender.place(x=100, y=200)

         # location
    location = Label(master, text="Location", font=(
             'georgia 18 bold'), fg='black', bg='grey')
    location.place(x=100, y=250)

         # phone
    phone = Label(master, text="Phone No", font=(
             'georgia 18 bold'), fg='black', bg='grey')
    phone.place(x=100, y=300)
    no = Label(master, text="Car No", font=(
             'georgia 18 bold'), fg='black', bg='grey')
    no.place(x=100, y=350)

         # Entries for all labels============================================================
    name_ent = Entry(master, width=30)
    name_ent.place(x=250, y=100)

    age_ent = Entry(master, width=30)
    age_ent.place(x=250, y=150)

    gender_ent = Entry(master, width=30)
    gender_ent.place(x=250, y=200)

    location_ent = Entry(master, width=30)
    location_ent.place(x=250, y=250)
    phone_ent = Entry(master, width=30)
    phone_ent.place(x=250, y=300)
    car_ent = Entry(master, width=30)
    car_ent.place(x=250, y=350)

         # button to perform a command
    submit = Button(master, text="Submit", width=20,
                              height=2, bg='white', command=lambda:add_car( name_ent.get(), age_ent.get(), gender_ent.get(), location_ent.get(), phone_ent.get(),car_ent.get()))
    submit.place(x=150, y=400)

    clear1 = Button(master, text="Clear", width=20,
                              height=2, bg='white', command=lambda:clear_car(master)) #    clear1.place(x=150, y=450)

    back = Button(master, text="Back", width=20,
                              height=2, bg='white', command=lambda:back_car(master))
    back.place(x=150, y=500)


def add_car(val1,val2,val3,val4,val5,val6):
         # getting the user inputs
    val1 = val1
    val2 = val2
    val3 = val3
    val4 = val4
    val5 = val5
    val6 = val6      
     # checking if the user input is empty
    if (val1 == '' or val2 == '' or val3 == '' or val4 == '' or val5 == '' or val6 == ''):
        messagebox.showinfo("Warning", "Please Fill Up All Boxes")
    else:
        messagebox.showinfo("Success", "Car got registered of" + str(val6) + " car no")
         # now we add to the database
        ''' sql = "INSERT INTO 'drivers' (name, age, gender, location, phone, car_no) VALUES(?, ?, ?, ?, ?, ?)"
        mycursor.execute(sql, (val1, val2, val3, val4 , val5, val6))
        mycursur.close()
        messagebox.showinfo(
             "Success", "Your Car number " + str(val5) + " is registered")'''

def clear_car(master):
    master.destroy()
def back_car(master):
    master.destroy()
    root5 = Tk()
    backland = init_Welcome(root5)

def init_feed(master):
    master = master
    master.geometry("600x600")
    master.title("Book Your Cab")
    master.configure(background="#F4C2C2")
    title=Label(master,text="Feedback ",font=("Matura MT Script Capitals",22),bg="red",fg="black").place(x=100,y=50)
    fed = Entry(master,width=70)
    fed.place(x=100,y=100)
    button = Button(master,width=20,text="Submit" ,height=2, bg='white',command=lambda:feedback(fed.get()))
    button.place(x=100,y=250)
    button1 = Button(master,width=20,text="Exit", height=2, bg='white',command=lambda:clearback(master))
    button1.place(x=100,y=300)
    button2 = Button(master,width=20,text="Back", height=2, bg='white',command=lambda:back(master))
    button2.place(x=100,y=350)
def feedback(feedback1):
    feedback1=feedback1
    file=open("feedback.txt","a")
    file.write(feedback1)
    file.close()
def clearfeed(master):
    master.destroy()
def back(master):
    master.destroy()
    root5 = Tk()
    backland = init_Welcome(root5)



def main():
 root = Tk()
 welcomegui = init_login_screen(root)
 root.mainloop()

if __name__=="__main__":
    main()
