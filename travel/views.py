from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .serialazers import TravelSerializer
from .models import Travel


class TravelViev(APIView):
    def get(self,request:Response):
        travel = Travel.objects.all()
        return Response({'travel':TravelSerializer(travel,many = True).data})
    
