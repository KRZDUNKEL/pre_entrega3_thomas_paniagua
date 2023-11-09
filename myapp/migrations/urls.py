from django.urls import path
from . import views

urlpatterns = [
    path('create/category/', views.create_category, name='create_category'),
    # Paths para crear Product y Customer
    path('search/', views.search, name='search'),
]
