
from tkinter import *
import base64

class MessageEncodeDecode():
    def __init__(self):
        self.window = Tk()
        self.window.title('Message Encode and Decode')
        self.window.geometry('800x500')

        lbl = Label(master=self.window, text='ENCODE DECODE',font=('Arial', 20,'bold'))
        lbl.pack(anchor='center')

        message_lbl = Label(master=self.window, text='MESSAGE', font=('Arial', 15,'bold'))
        message_lbl.place(x=50, y=80)

        self.message = StringVar()
        message_entry = Entry(master=self.window, textvariable=self.message,  width=30)
        message_entry.place(x=300, y=80)

        key_lbl = Label(master=self.window, text='KEY', font=('Arial', 15, 'bold'))
        key_lbl.place(x=50, y=140)

        self.key = StringVar()
        key_entry = Entry(master=self.window, textvariable=self.key, width=30)
        key_entry.place(x=300, y=140)

        mode_lbl = Label(master=self.window, text='MODE(e-encode,d-decode)', font=('Arial', 15, 'bold'))
        mode_lbl.place(x=50, y=200)

        self.mode = StringVar()
        mode_entry = Entry(master=self.window, textvariable=self.mode, width=30)
        mode_entry.place(x=300, y=200)

        result_bnt = Button (master=self.window, text='RESULT', font=('Arial', 15,'bold'), command=self.get_result)
        result_bnt.place(x=50, y=260)

        self.result = StringVar()
        result_entry = Entry(master=self.window, textvariable=self.result, width=30)
        result_entry.place(x=300, y=260)

        reset_bnt = Button(master=self.window, text='RESET', font=('Arial', 15, 'bold'), bg='red', command=self.reset)
        reset_bnt.place(x=80, y=350)

        exit_bnt = Button(master=self.window, text='EXIT',font=('Arial', 15, 'bold'), bg='green', command=self.exit_app)
        exit_bnt.place(x=300, y=350)

        self.window.mainloop()


    def get_result(self):
        msg_info = self.message.get()
        key_info = self.key.get()
        mode_info = self.mode.get()

        if mode_info == 'e':
            enc=[]
            for i in range(len(msg_info)):
                key_c = key_info[i%len(key_info)]
                enc.append(chr((ord(msg_info[i]) + ord(key_c)) % 256))
            self.result.set(base64.urlsafe_b64encode(''.join(enc).encode()).decode())

        elif mode_info =='d':

            dec = []
            msg = base64.urlsafe_b64decode(msg_info).decode()
            for i in range(len(msg)):
                key_c = key_info[i % len(key_info)]
                dec.append(chr((256 + ord(msg[i]) - ord(key_c)) % 256))

            self.result.set(''.join(dec))

    def reset(self):
        self.message.set('')
        self.key.set('')
        self.mode.set('')
        self.result.set('')

    def exit_app(self):
        self.window.destroy()



if __name__ == '__main__':
    MessageEncodeDecode()


