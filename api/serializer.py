
from catalog.models import *
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id','name', 'category', 'genre', 'raiting', 'description',
            'image', 'directed_by', 'trailir_video', 'country', 'age_rating'
        )
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
           'id', 'name', 'slug',
        )
        
        
        
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            'id','name',
        )