from django.contrib.postgres.fields import ArrayField
from django.db.models import Model, CharField, DateTimeField, ForeignKey, SET_NULL, IntegerField, TextField


# Create your models here.
class Movie(Model):
    title = CharField(max_length=255)
    date_realised = DateTimeField()
    country = CharField(max_length=255)
    genre = ForeignKey('apps.genre', SET_NULL)
    premiere = CharField(max_length=255)
    quality = IntegerField()
    author = ForeignKey('apps.author', SET_NULL)
    actors = ArrayField(ForeignKey('apps.author', SET_NULL))
    description = TextField()
    slogan = CharField(max_length=255, null=True)

    def __str__(self):
        if self.slogan:
            return self.title + " / " + self.slogan
        return self.title
