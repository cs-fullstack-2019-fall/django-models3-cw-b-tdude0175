from django.db import models

# Create your models here.

# Book model with name, pageNumber, genre, and publishDate attributes.

class Book(models.Model):
    name = models.CharField(max_length= 400)
    pageNumber = models.IntegerField(default=0)
    genre = models.CharField(max_length=200)
    publishDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} has the genre {self.genre}"