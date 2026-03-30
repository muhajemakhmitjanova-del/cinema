from .views import *
from django.urls import path,include

urlpatterns = [
   path('movie/', movie_views),
   path('catalog/', catalog_views)
]
