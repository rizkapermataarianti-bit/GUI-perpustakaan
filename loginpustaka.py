import tkinter as tk #mengimpor fugsi gui
from tkinter import ttk # memanggil tampilan layar
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess

layarLogin=tk.Tk()
w=400
h=350
ws=layarLogin.winfo_screenwidth()
hs=layarLogin.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
layarLogin.geometry('%dx%d+%d+%d' %(w,h,x,y))
layarLogin.resizable(False, False) #untuk mengunci layar supya tidak bisa diedit
layarLogin.title("Login Perpustakan")

data_admin= {
    "nicko": "123",
    "rezi": "123",
    "rizka": "123"
}
data_user= {
    "zayu": "123",
    "willy": "123"
}


def login():
    username = entr1.get()
    password = entr2.get()
    
    if username in data_admin and data_admin[username] == password:
        messagebox.showinfo("Login Berhasil", "Selamat datang di dashboard Admin!")
        subprocess.run(["python", "tabAdmin.py"])
        layarLogin.quit()

    elif username in data_user and data_user[username] == password:
        messagebox.showinfo("Login Berhasil", "Selamat datang di halaman User!")
        subprocess.run(["python", "tabUser.py"])
        layarLogin.quit()
    else:
        messagebox.showerror("Login Gagal", "Username atau Password salah.")

#FRAME 1  
        
frame1=tk.Frame(layarLogin, padx=5, pady=5, borderwidth=2,background='white')
frame1.pack(fill='y', expand=True)#biar warna dalam frame penuhh


try:
    image = Image.open("logo.png")  
    image = image.resize((140,80), Image.Resampling.LANCZOS)
    logo = ImageTk.PhotoImage(image)
    logo_label = tk.Label(frame1, image=logo,bg="white")
    logo_label.grid(row=0,column=1,pady=10,padx=0)
except FileNotFoundError:
    tk.Label(frame1, text="[Logo Tidak Ditemukan]").pack(pady=10)


lbl1=tk.Label(frame1,text="Username",bg="white",font=('Arial',10))
lbl1.grid(row=1,column=0, columnspan=2,sticky='w' )
lbl2=tk.Label(frame1,text='Password',bg="white",font=('Arial',10))
lbl2.grid(row=2,column=0, columnspan=2,sticky='w')

entr1=tk.Entry(frame1,width=40)
entr1.grid(row=1,column=1, columnspan=20,sticky='w', padx=0, pady=15)
entr2=tk.Entry(frame1,width=40,show='☺')
entr2.grid(row=2,column=1, columnspan=20, sticky='w', padx=0, pady=15)

btn1=tk.Button (frame1, text="Login", command=(login), font=('Arial',12,"bold"),bg="lightgreen",width=10)
btn1.grid(column=0,columnspan=1, padx=0, pady=15)

layarLogin.mainloop()
