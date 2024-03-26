from django.shortcuts import render
from django.http import HttpResponse


def drinks(request, drink_name):
    drink = {
        'mocha': 'type of coffee',
        'tea': 'type of beverage',
        'lemonade': 'type of refreshment'
    }
    return HttpResponse(f'<h2> {drink_name} </h2> {drink[drink_name]}')

def home(request):
    return HttpResponse("Welcome to Little Lemon !")

def about(request):
    print(request.user)
    return HttpResponse("About us")

def menu(request):
    return HttpResponse("Menu for Little Lemon")

def book(request):
    return HttpResponse("Make a booking")

def showform(request):
    return render(request, 'form.html')

def getform(request):
    if request.method == 'POST':
        name = request.POST['name']
        id = request.POST['id']
        return HttpResponse(f'Name: {name}  ID: {id}')