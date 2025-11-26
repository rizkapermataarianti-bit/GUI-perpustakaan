import tkinter as tk
from tkinter import ttk
import pymysql
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess


connection = pymysql.connect(host='localhost',
user='root',
password='',
database='perpustakaan')

layar1=tk.Tk()
w=650
h=440
ws=layar1.winfo_screenwidth()
hs=layar1.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
layar1.geometry('%dx%d+%d+%d' %(w,h,x,y))
layar1.resizable(False, False)
layar1.title("halaman daftar buku umum")

    
def tampilkanData():
    for data in trv.get_children():
        trv.delete(data)
    for array in bacaData():
        trv.insert(parent='', index='end',iid=array,text="", values=(array))
    trv.grid(row=3,column=1, columnspan=5,padx=20,pady=20,)


def bacaData():
    cursor=connection.cursor()
    cursor.execute("select * from buku")
    results=cursor.fetchall()
    connection.commit()
    return results

#FRAME3
frame3=tk.Frame(layar1, padx=130, pady=1, borderwidth=2,background='white')
frame3.pack(fill='x', expand=True)

try:
    image = Image.open("logo.png")  
    image = image.resize((140,80), Image.Resampling.LANCZOS)
    logo = ImageTk.PhotoImage(image)
    logo_label = tk.Label(frame3, image=logo,bg="white")
    logo_label.grid(padx=120)
except FileNotFoundError:
    tk.Label(frame3, text="[Logo Tidak Ditemukan]").pack(pady=10)

lbl1=tk.Label(frame3,text="DAFTAR BUKU UIN IB PADANG",bg="white",font=('calibri',15,"bold"))
lbl1.grid(columnspan=2,padx=70 )


frame2=tk.Frame(layar1,padx=1, pady=1, borderwidth=2,background='white')
frame2.pack(fill='both')
trv = ttk.Treeview(frame2)
trv["columns"] = ("idbuku", "judulbuku","penulis","tahunterbit","jumlah","status") # buat kolom
trv['show'] = 'headings' # membuat heading
# atur lebar kolom dan posisi mau kanan, kiri, atau tengah
trv.column("idbuku", width = 100, anchor ='w')
trv.column("judulbuku", width = 100, anchor ='c')
trv.column("penulis", width = 100, anchor ='w')
trv.column("tahunterbit", width = 100, anchor ='c')
trv.column("jumlah", width = 100, anchor ='w')
trv.column("status", width = 100, anchor ='c')
# atur nama heading berdasarkan kolom
trv.heading("idbuku", text ="idbuku")
trv.heading("judulbuku", text ="judulbuku")
trv.heading("penulis", text ="penulis")
trv.heading("tahunterbit", text ="tahunterbit")
trv.heading("jumlah", text ="jumlah")
trv.heading("status", text ="status")
trv.bind('<ButtonRelease-1>')
#btn1=tk.Button (frame2, text="Login", command=layar1.destroy, font=('Arial',12),bg="red")
#btn1.grid(pady=20)
tampilkanData()

tutup_button = tk.Button(layar1, text="Logout", command=layar1.destroy,font=('Arial',12,"bold"),bg="red")
tutup_button.pack(pady=10)

layar1.mainloop()
