from rest_framework import serializers
from .models import Post
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
class PostSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(max_length=255)
    class Meta:
        model = Post
        fields = ['bio', 'profile_picture', 'followers']
    class UserSerializer(serializers.ModelSerializer):
        token = serializers.CharField(max_length=255,source='auth_token.key', read_only=True)

        class Meta:
            model = get_user_model()
            fields = ['username', 'email', 'password', 'token']
            extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = get_user_model().objects.create_user(**validated_data)
            Token.objects.create(user=user)
            return user