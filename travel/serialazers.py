from rest_framework import serializers
from .models import Travel,Klass,Hotel
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io


class TravelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    conten = serializers.CharField()
    period = serializers.DateTimeField(read_only=True)
    price = serializers.IntegerField()
    klass = serializers.CharField()
    hotel = serializers.CharField()

class HotelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    price = serializers.IntegerField()

class KlassSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    price = serializers.IntegerField()