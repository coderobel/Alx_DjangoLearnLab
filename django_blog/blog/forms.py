from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile, Comment, Post
from django.contrib.auth.models import User
from taggit.forms import TagField
from taggit.models import Tag
from django_select2.forms import Select2TagWidget
from django.forms.widgets import TextInput
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
    tags = TagField(
        widget=Select2TagWidget(
            attrs={'data-placeholder': 'Add tags separated by commas'}
        )
    )
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }
class TagWidget(TextInput):
    def __init__(self, attrs=None):
        default_attrs = {'placeholder': 'Enter tags separated by commas'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)

    def format_value(self, value):
        if value is None:
            return ''
        if isinstance(value, (list, tuple)):
            return ', '.join(value)
        return value