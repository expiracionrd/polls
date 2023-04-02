from django.shortcuts import render
from .models import Poll, Author, Book, Category
from .helper.auth import startAuth
from .helper.keeper import saveForm
import json

# Create your views here.

def index(request):
    
    return render(request, 'index.html')

def polls(request):

    # // Solo usar durante pruebas
    print(request.POST) 

    # // Validación de inicio sesión
    form_data = request.POST
    name = form_data.get('your_name')
    print(name)
    startAuth(name)


    return render(request, 'polls.html')

def get_employee():
    return {'name': 'Bobby Hadz', 'vote': ''}

def voted(request):

    # // Solo usar durante pruebas
    print(request.POST)
    # if request.method == 'POST':


    # // Validación de selección.
    form_data = request.POST
    voto = form_data.get('elección')
    print(voto)
    
    data = {
        'ganador':[
        {
        'eleccion': voto
        }
        ]
    }
    
    json_str = json.dumps(data)
    print(json_str)
    jsonFile = open('data.json', 'a')
    jsonFile.write(json_str)
    jsonFile.close() 

    return render(request, 'voted.html')
