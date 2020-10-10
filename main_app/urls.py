from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('hunters/', views.hunters_index, name='index'),
  path('hunters/<int:hunter_id>/', views.hunters_detail, name='detail'),
  path('hunters/create/', views.HunterCreate.as_view(), name='hunters_create'),

]