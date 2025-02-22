from django.shortcuts import render
from .models import Books
# Create your views here.

def book_list(request):
    books = Books.objects.all()
    context = {'book_list': books}
    return render(request, 'books/book_list.html',context)