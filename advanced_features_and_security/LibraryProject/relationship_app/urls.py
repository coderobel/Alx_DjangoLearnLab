from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import list_books


urlpatterns = [
    path('relationship_app/',views.LibraryDetailView,name = 'relationship_app'),
    path('relationship_app/', views.list_books,name = 'relationship_app'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path("views.register", "LogoutView.as_view(template_name=")),
]