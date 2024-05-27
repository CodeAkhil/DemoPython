from django.urls import path
from . import views

app_name = 'task_movieapp'

urlpatterns = [
    path('', views.allprodcat, name='allprodcat'),
    path('category/<slug:c_slug>/', views.allprodcat, name='products_by_category'),
    path('category/<slug:c_slug>/<slug:product_slug>/', views.prodetail, name='product_detail'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<slug:product_slug>/', views.movie_update, name='update'),
    path('delete/<slug:product_slug>/', views.movie_delete, name='delete'),
    path('', views.home, name='home'),

]
