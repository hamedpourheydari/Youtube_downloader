"""
Designed by Hamed Pourheidari
Designed on March 2024
This program belongs to Sendmind company
email: pourheadari1990@gmail.com
Company email: info@sendmind.net

"""
import tkinter as tk
from tkinter.filedialog import askdirectory
from pytube import YouTube
from tkinter import messagebox

#------Start TK----------
window = tk.Tk()

#------Window Title --------
window.title("برنامه دانلود از یوتیوب سندمایند")
#------Window Title --------

#---------Window Size-----------
window.maxsize(500,500)
window.minsize(450,300)
#---------Window Size-----------
def widgets():
    #------------------Link_Label-------------------------
    link_label = tk.Label(window, text="لینک خود را وارد نمایید")
    link_label.grid(row=0, column=0, padx=20, pady=20)
    link_label.config(font=("None",15),fg="green")
    link_input = tk.Entry(window, width=30, textvariable=video_link)
    link_input.grid(row=0, column=1)
    #------------------Link_Label-------------------------
    
    #--------------------place label------------------------
    
    place_label = tk.Label(window, text="محل ذخیره")
    place_label.grid(row=1, column=0)
    place_label.config(font=("None",15),fg="red")
    place_input = tk.Entry(window, width=30, textvariable=download_dir)
    place_input.grid(row=1, column=1)
    #--------------------place label------------------------
    
    #--------------------‌Browse ‌Button------------------------
    place_btn= tk.Button(window, text="جستجو", command=browse)
    place_btn.grid(row=1, column=2)
    #--------------------place ‌Button------------------------
    
    #--------------------Download ‌Button------------------------
    download_btn= tk.Button(text="دانلود", command=download)
    download_btn.grid(row=2,column=1, pady=30)
    download_btn.config(height=1, width=10, bg="green", fg="white")
    #--------------------Download ‌Button------------------------
    
#--------------------جستجو بین فولدرها------------------------
def browse():
    directory= askdirectory(initialdir="مسیر پوشه شما", title="ذخیره")
    download_dir.set(directory)
download_dir = tk.StringVar()

#--------------------جستجو بین فولدرها------------------------
#--------------------خواندن لینک دانلود و اجرای آن------------------------
video_link = tk.StringVar()
#--------------------خواندن لینک دانلود و اجرای آن------------------------
#--------------------اتصال دکمه دانلود به لینک اینپوت------------------------
def download():
    link= video_link.get()
    save_dir = download_dir.get()
    yt = YouTube(link)
    yt.streams.filter(file_extension="mp4").get_highest_resolution().download(save_dir)
    messagebox.showinfo(title="ثبت موفق", message="فیلم شما دانلود شد. باتشکر از انتخاب شماُ شرکت بین المللی سندمایند")
#--------------------اتصال دکمه دانلود به لینک اینپوت------------------------


widgets()
window.mainloop()