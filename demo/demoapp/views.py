# from django.http import HttpResponse
from django.shortcuts import render
from . models import Trip

# Create your views here.


def home(request):
    tripcode = Trip.objects.all()
    return render(request, 'index.html', {'out': tripcode})
