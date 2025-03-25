from django.urls import path, include
from django.views.generic import TemplateView
from .views import SignUpView,profile_view
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    blogpostListView,
    blogpostDetailView,
    blogpostCreateView,
    blogpostUpdateView,
    blogpostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile', TemplateView.as_view(template_name = 'accounts/profile.html'), name = 'profile'),
    path('signup/', SignUpView.as_view(),name = 'templates/registration/signup'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(),  name='register'),
    path('profile/', profile_view, name = 'profile'),
    path('', blogpostListView.as_view(), name='blogpost-list'),
    path('<int:pk>/', blogpostDetailView.as_view(), name='blogpost-detail'),
    path('post/new/', blogpostCreateView.as_view(), name='blogpost-create'),
    path('post/<int:pk>/update/', blogpostUpdateView.as_view(), name='blogpost-update'),
    path('post/<int:pk>/delete/', blogpostDeleteView.as_view(), name='blogpost-delete'),
    path('post/<int:pk>', blogpostDetailView.as_view(), name='blogpost-detail'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view, name='add_comment_to_post'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
]