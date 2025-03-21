from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms
from .forms import ProfileForm
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm  # Replace with your CustomUserCreationForm if you have one
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration
    template_name = 'register.html'
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
@login_required
def profile_view(request):
    return render(request, 'profile.html')
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
    return render(request, 'edit_profile.html', {'form': form})

