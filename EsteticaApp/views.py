from django.shortcuts import render
from .models import Masaje, Cliente, Turno
from .forms import ClientesForm, MasajesForm, TurnosForm

# Create your views here.
def home(req):
  return render(req, "home.html", {})

def masajes(req):
  list = Masaje.objects.all()
  return render(req, "masajes.html", {"list": list})

def clientes(req):
  list = Cliente.objects.all()
  return render(req, "clientes.html", {"list": list})

def turnos(req):
  list = Turno.objects.all()
  return render(req, "turnos.html", {"list": list})

def clientes_form(req):
  
  if req.method == "POST":

    miFormulario = ClientesForm(req.POST)

    if miFormulario.is_valid():
      data = miFormulario.cleaned_data
      new_cliente = Cliente(nombre=data['nombre'], apellido=data['apellido'], telefono=data['telefono'] )
      new_cliente.save()

      return render(req, "clientes_form.html", {"messege": "Curso creado con éxito"} )
    else:
      return render(req, "clientes_form.html", {"messege": "Datos inválidos"} )

  else: 

    miFormulario = ClientesForm()
    return render(req, "clientes_form.html", {"miFormulario":miFormulario } )
  
def masajes_form(req):
  
  if req.method == "POST":

    miFormulario = MasajesForm(req.POST)

    if miFormulario.is_valid():
      data = miFormulario.cleaned_data
      new_masaje = Masaje(nombre=data['nombre'], descripcion=data['descripcion'], precio=data['precio'], duracion=data['duracion'] )
      new_masaje.save()

      print("Masaje creado con éxito")
      return render(req, "home.html", {} )
    else:
      print("error en la validacion de datos")
      return render(req, "masajes_form.html", {} )

  else: 

    print("Entrando desde get")
    miFormulario = MasajesForm()
    return render(req, "masajes_form.html", {"miFormulario":miFormulario } )
  
def turnos_form(req):
  
  if req.method == "POST":

    miFormulario = TurnosForm(req.POST)

    if miFormulario.is_valid():
      data = miFormulario.cleaned_data
      new_turno = Turno(fecha=data['fecha'], hora=data['hora'], cliente=data['cliente'], masaje=data['masaje'] )
      new_turno.save()

      return render(req, "turnos_form.html", {"messege": "Turno creado con éxito"} )
    else:
      return render(req, "turnos_form.html", {"messege": "Datos inválidos"} )

  else: 

    miFormulario = TurnosForm()
    return render(req, "turnos_form.html", {"miFormulario":miFormulario } )
