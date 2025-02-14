from book_shelf.models import Book

# Retrieve the Book instance
book = Book.objects.get(title='1984', author='George Orwell')