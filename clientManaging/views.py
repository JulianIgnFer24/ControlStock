from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    title = 'Django test'
    return render(request, 'index.html', {
        'title': title
    })

