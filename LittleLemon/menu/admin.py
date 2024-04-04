from django.contrib import admin
from .models import (
    Drinks, 
    DrinkCategory,
    Employee,
    )

admin.site.register(DrinkCategory)
admin.site.register(Drinks)
admin.site.register(Employee)