from django.shortcuts import render
from flight.serializers import AirportSerializer
from flight.models import Airport, Flight
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView


# Create your views here.    
class AirportListView(ListAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    
class AirportCreateView(CreateAPIView):
    serializer_class = AirportSerializer