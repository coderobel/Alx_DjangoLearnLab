from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.Serializer)
    class Meta:
        model = Book
        fields = '__all__'
class AuthorSerializer(serializers.Serializer)
    class Meta:
        model = Author
        fields = ['name']