#import distutils
#import curses
#from curses import *

from distutils.util import execute
from asyncio import subprocess
from cProfile import label
from tkcalendar import *
from distutils.util import execute
from email.mime import image
from sre_parse import *
from sys import stderr, stdin, stdout
from tkinter import *
from tkinter import PhotoImage
from tkinter import ttk, messagebox as msg
import tkinter
from turtle import right, title
from webbrowser import get
import MySQLdb as mdb
import mysql.connector
from PIL import ImageTk,Image
from project_final import bca

a = Tk()
def clear():
    fname.delete(0,END)
    lname.delete(0,END)
    contact.delete(0,END)
    email.delete(0,END)
    quest.delete(0)
    answer.delete(0,END)
    password.delete(0,END)
    cpassword.delete(0,END)

def next():
    top= Toplevel()    
    #c=Tk()
    top.title("Courses")
    top.maxsize(1550,860)
    top.minsize( 1550,860)
    top.config(bg="white")

#==bg image===
#img1=Image.open("i3.jpg").resize((1550,860))
    img1=Image.open("cor.jpg").resize((1550,860))
    test=ImageTk.PhotoImage(img1)
    lab1=tkinter.Label(image=test)
    lab1.pack()

    frame1=Frame(bg="gray")
    frame1.place(x=400,y=150,width=800,height=500)

#===label text===
    l=Label(top,text="Available Courses", font=("times new roman", 30, "bold"), bg="pink", fg="green")
    l.place(x=650,y=40)

#===BCA===
    b = Button(top,text="BCA", font=( "times new roman", 20, "bold"),width=20,command=bca,cursor="hand2", bg="yellow", fg="red").place(x=430, y=230)

#=== MCA===
    #mca=StringVar()
    b2 = Button(top,text="MCA", font=("times new roman", 20, "bold"), width=20, bg="yellow", fg="red", command=mca).place(x=830, y=230)

#===BBA===
    #bba=StringVar()
    b3 = Button(top,text="BBA", font=( "times new roman", 20, "bold"),width=20, bg="yellow", fg="red", command=bba).place(x=430, y=330)

#====MBA===
    #mba=StringVar()
    b4 = Button(top, text="MBA", font=("times new roman", 20, "bold"), width=20,bg="yellow", fg="red", command=mba).place(x=830, y=330)
    
    #=== fac==
    b5= Button(top, text="faculty", font=("times new roman", 20, "bold"), width=45,bg="yellow", fg="red", command=fac).place(x=430, y=430)
    top.group(window)
    top.mainloop()

def fac():
    n=Tk()
    n.minsize(1450,900)
    n.title("Faculty Management")

#==bg image===
    i=Image.open("book.jpg").resize((1550,900))
    test=ImageTk.PhotoImage(i)
    lab1=tkinter.Label(image=test)
    lab1.pack()
    l1=Label(a,text="Faculty", font=("times new roman", 30, "bold"), bg="white", fg="red").place(x=680,y=38)
    
#===main img==
    i2=Image.open("fac.jpg").resize((750,650))
    test1=ImageTk.PhotoImage(i2)
    lab2=tkinter.Label(image=test1)
    lab2.place(x=420, y=80)
    n.mainloop()


def mca():
    a=Tk()
    a.minsize( 1550,860)
    a.config(bg="gray")
    img1=Image.open("mca.jpg").resize((650,750))
    test=ImageTk.PhotoImage(img1)
    lab1=tkinter.Label(image=test)
    lab1.place(x=450, y=22)
    a.mainloop()

#=bba
def bba():
    a=Tk()
    a.minsize( 1550,860)
    a.config(bg="gray")
    img1=Image.open("bba.jpg").resize((650,750))
    test=ImageTk.PhotoImage(img1)
    lab1=tkinter.Label(image=test)
    lab1.place(x=440, y=22)
    a.mainloop()


#==mba
def mba():
    a=Tk()
    a.minsize( 1550,860)
    a.config(bg="gray")
    img1=Image.open("mba.jpg").resize((750,750))
    test=ImageTk.PhotoImage(img1)
    lab1=tkinter.Label(image=test)
    lab1.place(x=420, y=22)
    a.mainloop()

#=attendance

def attend():
    a=Tk()
    a.title("Attendance Submission")
    a.minsize(1550,900)
    def clear1():
        v_cls.delete(0,END)
        v_sub.delete(0,END)
        v_rno.delete(0,END)
        v_cal.delete(1,END)
    
    def data1():
        if v_cls.get()=="choose class" or v_sub.get()=="choose subject" or v_rno.get()=="":
            msg.showerror("error", "All fields are manadatory",parent=a)
        else:   
            print(v_cls.get(),v_sub.get(),v_rno.get(), v_cal.get())
            msg.showinfo("great", "Successfully Registered")

            conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="Pri@1234"
            )
            print(conn)
            cur=conn.cursor()
            cur.execute("use pri")
            cur.execute("insert into st_record(class, subject, r_no, cal) values (%s,%s,%s,%s)",
                (
                v_cls.get(), v_sub.get(),v_rno.get(),v_cal.get()
                ))
            conn.commit()
            print(cur.rowcount, "record inserted")
        conn.close()    
    #    clear()
     
#==bg image===
    i=Image.open("attendance.png").resize((1260,700))
    test=ImageTk.PhotoImage(i)
    lab1=tkinter.Label(image=test)
    lab1.pack()
    l1=Label(a,text="Attendance Form", font=("times new roman", 30, "bold"), bg="white", fg="green").place(x=550,y=40)

#====class select==
    v_cls=StringVar()
    cls=ttk.Combobox(a,width=40, font=("times new roman", 15, "bold"),textvariable=v_cls)
    cls['state']='readonly'
    cls['values']=("choose class ","bca1","bca 2","bca 3", "mca 1", "mca 2", "mca 3", "bba 1", "bba 2", "bba 3", "mba 1", "mba 2", "mba 3")
    cls.current(0)
    cls.place(x=50,y=150)

#===subject choose===
    v_sub=StringVar()
    sub=ttk.Combobox(a,width=40, font=("times new roman", 15, "bold"),textvariable=v_sub)
    sub['state']='readonly'
    sub['values']=("choose Subject","Java","Web-Tech","Operating System","Cyber Security","Python","HTML", "Bussiness organisation", "bussiness managemnt", "Bussiness Communications", "HR", "Financial")
    sub.current(0)
    sub.place(x=750,y=150)

#== date===
    v_cal=StringVar()
    cal=DateEntry(a ,width=40, font=("times new roman" , 15,"bold"))
    cal.insert(0,"Date")
    cal.place(x=50,y=250)

#===attendence absent===
    v_rno=IntVar()
    l2=Label(a,text="Enter roll no. of absentees",width=40, font=("times new roman", 15, "bold")).place(x=750, y=250)
    e=Entry(a,width=40,font=("times new roman", 15, "bold"), bg="gray",textvariable=v_rno).place(x=750,y=280)

    bt=Button(a,text="Enter",font=("times new roman", 12, "bold")).place(x=50, y=350)
    bt2=Button(a,text="Submit", font=("times new roman", 12, "bold"),cursor="hand2", command= data).place(x=150, y=350)
    a.mainloop()

#resp
def resp():
    a=Tk()

    def clear():
        v_cls.delete(0,END)
        v_sub.delete(0,END)
       
    def data():
        if v_cls.get()=="select class" or v_sub.get()=="select subject" :
            msg.showerror("error", "All fields are manadatory",parent=a)
        else:
            print(v_cls.get(),v_sub.get())
            msg.showinfo("great", "Successfully respond")
        
            conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="Pri@1234"
            )
            print(conn)
            cur=conn.cursor()   
            cur.execute("use pri")
            cur.execute("select st_record.r_no from st_record where st_record.class='"+ v_cls.get() +"'&& st_record.subject= '"+v_sub.get()+"'")
            print("hey done") 
            cur.execute("select rno from st_record")
            cur.fetchone()
            print(cur)   
        #conn.commit()
            print(cur.rowcount, "record displayed")
        #conn.close()    
        
    a.minsize(1550,900)
    a.title("Attendance Response")

#==bg image===
    i=Image.open("clock.png").resize((1260,700))
    test=ImageTk.PhotoImage(i)
    lab1=tkinter.Label(image=test)
    lab1.pack()
    l1=Label(a,text="Attendance Response", font=("times new roman", 30, "bold"), bg="white", fg="red").place(x=550,y=40)

#====select class===
    v_cls=StringVar()
    cls=ttk.Combobox(a,width=40, font=("times new roman", 15, "bold"),textvariable=v_cls)
    cls['state']='readonly'
    cls['values']=("Select class ","bca1","bca 2","bca 3")
    cls.current(0)
    cls.place(x=50,y=150)

#===select subject==
    v_sub=StringVar()
    sub=ttk.Combobox(a,width=40, font=("times new roman", 15, "bold"),textvariable=v_sub)
    sub['state']='readonly'
    sub['values']=("Select Subject","Java","Web-Tech","Operating System","Cyber Security")
    sub.current(0)
    sub.place(x=750,y=150)

    cal=DateEntry(a ,width=40, font=("times new roman" , 15,"bold"))
    cal.insert(0,"Date")
    cal.place(x=50,y=250)

    l2=Label(a,text="roll no. of absentees:",width=40, font=("times new roman", 15, "bold")).place(x=50, y=300)
    e=Entry(a,width=40,font=("times new roman", 15, "bold"), bg="gray").place(x=50,y=340)

    bt=Button(a,text="Search",font=("times new roman", 14, "bold"),cursor="hand2", command=data).place(x=50, y=390)
    a.mainloop()




def data():
    if v_fname.get()=="" or v_contact.get()=="" or v_email.get()=="" or v_ques.get()=="select" or v_ans.get()=="" or v_pass.get()=="" or v_cpass.get()=="":
        msg.showerror("error", "All fields are manadatory",parent=a)
    elif v_pass.get()!=v_cpass.get():
        msg.showerror("Error", "password & confirm password must be same", parent=a)
    elif v_chk.get()==0:
        msg.showerror("Error","Please agree with terms & conditions")
    else:
        print(v_fname.get(),v_lname.get(),v_contact.get(),v_email.get(),v_ques.get(),v_ans.get(),v_chk.get(),v_pass.get())
        msg.showinfo("great", "Successfully Registered")   
        print(v_fname.get(),v_lname.get(),v_contact.get(),v_email.get(),v_ques.get(),v_ans.get(),v_chk.get(),v_pass.get())
        msg.showinfo("great", "Successfully Registered")
        
        conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="Pri@1234"
            )
        print(conn)
        cur=conn.cursor()
            #cur.execute("create database mine")
        cur.execute("use pri")
        cur.execute("insert into project(fname,lname, contact, email, quest,answer,password,cpassword) values (%s,%s,%s,%s,%s,%s,%s,%s)",
        
            (
            v_fname.get(),v_lname.get(), v_contact.get(), v_email.get(), v_ques.get(), v_ans.get(), v_pass.get(), v_cpass.get()             
           ))
                         
           #try:                
    #        conn=pymysql.connect(host="localhost", user="root", password="",database="register")
    #        cur=conn.cursor()
    #        #cur.execute("select * from student where email=%s", email.get())
    #        #row=cur.fetchone()
            #print(row)
            #if row!="":
            #    msg.showerror("Error","User already exists")
            #else:
    #        cur.execute("insert into student(fname, lname, contact, email, quest,answer,password,cpassword) values (%s,%s,%s,%s,%s,%s,%s)"
    #        (
    #        fname.get(), lname.get(),  contact.get(), email.get(), quest.get(),answer.get(),password.get()            
    #        ))
    #        conn.commit()
    #         conn.close()           
    #        msg.showinfo("success", "Registered Successfully!",parent=a)
     #       clear()        
     #   except Exception as es:
     #      msg.showerror("Error", f"Error due to: {str(es)}", parent=a)
   #     print(v_lname.get())
#        conn.commit()
 #       print(cur.rowcount, "record inserted")
  #      conn.close()     

a.title("Registration window")
a.maxsize(1550,860)
a.minsize( 1550,860)
a.config(bg="white")
a.title("Project")

#==bg image===
img1=Image.open("IMG-20220805-WA0005.jpg").resize((1550,860))
test=ImageTk.PhotoImage(img1)
lab1=tkinter.Label(image=test)
lab1.pack()

# ==left image==
img2=Image.open("IMG-20220805-WA0008.jpg").resize((520,520))
test2=ImageTk.PhotoImage(img2)
lab2=tkinter.Label(image=test2)
lab2.place(x=80,y=100,width=400,height=500)

frame1=Frame(bg="white")
frame1.place(x=480,y=100,width=700,height=500)

#====label text======

l=Label(a,text="Student Registration Panel", font=("times new roman", 30, "bold"), bg="white", fg="green")
l.place(x=550,y=40)

#===first name===
v_fname=StringVar()
fname = Label(a,text="first name", font=( "times new roman", 15, "bold"), bg="white", fg="gray").place(x=500, y=150)
txt_fname = Entry(a, font=("times new roman", 15, "bold"), bg="light gray", textvariable=v_fname).place(x=500, y=180, width=250)

# === last n-ame
v_lname=StringVar()
lname = Label(a,text="last name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=880, y=150)
txt_lname = Entry(a, font=("times new roman", 15, "bold"), bg="light gray",textvariable=v_lname).place(x=880, y=180, width=250)

# ==contact==
v_contact=StringVar()
contact = Label(a,text="contact no.", font=( "times new roman", 15, "bold"), bg="white", fg="gray").place(x=500, y=210)
txt_contact = Entry(a, font=("times new roman", 15, "bold"), bg="light gray",textvariable=v_contact).place(x=500, y=240, width=250) 

# ====email==
v_email=StringVar()
email = Label(a, text="E-mail", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=880, y=210)
txt_email = Entry(a, font=("times new roman", 15, "bold"),bg="light gray",textvariable=v_email).place(x=880, y=240, width=250)

# ==question===
v_ques=StringVar()
quest = Label(a, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=500, y=270)
com=ttk.Combobox(a,font=("times new roman", 13),textvariable=v_ques)
com['state']='readonly'
com['values'] = ("select", "your name?", "your pet name?", "your birth place?")
com.current(0)
com.place(x=500,y=300)

#===answer====
v_ans=StringVar()
answer = Label(a, text="answer", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=880, y=270)
txt_answer = Entry(a, font=("times new roman", 15, "bold"),bg="light gray",textvariable=v_ans).place(x=880, y=300, width=250)

# ===password===
v_pass=StringVar()
password = Label(a, text="password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=500, y=330)
txt_pass = Entry(a, font=("times new roman", 15, "bold"),show="*",bg="light gray",textvariable=v_pass).place(x=500, y=360, width=250)

# ==confirm password===
v_cpass=StringVar()
cpassword = Label(a, text="confirm password", font=("times new roman", 15,"bold"), bg="white", fg="gray").place(x=880, y=330)
txt_cpass = Entry(a, font=("times new roman", 15, "bold"),show="*",bg="light gray",textvariable=v_cpass).place(x=880, y=360, width=250)

v_chk=IntVar()
chk = Checkbutton(a, text="I agree with Terms & conditions",variable=v_chk,onvalue=1, offvalue=0, bg="white",font=("times new roman", 12)).place(x=500,y=420)
btn = Button(a, text="register here", font=("times new roman", 20),width=41,cursor="hand2",command=data).place(x=500, y=460)
btn2= Button(a, text="click", font=("times new roman", 20),width=41, cursor="hand2",command=next).place(x=500, y=520)
btn_login = Button(a, text="sign in", font=("times new roman", 20), cursor="hand2").place(x=200, y=460, width=108)
a.mainloop()