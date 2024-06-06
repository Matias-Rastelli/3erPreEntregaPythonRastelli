from django.shortcuts import render
from .models import Masaje, Cliente, Turno


# Create your views here.
def home(req):

  return render(req, "home.html", {})

def masajes(req):
  list = Masaje.objects.all()
  print(list)
  return render(req, "masajes.html", {"list": list})

def clientes(req):

  list = Cliente.objects.all()
  return render(req, "clientes.html", {"list": list})

def turnos(req):
  list = Turno.objects.all()
  return render(req, "turnos.html", {"list": list})
