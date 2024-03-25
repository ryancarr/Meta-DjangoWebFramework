from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('showform/', views.showform),
    path('getform/', views.getform),
]