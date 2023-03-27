from django.shortcuts import render
from .models import Poll

# Create your views here.

def index(request):
    employees = employees
    return render(request, 'index.html', {'employees' : employees})

def polls(request):
    print(Poll.objects.all())
    return render(request, 'polls.html')

def voted(request):
    return render(request, 'voted.html')
