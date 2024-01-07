from django.contrib import admin
from django.urls import path
from .views import displayAll, addBook, deleteBook, searchBar

# Set the app name for namespacing URLs
app_name = 'library'

urlpatterns = [
    # Define the URL pattern for the home page, mapped to the displayAll view
    path('', displayAll, name='home'),

    # Define the URL pattern for adding a book, mapped to the addBook view
    path('add_book/', addBook, name='addBook'),

    # Define the URL pattern for deleting a book, mapped to the deleteBook view
    path('delete', deleteBook, name='delete'),

    # Define the URL pattern for searching books, mapped to the searchBar view
    path('search', searchBar, name='search'),
]
