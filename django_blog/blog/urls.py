from django.urls import path, include
from django.views.generic import TemplateView
from .views import SignUpView
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
   # path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/profile', TemplateView.as_view(template_name = 'accounts/profile.html'), name = 'profile'),
    #path('signup/', SignUpView.as_view(),name = 'templates/registration/signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('register/', SignUpView.as_view(),  name='register'),
]