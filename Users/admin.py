from django.contrib import admin
from .models import CustomUser, Post, Place, CategoryClass
from django.contrib.auth.admin import UserAdmin


admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(Place)
admin.site.register(CategoryClass)

