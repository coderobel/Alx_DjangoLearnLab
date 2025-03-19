from django.urls import path, include
from django.views.generic import TemplateView
from .views import SignUpView
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
   # path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/profile', TemplateView.as_view(template_name = 'accounts/profile.html'), name = 'profile'),
    #path('signup/', SignUpView.as_view(),name = 'templates/registration/signup'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]