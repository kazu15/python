from tkinter import *
import os

def register_user():
    username_info = username.get()
    password_info = password.get()
    
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    Label(screen1, text="registeration success", font="green", height='2', width='30').pack()
    
    
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry("400x300")
    screen1.title("register")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(screen1, text="please enter the given given information", height="2", width="30")
    Label(screen1, text="", height='2', width="30").pack()
    Label(screen1, text="username", height='2', width="30").pack()
    username_entry = Entry(screen1,textvariable = username)
    username_entry.pack()
    Label(screen1,text="password", height= '2', width='30').pack()
    password_entry = Entry(screen1,textvariable=password)
    password_entry.pack()
    Label(screen1,text="", height='2', width='30').pack()
    Button(screen1,text="submit", height='2', width='15', command=register_user).pack() 
    
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    list_of_dir = os.listdir()
    if username1 in list_of_dir:
        file = open(username1,"r")
        verify = file.read().splitlines()
        if password1 in verify:
            print("success")
        else:
            print("wrong password")
    else:
        pass
        # print ("user not found")url go(f, seed, [])
        
def login():
    global screen2
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    
    screen2 = Toplevel(screen)
    screen2.geometry("400x300")
    screen2.title("login")
    Label(screen2,text="Please enter the information for login", height='2', width='30').pack()
    Label(screen2,text="", height='2', width='30').pack()
    Label(screen2,text="username : ", height='2',width='30').pack()
    username_entry1 = Entry(screen2,textvariable = username_verify)
    username_entry1.pack()
    password_entry1 = Entry(screen2,textvariable = password_verify)
    password_entry1.pack()
    Label(screen2,text="", height='2', width='30').pack()
    Button(screen2, text="login", height='2', width="15", command = login_verify).pack()
    
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("400x300")
    Label(text="AutoLike login", height='5').pack() 
    Label(text="", height='5', width='30') #
    Button(text="Login", height='2', width='45', bg='skyblue', command = login).pack()
    Label(text="", height='2',width='30').pack()
    Button(text="register", height='2', width='45', bg="yellowgreen", command = register).pack()
    screen.mainloop()
    
main_screen()