from rest_framework.exceptions import ValidationError

class AirportValidator:
    def __init__(self):
        self.max_length = 30
    def __call__(self, attrs):
        name = attrs.get('name')
        country = attrs.get('country')
        
        if name == "" or country == "":
            raise ValidationError("Name or country should be filled.")
        else:
            if len(name) > self.max_length:
                raise ValidationError("Name of the airport too long.")
            elif len(country) > self.max_length:
                raise ValidationError("Name of the country too long.")