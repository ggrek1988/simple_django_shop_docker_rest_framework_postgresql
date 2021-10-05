from django.shortcuts import render

# Create your views here.

from django.shortcuts import render #funckja odpowiedzialna za wyswietlanie html
from django.http import  HttpResponse
from .models import *

def index_f(request):
    zapytanie = Produkty.objects.all() #select * from Producty
    jeden_produkt = Produkty.objects.get(pk=3) #select * from Producty_produkty where id = 3
    kat = Produkty.objects.filter(kategoria = 1)  #select * from Producty_produkty where kategoria = 3
    kat_name = Kategoria.objects.get(pk=1)  # select * from Producty_kategoria where kategoria = 3
    kategoriav = Kategoria.objects.all()

    dane = {'kategoria_v1' : kategoriav}

    return render(request,'szablon.html',dane)

def kategoria_f(request,id):
    kategoria_user = Kategoria.objects.get(pk=id)
    katv = Produkty.objects.filter(kategoria=id)
    test = 'Lista produktów w kategorii'
    dane = {'produkt_v1' : katv,
            'tekst' : test
            }
    return render(request,'szablon_p.html',dane) # dane jest to informacja jakie dane beda pobierane z selecta kat

def produkt_f(request,id):
    produkt_user = Produkty.objects.get(pk=id)
    napis = "<h1>" + str(produkt_user.nazwa) + "</h1>" + \
        "<p>" + str(produkt_user.opis) + "</p>" + \
        "<p>" + str(produkt_user.cena) + "</p>"

    return HttpResponse(napis)
