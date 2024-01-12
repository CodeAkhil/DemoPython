from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from . models import Links
# Create your views here.


def home(request):
    if request.method == 'POST':
        link_new = request.POST.get('page', '')
        urls = requests.get(link_new)
        # urls = requests.get("https://www.google.com/")
        beautysoup = BeautifulSoup(urls.text, 'html.parser')

        for k in beautysoup.find_all('a'):
            li_address = k.get('href')
            li_name = k.string
            Links.objects.create(address=li_address, stringname=li_name)
        return HttpResponseRedirect('/')
    else:
        data_values = Links.objects.all()
    return render(request, 'home.html', {'data_value': data_values})
