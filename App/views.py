from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'App/home.html')

def dashboard(request):
    return render(request, 'App/dashboard.html')

def products(request):
    return render(request, 'App/products.html')

def customers(request):
    return render(request, 'App/customers.html')


