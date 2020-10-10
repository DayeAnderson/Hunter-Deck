from django.shortcuts import render
from .models import Hunter

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def hunters_index(request):
  hunters = Hunter.objects.all()
  return render(request, 'hunters/index.html', { 'hunters': hunters })


