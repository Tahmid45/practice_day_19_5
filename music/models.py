from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    instrument_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Album(models.Model):
    name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, related_name='albums', on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.name
