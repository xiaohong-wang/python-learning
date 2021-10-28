from tkinter import *
import random

class Rock_Scissor_Paper():
    def __init__(self):
        window = Tk()
        window.title('Rock,Paper,Scissors')
        window.geometry('600x500')
        window.configure(bg='light gray')

        lbl = Label(master=window, text='Rock,Paper,Scissors', bg='light gray', fg='black', font=('Arial', 30,'bold'))
        lbl.place(x=50,y=10)
        lbl_choose = Label(master=window,text='Choose any one: rock, paper scissors',bg='light gray',font=('Arial', 20, 'bold'))
        lbl_choose.place(x=50, y=60)

        self.player_input =StringVar()
        entry_player = Entry(master=window, textvariable=self.player_input, width=30)
        entry_player.place(x=70,y=110)

        bnt_play = Button(master=window, text='Play', font=('Arial', 20, 'bold'), command=self.play)
        bnt_play.place(x=150, y=180)

        self.result =StringVar()
        result_entry = Entry(master=window, textvariable=self.result, width= 50)
        result_entry.place(x=50, y=220)


        bnt_reset = Button(master=window, text='RESET', font=('Arial', 20,'bold'), command=self.reset)
        bnt_reset.place(x=50, y=270)

        bnt_exit = Button(master=window, text='EXIT', font=('Arial', 20,'bold'), command=self.exit_from_app)
        bnt_exit.place(x=200, y=270)

        window.mainloop()

    def play(self):
        choices=['rock','paper','scissor']
        winning_choices =[('rock','scissor'),('scissor','paper'),('paper','rock')]
        comp_choice = random.choice(choices)
        print(str(self.player_input.get()))
        if comp_choice == str(self.player_input.get()):
            self.result.set('Tie. You both selected ' + str(self.player_input.get()))

        elif (str(self.player_input.get()), comp_choice) in winning_choices:
            self.result.set('You win! Computer selected '+ comp_choice)
        else:
            self.result.set('You lose! Computer selected ' + comp_choice)

    def reset(self):
        self.player_input.set('')
        self.result.set('')

    def exit_from_app(self):
        exit()




Rock_Scissor_Paper()