from django.shortcuts import render
from .models import Poll
from .helper.auth import startAuth

# Create your views here.

def index(request):
    
    return render(request, 'index.html')

def polls(request):

    print(request.POST)
    form_data = request.POST
    name = form_data.get('your_name')
    print(name)
    startAuth(name)


    return render(request, 'polls.html')

def voted(request):
    
    return render(request, 'voted.html')
