from .views import *
from django.urls import path,include

urlpatterns = [
   path('movie/', movie_views),
   path('catalog/', category_views),
   path('catalog/', genre_views),
]