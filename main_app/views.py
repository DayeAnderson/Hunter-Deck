from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Hunter

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def hunters_index(request):
  hunters = Hunter.objects.all()
  return render(request, 'hunters/index.html', { 'hunters': hunters })

def hunters_detail(request, hunter_id):
  hunter = Hunter.objects.get(id=hunter_id)
  return render(request, 'hunters/detail.html', { 'hunter': hunter })

class HunterCreate(CreateView):
  model = Hunter
  fields = ['name', 'rank', 'gender', 'favorite_meal']
  success_url = '/hunters/'

class HunterUpdate(UpdateView):
  model = Hunter
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['name', 'rank', 'favorite_meal']

class HunterDelete(DeleteView):
  model = Hunter
  success_url = '/hunters/'


