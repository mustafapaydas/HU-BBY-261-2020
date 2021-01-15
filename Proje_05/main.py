from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from sqlite3 import *
import time
import datetime
import random

pencere=Tk()
pencere.title("Sqlite Database")
pencere.geometry("1150x670+100+10")


C = Canvas(pencere, width=1150,height=650)
filename =ImageTk.PhotoImage(Image.open("arka.png"))
background_label = Label(pencere, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)





#pencere.config(bg = "light grey")
with connect("Mesaj Kutusu.db")as datam:
    mesaj = datam.cursor()
    mesaj.execute("CREATE TABLE IF NOT EXISTS MesajKutusu (ID INTEGER PRIMARY KEY AUTOINCREMENT,İsim TEXT,Tarih TEXT,Mesaj TEXT)")
mesajresmi=ImageTk.PhotoImage(Image.open("mesajre.png"))
silgi=ImageTk.PhotoImage(Image.open("delete.png"))
arayıcı=ImageTk.PhotoImage(Image.open("okut.png"))
degis=ImageTk.PhotoImage(Image.open("exchange.png"))
okut=ImageTk.PhotoImage(Image.open("listele.png"))

def database():

    def kisi():

        if kim.get() == "":
            a="  Kimden: "+random.choice(isimler)
        else:
            a="  Kimden: "+kim.get()
        return a

    isimler = ['Mehmet', ' Mustafa', ' Ahmet', ' Ali', ' Hüseyin', ' Hasan', ' İbrahim', ' \nİsmail', ' Osman',
               ' Halil', ' Süleyman', ' Yusuf', ' \nÖmer', ' Abdullah', ' Mahmut', ' Salih', ' Kemal', ' Ramazan',
               ' Recep', ' Mehmet Ali.\nFatma', ' Ayşe', ' Emine', ' Hatice', ' Zeynep', ' Şerife', ' Hanife',
               ' Meryem', ' Sultan', '\n Zehra', ' Havva', ' Hayriye', ' Cemile', ' Zeliha', ' Elif', ' Gülsüm',
               ' Naciye', ' Havva ve Fadime.\n']

    vakit = time.time()
    tarih = str(datetime.datetime.fromtimestamp(vakit).strftime("  %Y/%m/%d Tarihinde ve %H.%M Saatinde Mesaj Alındı."))
    gonderene = kisi()
    mesajial = "  Mesaj: "+ileti.get()
    mesaj.execute("INSERT INTO  MesajKutusu(İsim,Tarih,Mesaj) VALUES(?,?,?)",(gonderene,mesajial, tarih ))
    datam.commit()
    messagebox.showinfo("Mesaj Ekleme","Mesajınız Başarıyla Eklendi!")
    ileti.delete(0,END)
    kim.delete(0,END)



def mesajokumak():
    box.delete(0, END)

    mesaj.execute("SELECT * FROM MesajKutusu")
    for tek in mesaj.fetchall():
        box.insert(0,str(tek[0])+tek[1]+tek[2]+tek[3])

def satirSil():
    mesaj.execute("delete from MesajKutusu WHERE ID=?",(satSil.get(),))
    datam.commit()
    mesaj.execute("SELECT * FROM MesajKutusu")
    box.delete(0,END)
    for tek in mesaj.fetchall():
        box.insert(0,str(tek[0])+tek[1]+tek[2]+tek[3])
def guncelleme():
    vakit = time.time()
    tarih = str(datetime.datetime.fromtimestamp(vakit).strftime("  %Y/%m/%d Tarihinde ve %H.%M Saatinde Mesaj Güncellendi."))
    yenisim= "  Kimden "+gunisim.get()
    mesaj.execute("update MesajKutusu set İsim=?,Mesaj=?,Tarih=? where ID=?",(yenisim,gunmesgir.get(),tarih,gunid.get()))
    datam.commit()
    box.delete(0,END)
    mesaj.execute("SELECT * FROM MesajKutusu")
    for tek in mesaj.fetchall():
        box.insert(0, str(tek[0]) + tek[1] + tek[2] + tek[3])
def Arama():
    mesaj.execute("select * from MesajKutusu where ID=?",(arayap.get(),))
    box.delete(0,END)
    for tek in mesaj.fetchall():
        box.insert(0, str(tek[0]) + tek[1] + tek[2] + tek[3])
def ismeara():
    mesaj.execute("select * from MesajKutusu where İsim LIKE ?", ('%'+arayapma.get()+'%',))
    box.delete(0, END)
    for tek in mesaj.fetchall():
        box.insert(0, str(tek[0]) + tek[1] + tek[2] + tek[3])
etik= Label(text=" Mesajınızı Girin ",font="Arial 18 bold",fg="white",bg="black")
etik.place(x=10,y=10)
ileti = Entry(font="Arial 18 bold")
ileti.place(x=250,y=10)
etik2= Label(text="Göndericiyi Girin",font="Arial 18 bold",fg="white",bg="black")
etik2.place(x=10,y=50)
kim=Entry(font="Arial 18 bold")
kim.place(x=250, y=50)
buton=Button(image=mesajresmi,command=database,bg="red",activebackground="darkblue")
buton.place(x=210,y=90)
satYaz=Label(text="Silmek İstediğiniz Satırın ID Numarası",font="Arial 18 bold",fg="white",bg="black")
satYaz.place(x=650,y=10)
satSil=Entry(font="Arial 18 bold")
satSil.place(x=725,y=50)
satDug = Button(image=silgi,command=satirSil,bg="red",activebackground="darkblue")
satDug.place(x=825,y=90)
gunyaz= Label(text="Değişim İşlemleri",font="Arial 18 bold",fg="white",bg="black")
gunyaz.place(x=185,y=230)
gunyaz1=Label(text="İsim",font="Arial 18 bold",fg="white",bg="black")
gunyaz1.place(x=40,y=270)
gunmesaj=Label(text="Mesaj",font="Arial 18 bold",fg="white",bg="black")
gunmesaj.place(x=40,y=310)
gunisim= Entry(font="Arial 18 bold")
gunisim.place(x=150,y=270)
gunmesgir = Entry(font="Arial 18 bold")
gunmesgir.place(x=150,y=310)
gunidyaz= Label(text="ID No",font="Arial 18 bold",fg="white",bg="black")
gunidyaz.place(x=40,y=350)
gunid=Entry(font="Arial 18 bold")
gunid.place(x=150,y=350)
gundug= Button(image=degis,command=guncelleme,bg="red",activebackground="darkblue")
gundug.place(x=260,y=400)
arayaz=Label(text="Arama Yapın",font="Arial 18 bold",fg="white",bg="black")
arayaz.place(x=785,y=230)
arayap =Entry(font="Arial 18 bold")
arayap.place(x=725,y=270)
aralık=Label(text="Veya İsimden Arama Yapın",font="Arial 10 bold",bg="black",fg="white")
aralık.place(x=775,y=315)
arayapma =Entry(font="Arial 18 bold")
arayapma.place(x=725,y=350)
aradug= Button(image=arayıcı,command=Arama,bg="red",activebackground="darkblue")
aradug.place(x=1000,y=270)
aradug2 = Button(image=arayıcı,command=ismeara,bg="red",activebackground="darkblue")
aradug2.place(x=1000,y=350)
box=Listbox(width=80,font="Arial 10 bold",bg="antique white")
box.place(x=290,y=450)
buton2=Button(image=okut,command=mesajokumak,bg="red",activebackground="darkblue")
buton2.place(x=550,y=625)


mainloop()
