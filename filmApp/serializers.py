from rest_framework import serializers

class AktyorSerializers(serializers.Serializer):
    ism = serializers.CharField()
    t_sana = serializers.DateField()
    davlat = serializers.CharField()
    jins = serializers.CharField()

class TarifSerializers(serializers.Serializer):
    nom = serializers.CharField()
    davomiylik = serializers.CharField()
    narx = serializers.IntegerField()