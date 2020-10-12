from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Hunter, Weapon

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
  weapons_hunter_doesnt_have = Weapon.objects.exclude(id__in = hunter.weapons.all().values_list('id'))
  return render(request, 'hunters/detail.html', { 'hunter': hunter, 'weapons': weapons_hunter_doesnt_have
 })

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

class WeaponList(ListView):
  model = Weapon

class WeaponDetail(DetailView):
  model = Weapon

class WeaponCreate(CreateView):
  model = Weapon
  fields = '__all__'

class WeaponUpdate(UpdateView):
  model = Weapon
  fields = ['name', 'type', 'rarity']

class WeaponDelete(DeleteView):
  model = Weapon
  success_url = '/weapons/'

def assoc_weapon(request, hunter_id, weapon_id):
  # Note that you can pass a toy's id instead of the whole object
  Hunter.objects.get(id=hunter_id).weapons.add(weapon_id)
  return redirect('detail', hunter_id=hunter_id)

