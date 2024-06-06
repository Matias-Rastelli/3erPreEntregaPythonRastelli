from django.contrib import admin
from .models import Cliente, Turno, Masaje


class MasajeAdmin(admin.ModelAdmin):
  list_display = ['nombre', 'descripcion', 'precio', 'duracion']
  search_fields = ['nombre']
class ClienteAdmin(admin.ModelAdmin):
  list_display = ['apellido', 'nombre', 'telefono']
  search_fields = ['apellido', 'nombre']
class TurnoAdmin(admin.ModelAdmin):
  list_display = ['cliente', 'fecha', 'hora', 'masaje']
  search_fields = ['cliente']
  
# Register your models here.
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Turno, TurnoAdmin)
admin.site.register(Masaje, MasajeAdmin)