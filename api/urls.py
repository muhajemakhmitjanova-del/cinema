from .views import *
from django.urls import path,include

urlpatterns = [
   path('movie/', movie_views),
   path('category/', category_views),
   path('genre/', genre_views),
]