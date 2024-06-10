from django.db import models
from django.core import validators
from django.core.validators import MinValueValidator, MaxValueValidator

from django.utils.text import slugify
# Create your models here.


class address(models.Model):
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    pin_code = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.city}, {self.state}, {self.pin_code}"

    class Meta:
        verbose_name_plural = "Address Entries"


class author_name(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = "Countries"

class book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    # author = models.CharField(null=True, max_length=100)

    # when author is deleted, it will also be cascaded onto the books with same author and it will be also be deleted
    author = models.ForeignKey(
        author_name, on_delete=models.CASCADE, null=True, related_name="all_books")
    # we set default value = null, ki agar kuch hoga bhi toh null ho jaega

    best_selling = models.BooleanField(default=False)

    country_book = models.ManyToManyField(country)

    sluged_url = models.SlugField(default="", null=False, db_index=True)

    # what the thing below does is, it will auto-write the slug field

    # def save(self,*args,**kwargs ):
    #     self.sluged_url = slugify(self.title)
    #     super().save(*args,**kwargs)

    def __str__(self):
        return f"\ntitle is: {self.title},\n rating is: {self.rating},\n author is:{self.author}, \n Is it best-selling: {self.best_selling} "
