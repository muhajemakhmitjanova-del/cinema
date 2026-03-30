from rest_framework import serializers
from catalog.models import *


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'name', 'category', 'genre', 'raiting', 'description',
            'image', 'directed_by', 'trailir_video', 'country', 'age_rating'
        )
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name', 'slug',
        )
        
        
        
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            'name',
        )