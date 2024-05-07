from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def addClient(request):
    return render(request, 'clients.html', {
        'title': 'Django test'
    })

