from ast import Add
from tkinter import CASCADE
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name} ({self.code})"

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=50)
    postal = models.CharField(max_length=5)
    city = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.postal}, {self.street} in {self.city}"

    class Meta:
        verbose_name_plural = "Address Entries"
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete= models.CASCADE, null=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators = [MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    is_best_selling = models.BooleanField(default=False)
    published_countries = models.ManyToManyField(Country)
    
    def __str__(self):
        return f"{self.title} ({self.rating})"
