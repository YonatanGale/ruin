from django.db import models
from datetime import datetime

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']

class employee(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    names = models.CharField(max_length=150, verbose_name='Nombres')
    ci =models.CharField(max_length=150, unique=True, verbose_name='CI')
    data_joined = models.DateField(default=datetime.now, verbose_name='Fecha de ingreso')
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']