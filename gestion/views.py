from django.shortcuts import render
from .models import Poll
from .helper.auth import startAuth, saveForm

# Create your views here.

def index(request):
    
    return render(request, 'index.html')

def polls(request):

    # // Solo usar durante pruebas
    print(request.POST) 

    # Validación de inicio sesión
    form_data = request.POST
    name = form_data.get('your_name')
    print(name)
    startAuth(name)


    return render(request, 'polls.html')

def voted(request):

    # Validación de selección.
    form_data = request.POST
    voto = form_data.get('elección', 'name')
    print(voto)
    saveForm(voto)

    return render(request, 'voted.html')


    
