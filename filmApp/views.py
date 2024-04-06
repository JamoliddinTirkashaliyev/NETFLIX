from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

class HelloAPI(APIView):
    def get(self,request):
        data = {
            'message':"Hello World!"
        }
        return Response(data)

class AktyorlarAPI(APIView):
    def get(self,request):
        aktyorlar = Aktyor.objects.all()
        serializers = AktyorSerializers(aktyorlar,many=True)
        return Response(serializers.data)
    def post(self,request):
        aktyor = request.data
        serializers = AktyorSerializers(data=aktyor)
        if serializers.is_valid():
            data = serializers.validated_data
            Aktyor.objects.create(
                ism = data.get('ism'),
                t_sana = data.get('t_sana'),
                davlat = data.get('davlat'),
                jins = data.get('jins'),
            )
            return Response({'success': True, 'create_data': serializers.data})
        return Response({'success': False, 'errors': serializers.errors})


class AktyorAPI(APIView):
    def get(self,request,pk):
        aktyor = Aktyor.objects.get(id=pk)
        serializers = AktyorSerializers(aktyor)
        return Response(serializers.data)
    def put(self,request,pk):
        aktyor = Aktyor.objects.filter(id=pk)
        serializers = AktyorSerializers(aktyor.first(), data=request.data)
        if serializers.is_valid():
            data = serializers.validated_data
            aktyor.update(
                ism=data.get('ism'),
                t_sana=data.get('t_sana'),
                davlat=data.get('davlat'),
                jins=data.get('jins'),
            )
            serializers = AktyorSerializers(aktyor.first())
            return Response({'success': True, 'create_data': serializers.data})
        return Response({'success': False, 'errors': serializers.errors})
    def delete(self,request, pk):
        aktyor = Aktyor.objects.get(id=pk)
        aktyor.delete()
        return Response({'success': True, 'delete_data': serializers.data})

class TariflarAPI(APIView):
    def get(self,request):
        tariflar = Tarif.objects.all()
        serializers = TarifSerializers(tariflar,many=True)
        return Response(serializers.data)
    def post(self,request):
        tarif = request.data
        serializers = TarifSerializers(data=tarif)
        if serializers.is_valid():
            data = serializers.validated_data
            Tarif.objects.create(
                nom = data.get('nom'),
                davomiylik = data.get('davomiylik'),
                narx = data.get('narx')

            )
            return Response({'success': True, 'create_data': serializers.data})
        return Response({'success': False, 'errors': serializers.errors})

class TarifAPI(APIView):
    def get(self,request,pk):
        tarif = Tarif.objects.get(id=pk)
        serializers = TarifSerializers(tarif)
        return Response(serializers.data)
    def put(self,request,pk):
        tarif = Tarif.objects.filter(id=pk)
        serializers = TarifSerializers(tarif.first(), data=request.data)
        if serializers.is_valid():
            data = serializers.validated_data
            tarif.update(
                nom=data.get('nom'),
                davomiylik=data.get('davomiylik'),
                narx=data.get('narx')

            )
            serializers = TarifSerializers(tarif.first())
            return Response({'success': True, 'create_data': serializers.data})
        return Response({'success': False, 'errors': serializers.errors})


    def delete(self,request, pk):
        tarif = Tarif.objects.get(id=pk)
        tarif.delete()
        return Response({'success': True, 'delete_data': serializers.data})




