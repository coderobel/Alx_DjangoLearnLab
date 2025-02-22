from .models import Book, Author, Library

# Define or pass library_name
library_name = 'Central Library'  # Example library name

# First, get the Author object for 'John Doe'
author = Author.objects.get(name='John Doe')

# Then, filter the books by this Author object
books_by_author = Book.objects.filter(author=author)

# Get the Library object
library = Library.objects.get(name=library_name)

# Retrieve all books in the specific library
books = Book.objects.all()
authors = Author.objects.all()
for book in books:
    print(book)
for author in authors:
    print(author)