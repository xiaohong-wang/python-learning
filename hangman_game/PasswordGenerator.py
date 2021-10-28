import random
import string
from tkinter import *
import pyperclip


window = Tk()
window.title('Password Generator')
window.geometry('500x500')

lbl_1 = Label(master=window, text='Passowrd Generator Application', font=('Arial', 25,'bold'))
lbl_1.place(x=50, y=20)

lbl_password_length = Label(master=window, text='Password Length', font=('Arial', 20))
lbl_password_length.place(x=100, y=70)

pass_len = IntVar()
pass_len.set(8)
sp = Spinbox(master=window, textvariable=pass_len, from_=5, to=32)
sp.place(x=100,y=105)

pass_str = StringVar()
entry_password = Entry(master=window, textvariable=pass_str, width=25)
entry_password.place(x=100, y=220)

def GeneratePassword():
    for i in range(0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_letters) + random.choice(string.digits)

    for i in range(4, pass_len.get()):
        password = password + random.choice(string.ascii_letters + string.punctuation + string.digits)

    pass_str.set(password)


bnt_generator = Button(master=window, text='Generate Password', width=25,command=GeneratePassword)
bnt_generator.place(x=100,y=150)

def copy2clip():
    text = pass_str.get()
    pyperclip.copy(text)



bnt_copy = Button(master=window, text='Copy to Clickboard', width=25,command=copy2clip)
bnt_copy.place(x=100,y=300)




window.mainloop()



