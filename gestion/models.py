from django.db import models
from django.forms import ModelForm

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)

class Poll(models.Model):
        title = models.CharField(max_length=255)
        description = models.TextField()
        avg = models.DecimalField(decimal_places=2, max_digits=4)
        Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']