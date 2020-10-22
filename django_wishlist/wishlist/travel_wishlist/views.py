from django.shortcuts import render, redirect
from .models import Place
from .forms import NewPlaceForm

# Create your views here.

def place_list(request):

    if request.method == 'POST':
        #Create new place
        form = NewPlaceForm(request.POST)   #Creating a form from data in the request
        place = form.save() #Creates a model object from form
        if form.is_valid(): #Validation against DB constraints
            place.save()    #Saves place to DB
            return redirect('place_list') #Reloads home page

    places = Place.objects.filter(visited = False).order_by('name')
    new_place_form = NewPlaceForm() #Used to create HTML
    return render(request, 'travel_wishlist/wishlist.html', {'places' : places, 'new_place_form' : new_place_form})


def places_visited(request):
    visited = Place.objects.filter(visited = True)
    return render(request, 'travel_wishlist/visited.html', {'visited' : visited})


def about(request):
    author = 'Brett'
    about = 'A website dedicated to creating a list of places to visit.'
    return render(request, 'travel_wishlist/about.html', {'author' : author, 'about' : about})