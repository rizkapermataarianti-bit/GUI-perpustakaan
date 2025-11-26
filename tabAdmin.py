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
w=790
h=780
ws=layar1.winfo_screenwidth()
hs=layar1.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
layar1.geometry('%dx%d+%d+%d' %(w,h,x,y))
layar1.resizable(False, False)
layar1.title("DATA PERPUSTAKAAN")

idbukuvariable=tk.StringVar()
judulbukuvariable=tk.StringVar()
penulisvariable=tk.StringVar()
tahunterbitvariable=tk.StringVar()
jumlahvariable=tk.StringVar()
statusvariable=tk.StringVar()
def selectItem(a):
    curItem = trv.focus()
    idbuku=trv.item (curItem) ['values'][0]
    idbukuvariable.set(idbuku)
    entr1.configure (textvariable=idbukuvariable)
    
    judulbuku=trv.item(curItem) ['values'] [1]
    judulbukuvariable.set(judulbuku)
    entr2.configure (textvariable=judulbukuvariable)
    
    penulis=trv.item (curItem) ['values'] [2]
    penulisvariable.set(penulis)
    entr3.configure (textvariable=penulisvariable)
    
    tahunterbit=trv.item (curItem) ['values'] [3]
    tahunterbitvariable.set(tahunterbit)
    entr4.configure (textvariable=tahunterbitvariable)
    
    jumlah=trv.item (curItem) ['values'] [4]
    jumlahvariable.set(jumlah)
    entr5.configure (textvariable=jumlahvariable)
#ini belum cc
    #selected_value = var_status.get()
    #entry_var.set(selected_value)

def tampilkanData():
    for data in trv.get_children():
        trv.delete(data)
    for array in bacaData():
        trv.insert(parent='', index='end',iid=array,text="", values=(array))
    trv.grid(row=3,column=1, columnspan=5,padx=20,pady=20,)


def bacaData():
    cursor=connection.cursor() #untuk menghubungkan dan berinteraksi dengan database
    cursor.execute("select * from buku") #menjalankan sql untuk menggabil semua data
    results=cursor.fetchall() #mengambil data dalam bentuk list
    connection.commit()
    return results

from tkinter import messagebox
def tambahData():
    idbuku=str(entr1.get())
    judulbuku=str(entr2.get())
    penulis=str(entr3.get())
    tahunterbit=str(entr4.get())
    jumlah=str(entr5.get())
    status=str(var_status.get())
    if (idbuku==""):
        messagebox.showinfo("Maaf","silahkan isi Id Buku")
        return
    else:
        try:
            cursor=connection.cursor() #menghubungkan data di msql dan codingan di python
            sql=("insert into buku (idbuku,judulbuku,penulis,tahunterbit,jumlah,status) values(%s,%s,%s,%s,%s,%s)")
            cursor.execute(sql,(idbuku,judulbuku,penulis,tahunterbit,jumlah,status))
            connection.commit()
        except:
            messagebox.showinfo("Maaf","ada error")
            return
        
        messagebox.showinfo("berhasil", "DATA SUDAH DI TAMBAH")
        entr1.delete(0, 'end')
        entr2.delete(0, 'end')
        entr3.delete(0, 'end')
        entr4.set("Pilih Tahun")
        entr5.delete(0, 'end')
      
    tampilkanData()

        
    tampilkanData()


def hapusData():
    pilihData=trv.selection()[0]
    idbuku=str(trv.item(pilihData)['values'][0])
    print(idbuku)
    try:
        sql=("delete from buku where idbuku=(%s)")
        cursor=connection.cursor()
        cursor.execute(sql,(idbuku))
        connection.commit()
    except:
        messagebox.showinfo("Maaf","ada error")
        return
    messagebox.showinfo("berhasil", "data sudah di hapus")
    entr1.delete(0, 'end')
    entr2.delete(0, 'end')
    entr3.delete(0, 'end')
    entr4.set("Pilih Tahun")
    entr5.delete(0, 'end')
    
    tampilkanData()

def updateData():
    idbuku=str(entr1.get())
    judulbuku=str(entr2.get())
    penulis=str(entr3.get())
    tahunterbit=str(entr4.get())
    jumlah=str(entr5.get())
    status=str(var_status.get())
    print(status)
    if (idbuku==""): 
        messagebox.showinfo("Maaf","silahkan isi Id Buku") 
        return
    else: 
        try:
            cursor=connection.cursor()
            sql=("update buku set idbuku=%s, judulbuku=%s, penulis=%s, tahunterbit=%s, jumlah=%s, status=%s where idbuku=%s") 
            cursor.execute(sql,(idbuku,judulbuku,penulis,tahunterbit,jumlah,status,idbuku))
            connection.commit() 
        except:
            messagebox.showinfo("Maaf","ada error")
            return
    messagebox.showinfo("berhasil", "data sudah diupdate")
    entr1.delete(0, 'end')
    entr2.delete(0, 'end')
    entr3.delete(0, 'end')
    entr4.set("Pilih Tahun")
    entr5.delete(0, 'end')

    tampilkanData()



#FRAME3
frame3=tk.Frame(layar1, padx=70, pady=5, borderwidth=2,background='white')
frame3.pack(fill='x', expand=True)

try:
    image = Image.open("logo.png")  
    image = image.resize((140, 80), Image.Resampling.LANCZOS)#perintah untuk nampilin data
    logo = ImageTk.PhotoImage(image)
    logo_label = tk.Label(frame3, image=logo,bg="white")
    logo_label.grid(row=0,column=0,pady=10,padx=10)
except FileNotFoundError:
    tk.Label(frame3, text="[Logo Tidak Ditemukan]").pack(pady=10)

lbl1=tk.Label(frame3,text="MANAJEMEN BUKU \n PERPUSTAKAAN UIN IB PADANG",bg="white",font=('calibri',15,"bold"))
lbl1.grid(row=0,column=1, columnspan=1,sticky='e',padx=70 )



#FRAME 1
frame1=tk.Frame(layar1, padx=125, pady=5, borderwidth=2,background='white')
frame1.pack(fill='x', expand=True)
var_status = tk.StringVar(value="Tersedia")

lbl1=tk.Label(frame1,text="ID BUKU",bg="white",font=('Arial',10))
lbl1.grid(row=0,column=0, columnspan=2,sticky='w' )
lbl2=tk.Label(frame1,text='JUDUL BUKU',bg="white",font=('Arial',10))
lbl2.grid(row=1,column=0, columnspan=2,sticky='w')
lbl3=tk.Label(frame1,text='PENULIS',bg="white",font=('Arial',10))
lbl3.grid(row=2,column=0, columnspan=2,sticky='w')
lbl4=tk.Label(frame1,text='TAHUN TERBIT',bg="white",font=('Arial',10))
lbl4.grid(row=3,column=0, columnspan=2,sticky='w')
lbl5=tk.Label(frame1,text='JUMLAH',bg="white",font=('Arial',10))
lbl5.grid(row=4,column=0, columnspan=2,sticky='w')
lbl6=tk.Label(frame1,text='STATUS',bg="white",font=('Arial',10))
lbl6.grid(row=5,column=0, columnspan=2,sticky='w')

entr1=tk.Entry(frame1,width=45, textvariable=idbukuvariable)
entr1.grid(row=0,column=2, columnspan=20,sticky='w', pady=10)
entr2=tk.Entry(frame1,width=45, textvariable=judulbukuvariable)
entr2.grid(row=1,column=2, columnspan=20, sticky='w', pady=10)
entr3=tk.Entry(frame1,width=45, textvariable=penulisvariable)
entr3.grid(row=2,column=2, columnspan=20, sticky='w', pady=10)

tahun = ["2015", "2016", "2017", "2018"]
entr4=ttk.Combobox(frame1,values=tahun)
entr4.grid(pady=10,row=3,column=2)
entr4.set("Pilih Tahun")
entr4['state'] = 'readonly'

entr5=tk.Entry(frame1,width=23, textvariable=jumlahvariable)
entr5.grid(row=4,column=2, columnspan=20, sticky='w', pady=10)

entr6 = tk.Radiobutton(frame1, text="Tersedia", variable=var_status, value="Tersedia",bg="white")
entr6.grid(row=5,column=2,pady=5,sticky='w')
entr6 = tk.Radiobutton(frame1, text="Tidak Tersedia", variable=var_status, value="Tidak Tersedia",bg="white")
entr6.grid(row=5,column=3,pady=5,sticky='w')


btn1=tk.Button (frame1, text="Tambah", command=tambahData, font=('Arial',12,"bold"),width=8)
btn1.grid(row=6, column=0,columnspan=1, pady=30, padx=15)
btn2=tk.Button (frame1, text="Hapus", command=hapusData, font=('Arial',12,"bold"),width=8)
btn2.grid(row=6, column=1, columnspan=1, sticky='w',pady=10, padx=15)
btn3=tk.Button (frame1, text="Update", command=updateData, font=('Arial',12,"bold"),width=8)
btn3.grid(row=6, column=2, columnspan=1, sticky='w', pady=10, padx=15)


#FRAME 2
frame2=tk.Frame(layar1,padx=1, pady=1, borderwidth=2,background='white')
frame2.pack(fill='both')# mengisi layar penuh baik herizontal maupun vertikal
trv = ttk.Treeview(frame2)
trv["columns"] = ("ID BUKU", "JUDUL BUKU","PENULIS","TAHUN TERBIT","JUMLAH","STATUS") # buat kolom
trv['show'] = 'headings' # membuat heading
# atur lebar kolom dan posisi mau kanan, kiri, atau tengah
trv.column("ID BUKU", width = 100, anchor ='c')
trv.column("PENULIS", width = 150, anchor ='w')
trv.column("TAHUN TERBIT", width = 100, anchor ='c')
trv.column("JUMLAH", width = 100, anchor ='c')
trv.column("STATUS", width = 100, anchor ='c')
# atur nama heading berdasarkan kolom
trv.heading("ID BUKU", text ="ID BUKU")
trv.heading("JUDUL BUKU", text ="JUDUL BUKU")
trv.heading("PENULIS", text ="PENULIS")
trv.heading("TAHUN TERBIT", text ="TAHUN TERBIT")
trv.heading("JUMLAH", text ="JUMLAH")
trv.heading("STATUS", text ="STATUS")
trv.bind('<ButtonRelease-1>', selectItem)
tampilkanData() 

tutup_button = tk.Button(layar1, text="Logout", command=layar1.destroy,font=('Arial',12,"bold"),bg="red")
tutup_button.pack(pady=10)

layar1.mainloop()



