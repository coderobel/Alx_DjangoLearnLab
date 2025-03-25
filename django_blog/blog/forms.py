from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile, Comment, Post
from django.contrib.auth.models import User
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post','author','content','created_at','updated_at']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': ' Write your comment here....', 'rows': 4}),
            'author': forms.TextInput(attrs={'placeholder': 'Your Name'}),
        }
    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 10:
            raise forms.ValidationError("Comment text must be at least 10 characters long.")
        return text

    # Custom validation for the 'author' field
    def clean_author(self):
        author = self.cleaned_data.get('author')
        if not author:
            raise forms.ValidationError("Author name cannot be empty.")
        return author
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include 'tags'
        widgets = {
            'tags': forms.TextInput(attrs={'placeholder': 'Enter tags separated by commas'}),
        }