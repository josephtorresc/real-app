from django.shortcuts import render

# Create your views here.

def login(request):
    
    context = {}

    return render(request, 'appUser/login.html', context=context)

def logout(request):
    return 0

def register(request):
    return 0