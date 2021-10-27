from django.contrib import admin
from django.utils.html import format_html
from .models import Produkty, Producent, Kategoria


# Register your models here.
#admin.site.register(Produkty)
#admin.site.register(Producent)
#admin.site.register(Kategoria)

from django.contrib.admin import AdminSite

admin.site.site_header = 'Panel administracyjny'
admin.site.index_title = 'Strony administratora'




@admin.register(Produkty)
class ProduktyAdmin(admin.ModelAdmin):
    search_fields = ['nazwa']
    list_display = ['kategoria','producent','nazwa','opis','cena']
    list_filter =  ['nazwa']
    list_editable = ['nazwa']


@admin.register(Producent)
class ProducentAdmin(admin.ModelAdmin):
    list_display = ['nazwa','opis','showopis']
    list_editable = ['opis']

    def showopis(self, obj):
        if len(obj.opis) > 0:
            return format_html(f'<a href="{obj.opis}" target ="_blank">{obj.opis}</a>')
        else:
            return ''

    showopis.short_description = "strona www"

@admin.register(Kategoria)
class KategoriaAdmin(admin.ModelAdmin):
   pass