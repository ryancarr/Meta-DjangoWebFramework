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
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def book(request):
    return render(request, 'book.html')

def showform(request):
    return render(request, 'form.html')

def getform(request):
    if request.method == 'POST':
        name = request.POST['name']
        id = request.POST['id']
        return HttpResponse(f'Name: {name}  ID: {id}')