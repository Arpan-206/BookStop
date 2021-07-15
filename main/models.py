from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    shelf = models.ManyToManyField("shelf", related_name="books")
    description = models.TextField(default='Default')
    image = models.ImageField(upload_to='images/', default='images/no-image.jpg')
    rating = models.IntegerField(default=3)
    book_file = models.FileField(upload_to='books/', default='books/no-file.epub')

    def __str__(self):
        return f"{self.title} by {self.author}"

class shelf(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    