from django.shortcuts import render
from .models import Category, Product, Customer
from .forms import CategoryForm, ProductForm, CustomerForm, SearchForm

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoryForm()
    return render(request, 'form.html', {'form': form})

# Funciones similares para crear Product y Customer

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            # Realizar la búsqueda en la base de datos y obtener resultados
            results = Product.objects.filter(name__icontains=search_query)
            return render(request, 'search.html', {'results': results})
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})

# Create your views here.
