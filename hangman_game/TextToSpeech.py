from gtts import gTTS
from tkinter import *
import os

class TextToSpeech():
    def __init__(self):
        window = Tk()
        window.title('Text_To_Speech')
        window.geometry('400x400')
        window.configure(bg='ghost white')

        lbl_text = Label(master=window, text='Enter Text', font=('Arial', 25,'bold'))
        lbl_text.place(x=20, y=50)

        self.text_variable = StringVar()
        text_entry = Entry(master=window, textvariable=self.text_variable, width=40)
        text_entry.place(x=20,y=80)

        bnt_play = Button(master=window, text='PLAY', width=10, command=self.play)
        bnt_play.place(x=20, y=120)

        bnt_exit = Button(master=window, text='EXIT', width=10, command=self.exit_from_app)
        bnt_exit.place(x=150, y=120)

        bnt_reset = Button(master=window, text='RESET', width=10, command=self.reset)
        bnt_reset.place(x=260, y=120)

        window.mainloop()

    def play(self):
        language = 'en'

        myobj = gTTS(text=self.text_variable.get(), lang=language,slow=False)
        myobj.save('TextToSpeech.mp3')
        os.system('afplay TextToSpeech.mp3')

    def exit_from_app(self):
        exit(0)

    def reset(self):
        self.text_variable.set('')


if __name__ == '__main__':
    TextToSpeech()