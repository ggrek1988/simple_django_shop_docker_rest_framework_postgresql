from django.shortcuts import render

# Create your views here.

from django.shortcuts import render #funckja odpowiedzialna za wyswietlanie html
from django.http import  HttpResponse
from .models import *
from rest_framework import  viewsets
from .serializer import  KategoriaSerializer, ProduktySerializer


def index_f(request):
    #zapytanie = Produkty.objects.all() #select * from Producty
    #jeden_produkt = Produkty.objects.get(pk=3) #select * from Producty_produkty where id = 3
    #kat = Produkty.objects.filter(kategoria = 1)  #select * from Producty_produkty where kategoria = 3
    #kat_name = Kategoria.objects.get(pk=1)  # select * from Producty_kategoria where kategoria = 3
    kategoriav = Kategoria.objects.all()

    dane = {'kategoria_v1' : kategoriav}

    return render(request,'szablon.html',dane)

def kategoria_f(request,id):
    kategoria_user = Kategoria.objects.get(pk=id)
    #katv = Produkty.objects.filter(kategoria=id)
    kategoria_produkt = Produkty.objects.filter(kategoria = kategoria_user)
    kategoriav = Kategoria.objects.all()
    dane = {'kategoria_user' : kategoria_user,
            'kategoria_produkt' : kategoria_produkt,
            'kategoria_v1' : kategoriav
             }
    return render(request,'kategoria_produkt.html',dane) # dane jest to informacja jakie dane beda pobierane z selecta kat

def produkt_f(request,id):
    produkt_user = Produkty.objects.get(pk=id)
    kategoriav = Kategoria.objects.all()
    print( produkt_user)
    dane = {'produkt_user' : produkt_user , 'kategoria_v1' : kategoriav}

    return render(request,'produkt.html',dane)

##############API######################API########################API#######################API#####

class ProduktyViewSet(viewsets.ModelViewSet):
    queryset = Produkty.objects.all()
    serializer_class = ProduktySerializer

class KategoriaViewSet(viewsets.ModelViewSet):
    queryset = Kategoria.objects.all()
    serializer_class = KategoriaSerializer

class ProducentViewSet(viewsets.ModelViewSet):
        queryset = Producent.objects.all()
        serializer_class = KategoriaSerializer
