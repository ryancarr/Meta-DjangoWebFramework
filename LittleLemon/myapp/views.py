from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> Welcome to Little Lemon </h1>')

def showform(request):
    return render(request, 'form.html')

def getform(request):
    if request.method == 'POST':
        name = request.POST['name']
        id = request.POST['id']
        return HttpResponse(f'Name: {name}  ID: {id}')