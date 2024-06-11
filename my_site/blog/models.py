from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Author(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Tag(models.Model):
    caption = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.caption}"

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=150)
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null = True, related_name="posts")
    content = models.TextField(validators=[MinLengthValidator(10)])
    tag = models.ManyToManyField(Tag)
    image = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
