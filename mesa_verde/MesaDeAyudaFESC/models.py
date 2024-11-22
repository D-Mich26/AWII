from django.db import models

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    puesto = models.CharField(max_length=50)
    area = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Tecnico(models.Model):
    id_tecnico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Peticion(models.Model):
    STATUS_CHOICES = [
        ('En proceso', 'En proceso'),
        ('Testeo', 'Testeo'),
        ('Solucionado', 'Solucionado'),
    ]

    id_peticion = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=500)
    prioridad = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    fecha = models.DateField()
    solucion = models.TextField(max_length=300, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='En proceso')
    empleado_peticion = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    tecnico_peticion = models.ForeignKey('Tecnico', on_delete=models.SET_NULL, null=True, blank=True)
    imagen = models.ImageField(upload_to='imagenes_tickets/', blank=True, null=True)  # Asegúrate de tener este campo

    def __str__(self):
        return f"Ticket #{self.id_peticion} - {self.descripcion[:20]}"