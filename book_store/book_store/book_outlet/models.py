from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    best_selling = models.BooleanField(default = False )

    def __str__(self):
        return f"\ntitle is: {self.title},\n rating is: {self.rating},\n author is:{self.author}, \n Is it best-selling: {self.best_selling} "
