from django.urls import path
from . import views

urlpatterns = [
    path('films/', views.films, name='films')
]