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
    return HttpResponse('<h1> Welcome to Little Lemon </h1>')

def about(request):
    return HttpResponse(f'<h1> About us </h1>')

def menu(request):
    return HttpResponse(f'<h1> Menu </h1>')

def book(request):
    return HttpResponse(f'<h1> Make a booking </h1>')

def showform(request):
    return render(request, 'form.html')

def getform(request):
    if request.method == 'POST':
        name = request.POST['name']
        id = request.POST['id']
        return HttpResponse(f'Name: {name}  ID: {id}')