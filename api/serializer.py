from rest_framework import serializers
from catalog.models import Movie, Category, Genre



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        
        
class Movieserializer(serializers.ModelSerializer):
    category = serializers.CharField()
    genre = GenreSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'

