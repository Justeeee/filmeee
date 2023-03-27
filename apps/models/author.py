from django.contrib.postgres.fields import ArrayField
from django.db.models import Model, CharField, DateTimeField, ForeignKey, SET_NULL, ImageField


class Author(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    photo = ImageField(upload_to='media/authors/')
    career = ArrayField(CharField(max_length=255), size=50, null=True)
    date_of_birth = DateTimeField()
    zodiac = CharField(max_length=255)
    genre = ForeignKey('apps.genre', SET_NULL)
    # films = ???? TODO add count of all films
    # first_film = ??? TODO add a year of first film
    # last_film = ??? TODO add a year of last film
    # last_film_name = ??? TODO add a name of last film

    best_films = ArrayField(CharField(max_length=255, size=10, null=True))
    best_series = ArrayField(CharField(max_length=255, size=10, null=True))

    def __str__(self):
        return self.first_name + " " + self.last_name