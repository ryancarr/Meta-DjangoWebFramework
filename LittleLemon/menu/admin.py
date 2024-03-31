from django.contrib import admin
from .models import (
    Drinks, 
    DrinkCategory,
    )

admin.site.register(DrinkCategory)
admin.site.register(Drinks)