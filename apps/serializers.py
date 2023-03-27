from rest_framework.serializers import ModelSerializer

from apps.models.author import Author
from apps.models.genre import Genre
from apps.models.movie import Movie


class MovieModelSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class GenreModelSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


