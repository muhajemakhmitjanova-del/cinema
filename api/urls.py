from .views import *
from django.urls import path,include

urlpatterns = [
   path('',include('api.yasg')),
   path("auth/", include("api.auth.urls")),
   path('movie/', MovieListCreate.as_view()),
   path('movie/<int:pk>/', MovieRetrieveUpdateDelete.as_view()),
   path('category/', CategoryListCreate.as_view()),
   path('category/<int:pk>/', CategoryRetrieveUpdateDelete.as_view()),
   path('genre/', GenreListCreate.as_view()),
   path('genre/<int:pk>/', GenreRetrieveUpdateDelete.as_view()),
]