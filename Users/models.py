from django.db import models
from django.contrib.auth import settings
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from autoslug import AutoSlugField

class CustomUser(AbstractUser):
    address = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=14)


class CategoryClass(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', unique=True)

    def __str__(self):
        return self.title


class Place(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    User = settings.AUTH_USER_MODEL
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    slug = AutoSlugField(populate_from='title', unique=True)
    content = models.TextField()
    description = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(to='CategoryClass', related_name='Categories', null=True, blank=True)
    places = models.ManyToManyField(to='Place', related_name='Places', null=True, blank=True)
    image = models.ImageField(upload_to="images/")
    published_at = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.title