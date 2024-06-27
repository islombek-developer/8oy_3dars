from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .serialazers import TravelSerializer,HotelSerializer,KlassSerializer
from .models import Travel,Hotel,Klass


class TravelViev(APIView):
    def get(self,request:Response,pk:int=None):
        if pk:
            try:
                travel = Travel.objects.get(pk=pk)
                return Response(TravelSerializer(travel).data)
            except:
                return Response({'massage':'Bunday malumot topilmadi'})
      
        travel = Travel.objects.get(pk=pk)
        return Response({'travel':TravelSerializer(travel,many=True).data})
      

    def post(self,request:Response):
        serializer = TravelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        travel = serializer.save()
        return Response(TravelSerializer(travel).data)

        
    def put(self,request:Request,pk:int=None):
        if not pk:
            return Response({'massage':'Method PUT not allowed'})
        try:
            travel = Travel.objects.get(pk=pk)
            serializer = TravelSerializer(travel,data = request.data)
            serializer.is_valid()
            update_travel = serializer.save()
            return Response(TravelSerializer(update_travel).data)
        except:
            return Response({'massage':'Bunday malumot topilmadi'})
            
    def delete(self,request:Request,pk:int):
        if not pk:
            return Response({'massage':'Method Delete not allowed'})
        try:
            travel = Travel.objects.get(pk=pk)
            travel.delete()
            return Response({'massage':'success'})
        except:
            return Response({'massage':'Bunday malumot topilmadi'})

class HotelViev(APIView):
    def get(self,request:Response,pk:int=None):
        if pk:
            try:
                hotel = Hotel.objects.get(pk=pk)
                return Response(HotelSerializer(hotel).data)
            except:
                return Response({'massage':'Bunday malumot topilmadi'})
      
        hotel = Hotel.objects.get(pk=pk)
        return Response({'hotel':HotelSerializer(hotel,many=True).data})
      

    def post(self,request:Response):
        serializer = HotelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        hotel = serializer.save()
        return Response(HotelSerializer(hotel).data)

        
    def put(self,request:Request,pk:int=None):
        if not pk:
            return Response({'massage':'Method PUT not allowed'})
        try:
            hotel = Hotel.objects.get(pk=pk)
            serializer = HotelSerializer(hotel,data = request.data)
            serializer.is_valid()
            update_hotel = serializer.save()
            return Response(Hotel(update_hotel).data)
        except:
            return Response({'massage':'Bunday malumot topilmadi'})
            
    def delete(self,request:Request,pk:int):
        if not pk:
            return Response({'massage':'Method Delete not allowed'})
        try:
            hotel = Hotel.objects.get(pk=pk)
            hotel.delete()
            return Response({'massage':'success'})
        except:
            return Response({'massage':'Bunday malumot topilmadi'})


class KlassViev(APIView):
    def get(self,request:Response,pk:int=None):
        if pk:
            try:
                klass = Klass.objects.get(pk=pk)
                return Response(KlassSerializer(klass).data)
            except:
                return Response({'massage':'Bunday malumot topilmadi'})
      
        klass = Klass.objects.get(pk=pk)
        return Response({'klass':KlassSerializer(klass,many=True).data})
      

    def post(self,request:Response):
        serializer = KlassSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        klass = serializer.save()
        return Response(KlassSerializer(klass).data)

        
    def put(self,request:Request,pk:int=None):
        if not pk:
            return Response({'massage':'Method PUT not allowed'})
        try:
            klass = Klass.objects.get(pk=pk)
            serializer = KlassSerializer(klass,data = request.data)
            serializer.is_valid()
            update_klass = serializer.save()
            return Response(klass(update_klass).data)
        except:
            return Response({'massage':'Bunday malumot topilmadi'})
            
    def delete(self,request:Request,pk:int):
        if not pk:
            return Response({'massage':'Method Delete not allowed'})
        try:
            klass = Klass.objects.get(pk=pk)
            klass.delete()
            return Response({'massage':'success'})
        except:
            return Response({'massage':'Bunday malumot topilmadi'})
