from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book

def displayAll(request):
    # Retrieve all books from the database
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

def searchBar(request):
    # Retrieve the search query from the request
    query = request.GET.get('search')
    # Filter books based on the title containing the search query
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'index.html', {'books': books})

def addBook(request):
    if request.method == 'POST':
        # Retrieve form data from the POST request
        t = request.POST['title']
        a = request.POST['author']
        i = request.POST['isbn']
        f = request.POST['format']
        
        # Create a new Book object and set its attributes
        book = Book()
        book.title = t
        book.author = a
        book.isbn = i
        
        # Check the file format and set the format attribute accordingly
        if (f.lower() == '.pdf' or f.lower() == '.epub' or f.lower() == '.mobi'):
            book.format = 'Only ' + f
        else:
            book.format = 'Book Available'
        
        # Save the book to the database
        book.save()
        
        # Retrieve all books from the database
        books = Book.objects.all()
        return redirect('/')
    
    # Render the add_book.html template for GET requests
    return render(request, 'add_book.html')

def deleteBook(request):
    # Retrieve the book to delete based on the provided book ID
    select_book = Book.objects.get(id=request.GET['bookid'])
    # Delete the selected book
    select_book.delete()
    return HttpResponseRedirect("/")



"""    I am still working on this. Due to some personal problems. I was delayed for 1hour. As of now I am submiting my work...
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        print( f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}")

class EBook(Book):
    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format

    def display_info(self):
        print( super().display_info() + f"\nFile Format: {self.file_format}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_all_books(self):
        if not self.books:
            return "No books in the library."
        else:
            book_info = ""
            for book in self.books:
                book_info += book.display_info() + "\n" + "-" * 20 + "\n"
            print( book_info)

    def search_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None


def displayAll(request):
    library = Library()
    books = library.books
    return render(request, 'index.html', {'books': books})

def searchBar(request):
    query = request.GET.get('search')
    library = Library()
    books = [book.display_info() for book in library.search_book_by_title(query)]
    return render(request, 'index.html', {'books': books})

def deleteBook(request):
    library = Library()
    try:
        book_id = int(request.GET['bookid'])
        select_book = next((book for book in library.books if book.id == book_id), None)
        if select_book:
            library.books.remove(select_book)
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("Book not found.")
    except ValueError:
        return HttpResponse("Invalid book ID.")
"""