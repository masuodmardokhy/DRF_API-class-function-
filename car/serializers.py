from rest_framework import serializers
from .models import *


class PersonSerializers(serializers.ModelSerializer):
     class Meta:
         model=Person
         fields = '__all__'


class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarReadSerializers(serializers.ModelSerializer):
    person=PersonSerializers()     #for show details person in answer
    class Meta:
        model = Car
        fields = '__all__'