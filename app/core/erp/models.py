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

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio')
    stock = models.IntegerField(default=0, verbose_name='Cantidad')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['cate'] = self.cate.toJSON()
        return item

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

    def toJSON(self):
        item = model_to_dict(self)
        item['Birthday'] = self.Birthday.strftime('%Y-%m-%d')
        return item

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

    def toJSON(self):
        item = model_to_dict(self)
        item['cli'] = self.cli.toJSON()
        item['subtotal'] = format(self.subtotal, '.2f')
        item['iva'] = format(self.iva, '.2f')
        item['total'] = format(self.total, '.2f')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item

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

    def toJSON(self):
        item = model_to_dict(self, exclude=['sale'])
        item['prod'] = self.prod.toJSON()
        item['price'] = format(self.price, '.2f')
        item['subtotal'] = format(self.subtotal, '.2f')
        return item

    class Meta:
        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalles'
        ordering = ['id']

class Unity(models.Model):
    name = models.CharField(max_length=150, verbose_name='Unidad de medida', unique=True)

    def __str__(self):
        return (self.name)

    def toJSON(self):
        item = model_to_dict(self)  
        return item

    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'
        ordering = ['id']

class Materials(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    stock = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name="Stock")
    uni = models.ForeignKey(Unity, on_delete=models.CASCADE, verbose_name="Unidad")
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name="Precio de compra")

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['uni'] = self.uni.toJSON()
        item['stock'] = format(self.stock, '.2f')
        item['price'] = format(self.price, '.2f')
        return item

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

class Supplier(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    ci = models.CharField(max_length=10, unique=True, verbose_name='RUC')
    email = models.CharField(max_length=150, unique=True, verbose_name='Correo electronico')
    phone = models.CharField(max_length=10, unique=True, verbose_name='Telefono')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')

    def __str__(self):
        return self.names

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['id']

class Buy(models.Model):
    prov = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prov.names

    def toJSON(self):
        item = model_to_dict(self)
        item['prov'] = self.prov.toJSON()
        item['subtotal'] = format(self.subtotal, '.2f')
        item['iva'] = format(self.iva, '.2f')
        item['total'] = format(self.total, '.2f')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item


    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        ordering = ['id']

class DetBuy(models.Model):
    buy = models.ForeignKey(Buy, on_delete=models.CASCADE)
    prodb = models.ForeignKey(Materials, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name="Cantidad")
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    def toJSON(self):
        item = model_to_dict(self)
        item['cant'] = format(self.cant, '.2f')
        item['buy'] = self.buy.toJSON() 
        item['prodb'] = self.prodb.toJSON()
        item['price'] = format(self.price, '.2f')
        item['subtotal'] = format(self.subtotal, '.2f')
        return item

    class Meta:
        verbose_name = 'Detalle de Compra'
        verbose_name_plural = 'Detalle de Compras'
        ordering = ['id']