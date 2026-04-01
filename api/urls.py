from .views import *
from django.urls import path,include

urlpatterns = [
   path('movie/', movie_views),
   path('category/', category_views),
   path('genre/', genre_views),
   path('movie/<int:id>/', movie_detail_views),
   path('category/<int:id>/', category_detail_views),
   path('genre/<int:id>/', genre_detail_views),
]