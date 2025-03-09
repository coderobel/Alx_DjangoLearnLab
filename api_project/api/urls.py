from django.urls import path
from .views import BookListCreateAPIView
urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book-list'),  # Maps to the BookList view
]