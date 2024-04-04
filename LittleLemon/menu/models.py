from django.db import models

class DrinkCategory(models.Model):
    category_name = models.CharField(max_length=200)
    
class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField()
    category_id = models.ForeignKey(DrinkCategory, on_delete=models.PROTECT, default=None)

class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.last_name}, {self.first_name}'