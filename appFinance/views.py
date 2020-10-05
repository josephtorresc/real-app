from django.shortcuts import render

# Create your views here.

def view_finance(request):
    context = {}

    return render(request, 'appFinance/finance.html', context=context)