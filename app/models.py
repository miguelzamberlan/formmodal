from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)

    year = models.PositiveSmallIntegerField(default=1980,
                                            validators=[
                                                MinValueValidator(1895),
                                                MaxValueValidator(2050),
                                            ]
                                            )

    rating = models.PositiveSmallIntegerField(default=5, choices=(
        (1, "★☆☆☆☆"),
        (2, "★★☆☆☆"),
        (3, "★★★☆☆"),
        (4, "★★★★☆"),
        (5, "★★★★★"),
    ))

    def __str__(self):
        return self.title
