from django.db import models

# Define the Book model representing a book in the library
class Book(models.Model):
    # Define attributes for the Book model
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    format = models.CharField(max_length=10, default='Book Available')

    def __str__(self):
        # Define a string representation for the Book model
        return f"{self.title} by {self.author}"
