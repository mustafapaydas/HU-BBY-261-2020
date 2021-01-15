from tkinter import *
from random import *
pen = Tk()
pen.title("Hacettepe BBY Kütüphanesi")
pen.geometry("1000x500+175+125")
def ekle():
    ek=open("kütüphane.txt","a",encoding="utf-8")
    kit = ekleE.get()

    ekleE.insert(0,ek.write("{} \n".format(kit)))
    ek.close()
def temizle():
    ekleE.delete(0,END)
    cikart.delete(0,END)
def show():
    okuma = open("kütüphane.txt",encoding="utf-8")
    al = okuma.readlines()
    for i in al:
        liste.insert(END, i)
def arama():
    aramak = ara.get()
    okuma2=open("kütüphane.txt",encoding="utf-8")
    for satir in okuma2.readlines():
        if satir.lower().find(aramak) != -1:
            cikart.insert(0,satir)
        elif satir.upper().find(aramak) != -1:
            cikart.insert(0,satir)
def kitapsec():
    okuma3=open("kütüphane.txt",encoding="utf-8")
    kitapsecim = choice(okuma3.readlines())
    sec.insert(0,kitapsecim)
yazi1 = Label(text="Kütüphaneme Hoşgeldiniz!!!",font="Arial 21 bold",fg="darkblue",bg="yellow")
yazi2= Label(text= "Neredeyse 2 sene önce yaptığım final ödevini arayüz ile tasarlamamıştım ve şimdi tasarlama fırsatı buldum!",fg="blue")
yazi1.grid()
yazi2.grid()

yazi3= Label(text="Lütfen eser adı, yazar adı, tarih(yyyy)olarak giriniz",font="Arial 18",fg="darkgrey")
ekleE = Entry()
butonE=Button(text="Ekle",font="Times 15 bold",fg="blue",command=ekle)
yazi3.grid(row=4,column=0)
ekleE.grid(row=5,column=0)
butonE.grid(row=6,column=0)


butonE=Button(text="Temizle",font="Times 18 bold",fg="blue",command=temizle)
butonE.grid(row=7,column=0)
yazboz = Label(text="",font="Arial 28")
yazboz.grid(row=4,column=1)

yazi4= Label(text="Aramak İstediğiniz Kitabi Girin",font="Arial 18",fg="darkgrey")
yazi4.grid(row=4,column=2)
ara = Entry(width=30,font="Arial 15")
ara.grid(row=5,column=2)
arat = Button(text="Tara",command=arama,font="Times 15 bold",fg="blue")
arat.grid(row=7,column=2)
cikart=Entry(width=30,font="Arial 15")
cikart.grid(row=6,column=2)

liste = Listbox(width=40,font="Times 12")
liste.grid(row=8,column=0)
okut = Button(text="Göster",command=show,font="Times 15 bold",fg="blue")
okut.grid()



sec= Entry(width=50,font="Arial 15")
sec.grid(row=8,column=2)
butonSec=Button(text="Kitap seç",command=lambda :kitapsec(),font="Times 15 bold",fg="blue")
butonSec.grid(row=9,column=2)
mainloop()