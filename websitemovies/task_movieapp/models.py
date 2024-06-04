
from django.db import models
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name', 'slug',)
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

    def get_url(self):
        return reverse('task_movieapp:products_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Movie(models.Model):
    objects = None
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    releasedate = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='movie', blank=True)
    actors = models.TextField()
    link = models.URLField()

    def get_url(self):
        return reverse('task_movieapp:product_detail', args=[self.category.slug, self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'movie'
        verbose_name_plural = 'movies'

    def __str__(self):
        return '{}'.format(self.name)

    def is_valid(self):
        pass
