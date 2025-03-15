from rest_framework import serializers
from models import Author,Book

class BookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fields = '__all___'
class Authorserializer(serializers.Serializer):
    class Meta:
        model = Author
        fields = ['name']