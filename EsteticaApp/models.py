from django.db import models

# Create your models here.
class Masaje(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion = models.DurationField()

    def __str__(self):
        return f'{self.nombre} - {self.precio} - {self.duracion}'

    class Meta:
        verbose_name = 'Masaje'
        verbose_name_plural = 'Masajes'
        ordering = ('nombre',)

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nombre} {self.apellido} - tel: {self.telefono}'

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ('apellido', 'nombre')

class Turno(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    masaje = models.ForeignKey(Masaje, on_delete=models.CASCADE)

    def __str__(self):
        return f'Turno de {self.cliente} para {self.masaje} el {self.fecha} a las {self.hora}'

    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'
        ordering = ('fecha', 'hora')