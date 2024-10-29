from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=75, verbose_name="Nombre")
    apellido = models.CharField(max_length=75, verbose_name="Apellido")
    DNI = models.CharField(max_length=12, verbose_name="DNI", null=False, blank=False)
    fecha_nac = models.DateField(verbose_name="Fecha Nacimiento", null=False, blank=False)
    correo = models.CharField(max_length=150, verbose_name="Correo", null=False, blank=False)
    clave = models.CharField(max_length=20, verbose_name="Clave", null=False, blank=False)
    
    class Meta:
        db_table = 'usuario'
        managed = True
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        
    def __str__(self) -> str:
        return self.nombre
    
class productos(models.Model):
    fecha_comp = models.DateField(verbose_name="Fecha Compra", null=False, blank=False)
    producto = models.CharField(max_length=75, verbose_name="Producto")
    kilogramo = models.IntegerField(verbose_name="kilogramo", null=False, blank=False)
    precio = models.IntegerField(verbose_name="Precio", null=False, blank=False)
    cantidad = models.IntegerField(verbose_name="Cantidad", null=False, blank=False)
    
    class Meta:
        db_table = 'productos'
        managed = True
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        
    def __str__(self) -> str:
        return self.producto
    
    
class ventas(models.Model):
    fecha = models.DateField(verbose_name="fecha", null=False, blank=False)  
    hamburguesa = models.IntegerField(verbose_name="hamburguesa", null=True, blank=True )
    lomo = models.IntegerField(verbose_name="lomo", null=True, blank=True)
    chorizo = models.IntegerField(verbose_name="chorizo", null=True, blank=True)
    cono_fritas = models.IntegerField(verbose_name="cono_fritas", null=True, blank=True) 
    milanesa = models.IntegerField(verbose_name="milanesa", null=True, blank=True) 
    pizza = models.IntegerField(verbose_name="pizza", null=True, blank=True)
    agua_chica = models.IntegerField(verbose_name="agua_chica", null=True, blank=True) 
    agua_grande = models.IntegerField(verbose_name="agua_grande", null=True, blank=True) 
    cerveza_lata = models.IntegerField(verbose_name="cerveza_lata", null=True, blank=True) 
    cerveza_litro = models.IntegerField(verbose_name="cerveza_litro", null=True, blank=True) 

    class Meta:
        db_table = 'venta'
        managed = True
        verbose_name = 'venta'
        verbose_name_plural = 'ventas'
        
    def __int__(self) -> int:
        return self.fecha
    