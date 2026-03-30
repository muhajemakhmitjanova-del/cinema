from django.shortcuts import render
from catalog.models import Movie, Category, Genre
from api.serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def movie_views(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies , many=True)
    
    return Response(serializer.data)
    
    
@api_view(['GET'])
def catalog_views(request):
    product = Category.objects.all()
    serializer = CategorySerializer(product , many = True)
    
    return Response(serializer.data)

    
