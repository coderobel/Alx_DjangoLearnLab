from django.contrib import admin
from .models import Book
from .models import CustomUser
# Register your models here.
admin.site.register(Book)
admin.ModelAdmin
admin.site.register(CustomUser, CustomUserAdmin)