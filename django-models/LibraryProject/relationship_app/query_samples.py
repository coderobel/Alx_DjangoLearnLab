from .models import Book, Author

# First, get the Author object for 'John Doe'
author = Author.objects.get(name='John Doe')

# Then, filter the books by this Author object
books_by_author = Book.objects.filter(author=author)
