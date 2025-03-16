from django.urls import path
from .views import BookListView
from .views import BookDetailView
from .views import BookCreateView
from .views import BookUpdateView
from .views import BookDeleteView

urlpatterns = [
    path('api/books', BookListView.as_view(), name = 'book_list_create' ),
    path('api/books/create', BookCreateView.as_view(), name = 'book_list_create'),
    path('api/books/update', BookUpdateView.as_view(), name = 'book_list_update'),
    path('api/books/delete',BookDeleteView.as_view(), name = 'book_list_delete'),
    path('api/books/<int:pk>', BookDetailView.as_view(), name = 'book_list_detail'),
]