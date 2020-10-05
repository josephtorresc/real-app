from django.shortcuts import render

# Create your views here.

def view_apartment(request):
    context = {}

    return render(request, 'appApartment/apartment.html', context=context)