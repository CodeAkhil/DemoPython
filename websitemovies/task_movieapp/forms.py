from django import forms
from .models import Movie


class MovieUpdateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'releasedate', 'image', 'actors', 'link']


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'slug', 'description', 'releasedate', 'category', 'image', 'actors', 'link']
