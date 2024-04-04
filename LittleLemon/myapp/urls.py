from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    #path('showform/', views.showform),
    #path('getform/', views.getform),
    #path('drinks/<str:drink_name>', views.drinks, name='drinks'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
]