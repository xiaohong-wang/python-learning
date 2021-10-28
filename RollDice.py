from tkinter import *
from PIL import Image, ImageTk
import random

class RollDice():

    def __init__(self):

        self.window = Tk()
        self.window.title('Roll the Dice')
        self.window.geometry('400x400')

        self.dice = ['die1.PNG','die2.PNG','die3.PNG','die4.PNG','die5.PNG','die6.PNG']
        self.path = random.choice(self.dice)
        img = ImageTk.PhotoImage(Image.open(self.path))
        self.lbl = Label(master=self.window, image=img)
        self.lbl.place(x=50, y=30)

        bnt = Button(master=self.window, text='Roll the Dice', command=self.DiceResult)
        bnt.place(x=120,y=350)


        self.window.mainloop()


    def DiceResult(self):
        self.path = random.choice(self.dice)
        img = ImageTk.PhotoImage(Image.open(self.path))
        self.lbl.configure(image=img)
        self.lbl.image=img



RollDice()
