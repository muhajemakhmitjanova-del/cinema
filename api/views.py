from django.shortcuts import render
from catalog.models import Movie, Category, Genre
from api.serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET',"POST"])
def movie_views(request):
    if request.method == "GET":
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
    if request.method == "GET":
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
    if request.method == "GET":
        genre_list = Genre.objects.all()
        serializer = GenreSerializer(genre_list,many= True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = GenreSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = 201)



@api_view(['GET', "PUT", "DELETE"])
def movie_detail_views(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == "DELETE":
        movie.delete()
        return Response(status=204)
    

@api_view(['GET', "PUT", "DELETE"])
def category_detail_views(request, id):
    try:
        movie = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = CategorySerializer(movie)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = CategorySerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == "DELETE":
        movie.delete()
        return Response(status=204)
    


@api_view(['GET', "PUT", "DELETE"])
def genre_detail_views(request, id):
    try:
        movie = Genre.objects.get(id=id)
    except Genre.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == "DELETE":
        movie.delete()
        return Response(status=204)
    
