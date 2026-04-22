from django.db import models

class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=30)
    year = models.DateField()
    price = models.IntegerField()
    car_type = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.brand} {self.model}"