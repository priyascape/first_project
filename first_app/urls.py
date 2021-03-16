from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('blogs', views.root),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<num>', views.show),
    path('blogs/<num>/edit', views.edit),
    path('blogs/<num>/delete', views.destroy),
    path('blogs/json', views.json),

]