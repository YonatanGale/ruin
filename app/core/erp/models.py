import decimal
from django.db import models
from datetime import datetime
from core.models import BaseModel
from django.forms import model_to_dict
from crum import get_current_user
from core.erp.choices import *


# Create your models here.
class Auditoria(models.Model):
    cod_auditoria = models.AutoField(primary_key=True)
    tabla = models.CharField(max_length=100)
    accion = models.CharField(max_length=1)
    datos_viejos = models.CharField(max_length=5000)
    datos_nuevos = models.CharField(max_length=5000)
    usuario = models.CharField(max_length=45)
    fecha = models.DateField(auto_now=True)

    def __str__(self):
        return self.tabla


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

class CategoryMaterials(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    unity = models.CharField(max_length=10, choices=unity_choices, default='ls', verbose_name='Unidad de medida')
    user_create = models.CharField(max_length=150, null=True)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    user_update = models.CharField(max_length=150, null=True)
    date_update = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['unity'] = {'id': self.unity, 'name': self.get_unity_display()}
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class MethodPay(models.Model):
    pay = models.CharField(max_length=50, choices=pay_choices, default='Efectivo', verbose_name='Metodo de pago')

    def __str__(self):
        return self.pay

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Metodo de pago'
        verbose_name_plural = 'Metodos de pagos'
        ordering = ['id']

class typeFunds(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Nombre de fondo')
    impo = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Fondo disponible')
    methodpay = models.ForeignKey(MethodPay, on_delete=models.CASCADE, verbose_name='Metodos aceptado')


    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['impo'] = format(self.impo, '.2f')
        return item

    class Meta:
        verbose_name = 'Tipo fondo'
        verbose_name_plural = 'Tipos fondos'
        ordering = ['id']

class CierreCaja(models.Model):
    typeF = models.ForeignKey(typeFunds, on_delete=models.CASCADE)
    tot = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de creación')

    def __str__(self):
        return self.typeF.name
    

    def toJSON(self):
        item = model_to_dict(self)
        item['impor'] = format(self.impor, '.2f')
        item['typeF'] = self.typeF.toJSON()
        item['tot'] = format(self.tot, '.2f')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Caja'
        verbose_name_plural = 'Cajas'
        ordering = ['id']
        
class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio')
    stock = models.IntegerField(default=0, verbose_name='Stock')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de creación')


    def __str__(self):
        return self.name
    
    def get_full_name(self):
        return '{} / {}'.format(self.name, self.cate.name)


    def toJSON(self):
        item = model_to_dict(self)
        item['full_name'] = self.get_full_name()
        item['cate'] = self.cate.toJSON()
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
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
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de creación')


    def __str__(self):
        return self.get_full_name

    def get_full_name(self):
        return '{} {} / {}'.format(self.names, self.surnames, self.ci)

    def toJSON(self):
        item = model_to_dict(self)
        item['Birthday'] = self.Birthday.strftime('%Y-%m-%d')
        item['full_name'] = self.get_full_name()
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

class Sale(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    methodpay = models.ForeignKey(MethodPay, on_delete=models.CASCADE, verbose_name='Metodo de pago')
    typfund = models.ForeignKey(typeFunds, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.names

    def toJSON(self):
        item = model_to_dict(self)
        item['cli'] = self.cli.toJSON()
        item['typfund'] = self.typfund.toJSON()
        item['methodpay'] = self.methodpay.toJSON()
        item['subtotal'] = format(self.subtotal, '.2f')
        item['iva'] = format(self.iva, '.2f')
        item['total'] = format(self.total, '.2f')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item

    def delete(self, using=None, keep_parements=False):
        for det in self.detsale_set.all():
            det.prod.stock += det.cant
            det.prod.save()
        super(Sale, self).delete()

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

class Materials(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cate = models.ForeignKey(CategoryMaterials, on_delete=models.CASCADE, verbose_name='Categoria')    
    stock = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name="Stock")
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name="Precio de compra")

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['stock'] = format(self.stock, '.2f')
        item['price'] = format(self.price, '.2f')
        item['full_name'] = '{} / {}'.format(self.name, self.cate.name)
        item['cate'] = self.cate.toJSON()
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
        return self.get_full_name

    def get_full_name(self):
        return '{} {} / {}'.format(self.names, self.surnames, self.ci)

    def toJSON(self):
        item = model_to_dict(self)
        item['full_name'] = self.get_full_name()
        return item

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['id']

class Buy(models.Model):
    prov = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    methodpay = models.ForeignKey(MethodPay, on_delete=models.CASCADE, verbose_name='Metodo de pago')
    typfund = models.ForeignKey(typeFunds, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prov.names

    def toJSON(self):
        item = model_to_dict(self)
        item['prov'] = self.prov.toJSON()
        item['typfund'] = self.typfund.toJSON()
        item['methodpay'] = self.methodpay.toJSON()
        item['subtotal'] = format(self.subtotal, '.2f')
        item['iva'] = format(self.iva, '.2f')
        item['total'] = format(self.total, '.2f')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item

    def delete(self, using=None, keep_parements=False):
        for det in self.detbuy_set.all():
            det.prod.stock -= (decimal.Decimal(det.cant))
            det.prod.save()
        super(Buy, self).delete()

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        ordering = ['id']

class DetBuy(models.Model):
    buy = models.ForeignKey(Buy, on_delete=models.CASCADE)
    prod = models.ForeignKey(Materials, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name="Cantidad")
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    def toJSON(self):
        item = model_to_dict(self)
        item['cant'] = format(self.cant, '.2f')
        item['buy'] = self.buy.toJSON() 
        item['prod'] = self.prod.toJSON()
        item['price'] = format(self.price, '.2f')
        item['subtotal'] = format(self.subtotal, '.2f')
        return item

    class Meta:
        verbose_name = 'Detalle de Compra'
        verbose_name_plural = 'Detalle de Compras'
        ordering = ['id']

class Production(models.Model):
    produc = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.produc.names

    def toJSON(self):
        item = model_to_dict(self)
        item['produc'] = self.produc.toJSON()
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item

    def delete(self, using=None, keep_parements=False):
        for det in self.detproduction_set.all():
            det.prod.stock += (decimal.Decimal(det.cant))
            det.prod.save()
        super(Production, self).delete()

    class Meta:
        verbose_name = 'Pruduccion'
        verbose_name_plural = 'Producciones'
        ordering = ['id']

class DetProduction(models.Model):
    crea = models.ForeignKey(Production, on_delete=models.CASCADE)
    prod = models.ForeignKey(Materials, on_delete=models.CASCADE)
    cant = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name="Cantidad")

    def __str__(self):
        return self.prod.name

    def toJSON(self):
        item = model_to_dict(self)
        item['cant'] = format(self.cant, '.2f')
        item['crea'] = self.crea.toJSON() 
        item['prod'] = self.prod.toJSON()
        return item

    class Meta:
        verbose_name = 'Detalle de produccion'
        verbose_name_plural = 'Detalle de producciones'
        ordering = ['id']

class Recycle(models.Model):
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    recy = models.CharField(max_length=10, choices=recycle_choices, default='Caducidad', verbose_name='Razon de retiro')
    cant = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name="Cantidad")

    def __str__(self):
        return self.prod.name

    def toJSON(self):
        item = model_to_dict(self)
        item['cant'] = format(self.cant, '.2f')
        item['prod'] = self.prod.toJSON()
        item['recy'] = {'id': self.recy, 'name': self.get_recy_display()}
        return item

    class Meta:
        verbose_name = 'Reciclar'
        verbose_name_plural = 'Reciclados'
        ordering = ['id']

class Fund(models.Model):
    typeF = models.ForeignKey(typeFunds, on_delete=models.CASCADE, verbose_name='Tipo de fondo')
    sale = models.ForeignKey(Sale, null=True, on_delete=models.CASCADE)
    buy = models.ForeignKey(Buy, null=True, on_delete=models.CASCADE)
    closing = models.ForeignKey(CierreCaja, null=True, on_delete=models.CASCADE, verbose_name='Apertura o cierre de caja')
    amount = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Importe')
    typeMove = models.CharField(max_length=50, verbose_name='Tipo de movimiento')
    methodpay = models.ForeignKey(MethodPay, on_delete=models.CASCADE, verbose_name='Metodos aceptado')
    payNro = models.CharField(max_length=150, null=True, verbose_name='Numero de tarjeta o cheque')
    payowner = models.CharField(max_length=150,  null=True, verbose_name='Titular de tarjeta o cheque')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de creación')


    
    def __str__(self):
        return self.typeMove

    def toJSON(self):
        item = model_to_dict(self, exclude=['buy', 'sale'])
        item['amount'] = format(self.amount, '.2f')
        item['typeF'] = self.typeF.toJSON()
        item['methodpay'] = self.methodpay.toJSON()
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Fondo'
        verbose_name_plural = 'Fondos'
        ordering = ['id']

class Withdraw(models.Model):
    typeF = models.ForeignKey(typeFunds, on_delete=models.CASCADE, verbose_name='Tipo de fondo')
    reason = models.CharField(max_length=150, verbose_name='Razon o motivo')
    cant = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name="Monto")
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de creación')


    def __str__(self):
        return self.typeF.name

    def toJSON(self):
        item = model_to_dict(self)
        item['cant'] = format(self.cant, '.2f')
        item['typeF'] = self.typeF.toJSON()
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Retiro'
        verbose_name_plural = 'Retiros'
        ordering = ['id']