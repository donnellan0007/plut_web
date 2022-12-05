from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile, Listing
from .forms import CreateListingForm, ProfileUpdateForm, UserUpdateForm, UserRegisterForm


# Create your views here.
def index(request):
    listings = Listing.objects.all()

    context = {
        'listings': listings,
    }
    return render(request, 'core/index.html', context)


def create_listing(request):
    if request.method == 'POST':
        form = CreateListingForm(request.POST, request.FILES)
        # set author to current user
        if form.is_valid():
            obj = form.save(commit=False)
            # obj.author current profile
            obj.author = request.user.profile
            obj.save()
            return redirect('index')
    else:
        form = CreateListingForm()
    context = {
        'form': form,
    }
    return render(request, 'core/create_listing.html', context)
