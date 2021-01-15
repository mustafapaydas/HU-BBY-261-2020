from django.shortcuts import render,redirect
from .models import Öğrenci
# Create your views here.

def anasayfa(request):
    ogrenciler= Öğrenci.objects.all()
    return render(request, "anasayfa.html",{"stud": ogrenciler})
def addÖğrenci(request):
    if request.method == "GET":
        return redirect("/")
    else:
        title = request.POST.get("title")
        title1 = request.POST.get("title1")
        title2 = request.POST.get("title2")
        newOgrenci = Öğrenci(isim= title,no=title1,ders=title2)

        newOgrenci.save()
        return redirect("/")

