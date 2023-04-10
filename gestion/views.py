from django.shortcuts import render
from .models import Poll, Author, Book, Category
from .resource.graphic import resultados
from .helper.auth import startAuth
import json, io, base64, urllib
from django.contrib import messages
from django.contrib.messages import constants


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

    # # Abre el archivo JSON y carga su contenido en una lista de Python
    # with open(r'votantes.json') as archivo:
    #     nombres = json.load(archivo)

    # # Crea un nuevo objeto JSON y agrégalo a la lista
    # nuevo_objeto = {'your_name': name}
    # nombres.append(nuevo_objeto)

    # # Guarda la lista modificada en el archivo JSON
    # with open('votantes.json', 'w') as archivo:
    #     json.dump(nombres, archivo)


    return render(request, 'polls.html')


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

