from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book
from .forms import ExampleForm

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
def raise_exception(request):
    try:
        pass
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")