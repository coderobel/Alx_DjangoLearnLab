from django.shortcuts import render
from .models import Book
# Create your views here.

def list_books(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html',context)