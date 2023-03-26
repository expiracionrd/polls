from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)

class Poll(models.Model):
        title = models.CharField(max_length=255)
        description = models.TextField()
        avg = models.DecimalField(decimal_places=2, max_digits=4)
        Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    