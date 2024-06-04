from django.db import models

# Create your models here.

class book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()

    def __str__(self):
        return f"title is: {self.title}, rating is {self.rating}"