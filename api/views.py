from django.shortcuts import render
from catalog.models import Movie, Category, Genre
from api.serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET',"POST"])
def movie_views(request):
    if request.medhod == "GET":
        movi_list = Movie.objects.all()
        serializer = MovieSerializer(movi_list,many= True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = MovieSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = 201)
        
    
@api_view(['GET',"POST"])
def category_views(request):
    if request.medhod == "GET":
        category_list = Category.objects.all()
        serializer = CategorySerializer(category_list,many= True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = 201)

    
@api_view(['GET',"POST"])
def genre_views(request):
    if request.medhod == "GET":
        genre_list = Genre.objects.all()
        serializer = GenreSerializer(genre_list,many= True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = GenreSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = 201)


