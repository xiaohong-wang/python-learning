from tkinter import *
import pytube

class YoutubeVideoDownloader():
    def __init__(self):
        window = Tk()
        window.title('Youtube Video Downloader')
        window.geometry('400x300')

        lbl = Label(master=window, text='Youtube Video Downloader', font=('Arial', 25, 'bold'))
        lbl.place(x=30, y=20)

        lbl_paste = Label(master=window, text='Paste Link Here:', font=('Arial', 20))
        lbl_paste.place(x=100, y=80)

        self.link = StringVar()
        link_entry = Entry(master=window, text=self.link, width=50)
        link_entry.place(x=20, y=150)

        bnt_download = Button(master=window, text='Download', bg='blue', fg='black',command=self.download)
        bnt_download.place(x=100, y=220)

        window.mainloop()

    def download(self):
        url = self.link.get()
        youtube = pytube.YouTube(url)
        video = youtube.streams.first()
        video.download()

if __name__ == '__main__':
    YoutubeVideoDownloader()
