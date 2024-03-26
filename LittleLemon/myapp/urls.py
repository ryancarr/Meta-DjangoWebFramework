from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('showform/', views.showform),
    path('getform/', views.getform),
    path('drinks/<str:drink_name>', views.drinks, name='drinks'),
    path('aboutus/', views.about),
    path('menu/', views.menu),
    path('book/', views.book),
]