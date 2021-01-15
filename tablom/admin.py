from django.contrib import admin
from .models import Öğrenci
# Register your models here.
class Student(admin.ModelAdmin):
    list_display = ("id","isim","no","ders","saat")
    list_display_links = ("isim","no")
    list_filter = ("saat",)
    search_fields = ("id","isim","no")
    list_per_page = 10
admin.site.register(Öğrenci,Student)