from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class OfertaEmpleo(models.Model):
    titulo = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    experiencia = models.CharField(max_length=255)
    nivel_estudio = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
