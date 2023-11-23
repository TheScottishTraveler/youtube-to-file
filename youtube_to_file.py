import tkinter
import customtkinter
from pytube import YouTube


def downlaodVid():
    try:
        youtubeLink = link.get()
        youtubeVid = YouTube(youtubeLink)
        video = youtubeVid.streams.get_highest_resolution()
        title.configure(text=youtubeVid.title, text_color="white")
        statusInfo.configure(text="")
        video.download("insert path to save your file too")
        statusInfo.configure(text="success", text_color="green")
    except:
        statusInfo.configure(text="error", text_color="red")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("800x500")
app.title("Youtube Video Downloader")

title = customtkinter.CTkLabel(app,text="Insert a link to the youtube video")
title.pack(padx=15, pady=15)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=400, height=50, textvariable=url_var)
link.pack()

download = customtkinter.CTkButton(app, text="Download", command=downlaodVid)
download.pack(padx=15, pady=15)

statusInfo = customtkinter.CTkLabel(app, text="")
statusInfo.pack()

app.mainloop()