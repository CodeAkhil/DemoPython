# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MovieUpdateForm, MovieForm
from .models import Category, Movie
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.


def allprodcat(request, c_slug=None):
    c_page = None

    if c_slug is not None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Movie.objects.all().filter(category=c_page)

    else:
        products_list = Movie.objects.all().filter()
    paginator = Paginator(products_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'category.html', {'category': c_page, 'products': products})


@login_required()
def prodetail(request, c_slug, product_slug):
    try:
        product = Movie.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product})


@login_required()
def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('task_movieapp:allprodcat')
    else:
        form = MovieForm()

    return render(request, 'add.html', {'form': form})


@login_required()
def movie_update(request, product_slug):
    movie = get_object_or_404(Movie, slug=product_slug)
    if request.method == 'POST':
        form = MovieUpdateForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('task_movieapp:product_detail', c_slug=movie.category.slug, product_slug=movie.slug)
    else:
        form = MovieUpdateForm(instance=movie)
    return render(request, 'update.html', {'form': form})


@login_required()
def movie_delete(request, product_slug):
    if request.method == 'POST':
        movie = Movie.objects.get(slug=product_slug)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')


def home(request):
    return redirect(request, '/')
