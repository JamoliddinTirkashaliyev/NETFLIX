from rest_framework import serializers
from .models import *

class AktyorSerializers(serializers.Serializer):
    ism = serializers.CharField()
    t_sana = serializers.DateField()
    davlat = serializers.CharField()
    jins = serializers.CharField()

class TarifSerializers(serializers.Serializer):
    nom = serializers.CharField()
    davomiylik = serializers.CharField()
    narx = serializers.IntegerField()

class KinoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kino
        fields = '__all__'
class KinoAktyorSerializers(serializers.ModelSerializer):
    class Meta:
        model = KinoAktior
        fields = '__all__'

