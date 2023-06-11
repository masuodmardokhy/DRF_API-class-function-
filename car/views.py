from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status         # for show messages
from rest_framework import viewsets , permissions      # viewsets for class base view
from .models import *                     # * it means all
from .serializers import *


@api_view(['GET', 'POST'])
def person_view(request):     # this is function API
    if request.method == "GET":
        person = Person.objects.all()
        return Response(PersonSerializers(person, many=True).data, status=status.HTTP_200_OK)  #object to json

    elif request.method == "POST":
        ser = PersonSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonViwSet(viewsets.ModelViewSet):        # this is class base view API
    queryset = Person.objects.all()
    serializer_class = PersonSerializers
    http_method_names = ['get', 'post','put', 'delete']

    search_fields = ('name',)
    ordering_fields = '__all__'

    def list(self, request, *args, **kwargs):
        objs = super().list(request, *args, **kwargs)
        print('this is list')
        return objs

    def create(self, request, *args, **kwargs):
        obj = super().create(request, *args, **kwargs)
        print('this is create')
        return obj

    def update(self, request, *args, **kwargs):
        obj = super().update(request, *args, **kwargs)
        instance = self.get_object()
        print(' this is update:{}'.format(instance.name))
        return obj

    def retrieve(self, request, *args, **kwargs):         # request to database get one field (filter)
        obj = super().retrieve(request, *args, **kwargs)
        instance = self.get_object()
        print('this is retrive : {}'.format(instance.name))
        return obj

    def destroy(self, request, *args, **kwargs):     # for delete field
        instance = self.get_object()
        print('this is destroy : {}'.format(instance.name))
        obj = super().retrieve(request, *args, **kwargs)
        return obj



@api_view(['GET', 'POST'])
def car_view(request):                      # this is function API
    if request.method == "GET":
        car = Car.objects.all()
        return Response(CarSerializers(car, many=True).data, status=status.HTTP_200_OK)  #object to json

    elif request.method == "POST":
        ser = CarSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class CarViewSet(viewsets.ModelViewSet):       # this is class base view API
    queryset = Car.objects.all()
    http_method_names = ['get', 'post','put', 'delete']

    def get_serializer_class(self):
            if self.request.method not in permissions.SAFE_METHODS:
                return CarSerializers
            else:
                return CarReadSerializers
