from django.db import models
from django.core import validators
from django.core.validators import MinValueValidator, MaxValueValidator

from django.utils.text import slugify
# Create your models here.


class author_name(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"The Author's name is: {self.first_name} {self.last_name}"


class book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    # author = models.CharField(null=True, max_length=100)

    # when author is deleted, it will also be cascaded onto the books with same author and it will be also be deleted
    author = models.ForeignKey(author_name, on_delete=models.CASCADE, null=True, related_name="all_books")
    # we set default value = null, ki agar kuch hoga bhi toh null ho jaega


    best_selling = models.BooleanField(default=False)
    sluged_url = models.SlugField(default="", null=False, db_index=True)

    # what the thing below does is, it will auto-write the slug field

    # def save(self,*args,**kwargs ):
    #     self.sluged_url = slugify(self.title)
    #     super().save(*args,**kwargs)

    def __str__(self):
        return f"\ntitle is: {self.title},\n rating is: {self.rating},\n author is:{self.author}, \n Is it best-selling: {self.best_selling} "
