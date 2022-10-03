from tkinter import *
from urllib.request import  urlopen
import json
from tkinter import ttk


class RealTimeCurrencyConvert():
    def __init__(self, url):
        self.response = urlopen(url)
        self.data_jason = json.loads(self.response.read())
        self.date = self.data_jason['date']
        self.data = self.data_jason['rates']
        self.currency_list = list(self.data.keys())

    def convert(self, from_curr, to_curr, amount):
        usd_amount = amount/self.data[from_curr]
        to_curr_amount = usd_amount * self.data[to_curr]
        return to_curr_amount

class App():
    def __init__(self, converter):
        window = Tk()
        window.title('Currency Converter')
        window.geometry('600x400')
        self.currency_converter = converter

        lbl_welcome = Label(master=window, text='Welcome to Real Time Currency Converter', font=('Arial', 20, 'bold'), \
                            bg='blue', fg='white')
        lbl_welcome.pack(fill=X,anchor='center')



        lbl_rate = Label(master=window, text = f"1 USD equals = {self.currency_converter.convert('USD','CNY',1)}  Yuan", font=('Arial', 20,'bold'))
        lbl_rate.pack(fill=X, anchor='center')

        lbl_date = Label(master=window, text=f'{self.currency_converter.date}', font=('Arial',20,'bold'))
        lbl_date.pack(fill=X, anchor='center')


        self.from_currency_variable = StringVar()
        self.from_currency_variable.set('USD')
        from_currency_box =ttk.Combobox(master=window,textvariable=self.from_currency_variable,width=20)
        from_currency_box['value'] = self.currency_converter.currency_list
        from_currency_box.place(x=50, y=120)

        self.from_currency_amount = IntVar()
        self.from_currency_amount.set('')
        from_currency_amount_entry = Entry(master=window, textvariable=self.from_currency_amount, width=20)
        from_currency_amount_entry.place(x=50,  y=160)


        self.to_currency_variable = StringVar()
        to_currency_box= ttk.Combobox(master=window, textvariable=self.to_currency_variable,width=20)
        to_currency_box['value'] = self.currency_converter.currency_list
        to_currency_box.place(x=300, y=120)

        self.to_currency_amount = IntVar()
        self.to_currency_amount.set('')
        to_currency_amount_entry= Entry(master=window, textvariable=self.to_currency_amount,width=20)
        to_currency_amount_entry.place(x=300, y=160)

        bnt_convert = Button(master=window, font=('Arial', 20,'bold'), text='Convert',bg='blue',fg='white',width=20,command=self.perform)
        bnt_convert.place(x=160, y=200)



        window.mainloop()

    def perform(self):
        amount_converted = self.currency_converter.convert(self.from_currency_variable.get(), self.to_currency_variable.get(), self.from_currency_amount.get())
        amount_converted =round(amount_converted,2)
        self.to_currency_amount.set(amount_converted)


if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    convert = RealTimeCurrencyConvert(url)
    App(convert)