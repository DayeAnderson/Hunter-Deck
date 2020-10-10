from django.shortcuts import render
from django.views.generic.edit import CreateView
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


