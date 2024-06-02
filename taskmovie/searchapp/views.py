from django.shortcuts import render
from task_movieapp.models import Movie
from django.db.models import Q
# Create your views here.


def searchresult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Movie.objects.all().filter((Q(name__contains=query) | Q(description__contains=query)))
        return render(request, 'search.html', {'query': query, 'products': products})