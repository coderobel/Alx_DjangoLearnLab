from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms
from .forms import ProfileForm
from django.contrib import messages
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import BlogPost
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm  # Replace with your CustomUserCreationForm if you have one
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration
    template_name = 'blog/register.html'
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
@login_required
def profile_view(request):
    return render(request, 'blog/profile.html')
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'blog/edit_profile.html', {'form': form})
class blogpostListView(ListView):
    model = BlogPost
    template = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
class blogpostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
class blogpostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class blogpostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'  # Template for editing a post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
class blogpostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/post_confirm_delete.html'  # Confirmation template
    success_url = reverse_lazy('blogpost-list')  # Redirect after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
        
