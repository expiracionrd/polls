from django.shortcuts import render
from .models import Poll, Author, Book, Category
from .helper.auth import startAuth
from .helper.graphic import resultados
import json, io, base64, urllib
from django.contrib import messages
from django.contrib.messages import constants
from django.http import JsonResponse, HttpResponseRedirect



# Create your views here.

def index(request):
    
    return render(request, 'index.html')

# Verifica sí el usuario existe antes de votar
def polls(request):

    # // Solo usar durante pruebas
    print(request.POST) 

    # // Validación de inicio sesión
    form_data = request.POST
    name = form_data.get('your_name')
    print(name)
    startAuth(name)

    return render(request, 'polls.html')
    # return HttpResponseRedirect(request.POST.get('next'))


# Guarda la información del voto.

def voted(request):

    # // Solo usar durante pruebas
    print(request.POST)


    # // Validación de selección.
    form_data = request.POST
    voto = form_data.get('elección')
    print(voto)    

    # Abre el archivo JSON y carga su contenido en una lista de Python
    with open('data.json') as archivo:
        datos = json.load(archivo)

    # Crea un nuevo objeto JSON y agrégalo a la lista
    nuevo_objeto = {'eleccion': voto}
    datos.append(nuevo_objeto)

    # Guarda la lista modificada en el archivo JSON
    with open('data.json', 'w') as archivo:
        json.dump(datos, archivo)

    return render(request, 'voted.html')

def results(request):

    #Ejecuta el 'graphics.py' para añadir imagen de los resultados en el template.
    resultados()

    return render(request, 'resultados.html')


##########################

def getRoutes(request):
    routes = [
        'api/token',
        'api/token/refresh',
    ]

    return JsonResponse(routes, safe=False)