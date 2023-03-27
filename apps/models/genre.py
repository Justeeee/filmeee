from django.db.models import Model, CharField


class Genre(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name