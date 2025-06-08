from django.db import models

# Create your models here.
class Airport(models.Model):
    name    = models.CharField(max_length=100)
    country = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'airport'
    
    def __str__(self):
        return f"Airport {self.name} - {self.country}"

class Flight(models.Model):
    price               = models.DecimalField(max_digits = 10, decimal_places=2)
    origin              = models.ForeignKey(Airport, related_name = 'departures', on_delete = models.CASCADE)
    destination         = models.ForeignKey(Airport, related_name = 'arrivals', on_delete = models.CASCADE)
    departure_datetime  = models.DateTimeField()
    duration            = models.DurationField()
    first_class_seats   = models.IntegerField()
    second_class_seats  = models.IntegerField()
    
    def __str__(self):
        return f"{self.origin.name} -> {self.destination.name} on {self.departure_datetime}"
    
    class Meta:
        db_table = 'flight'
        
class Layover(models.Model):
    flight      = models.ForeignKey(Flight, related_name = 'layovers', on_delete = models.CASCADE)
    airport     = models.ForeignKey(Airport, related_name = 'layovers', on_delete = models.CASCADE)
    duration    = models.IntegerField(help_text = "Duration in minutes")
    note        = models.TextField(blank = True)
    
    def __str__(self):
        return f"{self.flight_id} will stop at {self.airport_id.name} for {self.duration} minutes"
    class Meta:
        db_table = 'layover'