from django.shortcuts import render
from .models import Automobil

def lista_automoviles(request):
    automoviles = Automobil.objects.all()
    return render(request, 'automoviles.html', {'automoviles': automoviles})
