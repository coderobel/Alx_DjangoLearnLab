from rest_framework import serializers
from .models import Post
from rest_framework.authtoken.models import Token
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['bio', 'profile_picture', 'followers']