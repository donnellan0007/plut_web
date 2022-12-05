import uuid

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
    user = models.OneToOneField(User, on_delete=models.CASCADE, max_length=45, related_name='profile')
    description = models.TextField(max_length=150)
    gender = models.CharField(
        max_length=10,
        choices=GENDER,
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
    images = models.ImageField(upload_to='images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True,allow_unicode=True)

    def __str__(self):
        return f'{self.title}'

    def listing_slug(self):
        uuid_value = str(uuid.uuid4())
        unique_slug = slugify(uuid_value[0:12])
        return unique_slug
    def save(self, *args, **kwargs):
        self.slug = self.listing_slug()
        super().save(*args, **kwargs)