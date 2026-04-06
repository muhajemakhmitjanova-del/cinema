from catalog.models import *
from rest_framework import serializers


# class ModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = (
#             'id','name', 'category', 'genre', 'raiting', 'description',
#             'image', 'directed_by', 'trailir_video', 'country', 'age_rating'
#         )
        
        
class Movieserializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length = 255)
    category = serializers.CharField(max_length = 255)
    genre = serializers.CharField(max_length = 255)
    raiting = serializers.FloatField()
    description = serializers.CharField(max_length = 255)
    image = serializers.ImageField()
    directed_by = serializers.CharField(max_length = 255)
    trailir_video = serializers.URLField()
    country = serializers.CharField(max_length = 255)
    age_rating = serializers.CharField(max_length = 255)
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.raiting = validated_data.get('raiting', instance.raiting)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.directed_by = validated_data.get('directed_by', instance.directed_by)
        instance.trailir_video = validated_data.get('trailir_video', instance.trailir_video)
        instance.country = validated_data.get('country', instance.country)
        instance.age_rating = validated_data.get('age_rating', instance.age_rating)
        
        return super().update(instance, validated_data)
    

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length = 255)
    slug = serializers.SlugField(max_length = 255)
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        
        return super().update(instance, validated_data)
  
    
    
class GenreSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length = 255)
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        
        return super().update(instance, validated_data)