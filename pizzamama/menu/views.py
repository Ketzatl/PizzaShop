from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza


# Create your views here.

def index(request):
    # pizzas = Pizza.objects.all()
    # pizzas_list_names_and_prices = [pizza.nom + ' : ' + str(pizza.prix) + '€' for pizza in pizzas]
    # pizzas_names_list_str_prices = ', '.join(pizzas_list_names_and_prices)
    # return HttpResponse("Les Pizzas disponibles : " + pizzas_names_list_str_prices)
    pizzas = Pizza.objects.all()
    return render(request, 'menu/index.html', {'pizzas': pizzas})
