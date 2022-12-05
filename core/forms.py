from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Listing

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['description', 'gender']

class CreateListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ['title', 'description', 'images', 'price']

    def clean(self):
        cleaned_data = super().clean()
        images = cleaned_data.get('images')
        if not images:
            raise forms.ValidationError('Please upload an image')
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')
        price = cleaned_data.get('price')


    def __init__(self, *args, **kwargs):
        super(CreateListingForm, self).__init__(*args, **kwargs)
        self.fields['images'].required = False