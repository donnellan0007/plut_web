from django.db import models
from django.contrib.auth.models import  User
from django.utils.text import slugify
# Create your models here.

class Profile(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'

    GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, max_length=45)
    description = models.TextField(max_length=150)
    gender = models.CharField(
        max_length=10,
        choices=(GENDER),
        default=MALE,
    )
    verified = models.BooleanField(default=False)
    slug = models.SlugField(unique=True,allow_unicode=True)

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

class Listing(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=350, blank=True, null=True)
    images = models.ImageField()