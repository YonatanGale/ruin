from django.db import models
from datetime import datetime
from core.models import BaseModel
from django.forms import model_to_dict
from crum import get_current_user

# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, Using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_update = user
        super(Category, self).save()

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')
    price = models.IntegerField(default=0, verbose_name='Precio')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    ci = models.CharField(max_length=10, unique=True, verbose_name='Ci')
    Birthday = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    addres = models.CharField(max_length=150, null=True, blank=True, verbose_name='Direccion')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

class Sale(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.names

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']

class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalles'
        ordering = ['id']

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

class buy(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    cant = models.IntegerField(default=0, verbose_name='Cantidad')
    cost = models.IntegerField(default=0, verbose_name='Costo')
    prov_name = models.CharField(max_length=150, verbose_name='Nombre de proveedor')
    descrip = models.CharField(max_length=150, verbose_name='Descripcion de compra')
    date_joined = models.DateTimeField(default=datetime.now, verbose_name= 'Fecha de registro')
    
    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        ordering = ['id']