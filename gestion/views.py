from django.shortcuts import render
from .models import Poll

# Create your views here.

def index(request):
    return render(request, 'index.html')

def polls(request):
    print(Poll.objects.all())
    return render(request, 'polls.html')

def voted(request):
    return render(request, 'voted.html')
