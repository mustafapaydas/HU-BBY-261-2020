import tkinter
from PIL import Image,ImageTk
from selenium import webdriver
import speech_recognition as sr
import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
import sifre

pen =tkinter.Tk()
pen.title("Jarvis")
pen.geometry("400x400")
mikrofon=ImageTk.PhotoImage(Image.open("microphone.png"))
r = sr.Recognizer()

def dersSayfa():
    driver=webdriver.Chrome()
    driver.get("https://www.madran.net/")
    driver.find_element_by_xpath('//*[@id="menu-item-3253"]/a').click()
    driver.find_element_by_xpath('//*[@id="menu-item-3254"]/a').click()
    driver.find_element_by_xpath('//*[@id="menu-item-4134"]/a').click()
    time.sleep(15)
    driver.close()
def instagir():
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/?hl=tr")
    driver.maximize_window()
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("mustafapaydaas")
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(sifre.sifre)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
    time.sleep(300)
def twitter():
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/login")
    driver.maximize_window()
    driver.find_element_by_name('session[username_or_email]').send_keys("mustafapaydass")
    driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').send_keys(sifre.sifre)
    driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div').click()
    time.sleep(300)
def sarki(sarkisim):
    dr = webdriver.Chrome()
    dr.get("https://www.youtube.com/?hl=tr&gl=TR")
    dr.find_element_by_xpath('//*[@id="search"]').send_keys(sarkisim)
    dr.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()
    degis = sarkisim.replace(" ", "+")
    dr.get('https://www.youtube.com/results?search_query=' + degis)
    dr.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string').click()
    time.sleep(300)

def kayit(soru=False):
    with sr.Microphone() as source:
        if soru:
            konusturma(soru)

        ses1 = r.listen(source)
        ses = ""
        try:
            ses = r.recognize_google(ses1, language="tr-TR")
        except sr.UnknownValueError:
            konusturma("Anlaşılmadı")
        return ses


def cevap(ses):
    if "adını söyler misin" in ses:
        konusturma("benim adım jarvis")
    if "müzik dinlemek istiyorum" in ses:
        sor = kayit("Hangi Müziği Dinlemek İstersiniz?")
        sarki(sor)
    if "ne olmak istiyorsun" in ses:
        konusturma("İnşallah Yapay Zeka")
    if "seni kodlayan" in ses:
        konusturma("mustafa paydaş tarafından yazıldım")
    if "nasılsın" in ses:
        konusturma("Bu Seni Hiç Alakadar Etmez")
    if "saat kaç" in ses:
        konusturma(datetime.datetime.now().strftime("%H:%M:%S"))
    if "İnternet'te arama yap" in ses:
        arama = kayit("Ne aramak İstiyorsun")
        url = "https://google.com/search?q=" + arama
        webbrowser.get().open(url)
        konusturma(arama + " için bulunanlar")
    if "çekilebilirsin" in ses:
        konusturma("sana mı soracağım aslanım")
        exit()
    if "hesabıma gir" in ses:
        instagir()
    if "video izlemek istiyorum" in ses:
        sor = kayit("Ne izlemek istersin")
        sarki(sor)
        konusturma("İyi Seyirler")
        time.sleep(150)
    if "aç" in ses:
        twitter()
    if "ödev var mı" in ses:
        konusturma("hocam bir daha bana ödev gönderme")
        dersSayfa()



def konusturma(string):
    tts = gTTS(string, lang="tr")
    dosyaisme = random.randint(1, 10000)
    dosya = "ses1 -" + str(dosyaisme) + ".mp3"
    tts.save(dosya)
    playsound(dosya)
    os.remove(dosya)

def uygulama():
    konusturma("Sizin için ne yapabilirim")

    while 1:
        ses = kayit()

        cevap(ses)

tkinter.Button(image=mikrofon,command=uygulama).pack(expand="YES")

tkinter.mainloop()
