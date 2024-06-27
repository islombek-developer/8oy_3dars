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

    def create(self, validated_data):
        return Travel().objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.conten = validated_data.get('conten',instance.conten)
        instance.naperiodme = validated_data.get('period',instance.period)
        instance.price = validated_data.get('price',instance.price)
        instance.klass = validated_data.get('klass',instance.klass)
        instance.hotel = validated_data.get('hotel',instance.hotel)
        instance.save()
        return instance

class HotelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    price = serializers.IntegerField()

class KlassSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    price = serializers.IntegerField()