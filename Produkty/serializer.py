from .models import Produkty, Producent, Kategoria
from rest_framework import serializers

### API ####
class ProduktySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produkty
        fields = ['id','kategoria','producent','nazwa','opis','cena']

class KategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kategoria
        fields = ['id','nazwa']

class ProducentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producent
        fields = ['id','nazwa']