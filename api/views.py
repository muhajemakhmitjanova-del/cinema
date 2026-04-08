from catalog.models import Movie, Category, Genre
from api.serializer import Movieserializer, CategorySerializer, GenreSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET', 'PATCH', 'POST','PUT',])
def movie_views(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = Movieserializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = Movieserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST','PUT','PATCH'])
def category_views(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST','PUT'])
def genre_views(request):
    if request.method == "GET":
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_views(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = Movieserializer(movie)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = Movieserializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        movie.delete()
        return Response(status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_views(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        category.delete()
        return Response(status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def genre_detail_views(request, id):
    try:
        genre = Genre.objects.get(id=id)
    except Genre.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        genre.delete()
        return Response(status=204)