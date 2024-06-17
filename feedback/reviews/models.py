from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class review(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    your_review = models.TextField(max_length = 200)
    rating = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"username is: {self.username}, password is: {self.password}, your opinion & rating is: {self.your_review}({self.rating})"