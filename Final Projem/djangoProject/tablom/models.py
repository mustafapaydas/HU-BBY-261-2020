from django.db import models

# Create your models here.

class Öğrenci(models.Model):
    isim = models.CharField(max_length=20,verbose_name="İsim")
    no= models.CharField(max_length=8,verbose_name="Okul Numara")
    ders = models.TextField(max_length=160,verbose_name="Aldığı Dersler")
    saat = models.DateTimeField(auto_now_add=True,verbose_name="Tarih")

    def __str__(self):
        return self.isim
