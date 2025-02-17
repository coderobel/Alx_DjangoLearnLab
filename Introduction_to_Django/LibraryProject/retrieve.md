# Retrieve a Book Instance

```python
from book_shelf.models import Book

# Retrieve the Book instance
book = Book.objects.get(title='1984', author='George Orwell')

# Display all attributes of the book
print(book.title, book.author, book.publication_year)

# Expected Output
# 1984 George Orwell 1949
