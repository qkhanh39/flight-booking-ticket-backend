from rest_framework import serializers
from flight.models import Airport, Flight, Layover
from flight.utils import AirportValidator

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Airport
        fields  = ["name", "country"]
    
    def validate(self, attrs):
        AirportValidator()(attrs)
        return attrs
    