from django.shortcuts import render

# Create your views here.

def view_rent(request):
    context = {}

    return render(request, 'appRent/rent.html', context=context)