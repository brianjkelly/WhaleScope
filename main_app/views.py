from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Sighting

# Create views below:
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class SightingList(ListView):
    model = Sighting

class SightingDetail(DetailView):
    model = Sighting

class SightingCreate(CreateView):
    model = Sighting
    fields = '__all__'

class SightingUpdate(UpdateView):
    model = Sighting
    fields = ['date', 'location', 'description']

class SightingDelete(DeleteView):
    model = Sighting
    success_url = '/sightings/'