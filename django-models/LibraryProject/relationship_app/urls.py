from django.urls import path
from .views import list_books


urlpatterns = [
    path('relationship_app/',views.LibraryDetailView,name = 'relationship_app'),
    path('relationship_app/', views.list_books,name = 'relationship_app'),
]