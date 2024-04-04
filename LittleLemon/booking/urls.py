from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.form_view, name='book'),
]