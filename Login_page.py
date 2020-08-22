import tkinter 
from tkinter import *
import tkinter as tk


root=tk.Tk()
username=tk.StringVar()
Mobile_no=tk.StringVar()
otp=tk.StringVar()
def esubmit():
    
    global name
    global username
    name=username_login_entry.get()
    Mobile=Mobile__login_entry.get()
    OTP=Otp_login_entry.get()
    print("username is: " +name)
    print("Mobile no is :"+Mobile)
    print("Password is :" +OTP)


root.title("Login Page")
root.geometry("300x250")
main_label=tk.Label(root, text="Please enter login details")
name_label=tk.Label(root, text="Username")
username_login_entry= Entry(root, textvariable=username)
Mobile_label=tk.Label(root, text="Mobile")
Mobile__login_entry = Entry(root, textvariable=Mobile_no)

sub_btn=tk.Label(root, text="Welcome", width=10, height=2)
Otp_label=tk.Label(root,text="Password")
Otp_login_entry=Entry(root,textvariable=otp)
otp_btn=tk.Button(root, text="Login", width=10, height=1,command=esubmit)

main_label.grid(row=0,column=1)
name_label.grid(row=3,column=1)
username_login_entry.grid(row=5,column=1)
Mobile_label.grid(row=7,column=1)
Mobile__login_entry.grid(row=8,column=1)
Otp_label.grid(row=11,column=1)
Otp_login_entry.grid(row=13,column=1)
sub_btn.grid(row=8,column=0)
otp_btn.grid(row=15,column=1)
root.mainloop()
