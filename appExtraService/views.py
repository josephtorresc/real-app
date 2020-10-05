from django.shortcuts import render

# Create your views here.

def view_extra_service(request):
    context = {}

    return render(request, 'appExtraService/extra_service.html', context=context)