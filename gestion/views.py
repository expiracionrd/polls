from django.shortcuts import render
from .models import Poll

# Create your views here.

def index(request):
    # if request.GET['your_name']:                  #! Pendiente de revisión
    #     encontrado = request.GET['your_name']
    #     nameLooking = 

    return render(request, 'index.html')

def polls(request):
    print(Poll.objects.all())
    return render(request, 'polls.html')

def voted(request):
    return render(request, 'voted.html')
