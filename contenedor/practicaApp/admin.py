from django.contrib import admin
from.models import usuario, productos, ventas
# Register your models here.


class usuAdmin(admin.ModelAdmin):#creamos el modelo administrador 
    fields = ["nombre", "apellido", "DNI", "fecha_nac", "correo", "clave" ]# estos campos podemos editar para ingresar datos 
    list_display = ["nombre", "correo"]# lo que queremos mostrar 
    
                   
admin.site.register(usuario, usuAdmin)# registramos BBDD y Modelo admin

class productosAdmin(admin.ModelAdmin):
    fields = ["fecha_comp", "producto", "kilogramo", "precio", "cantidad"]
    list_display = ["fecha_comp", "producto", "precio"]
    
admin.site.register(productos, productosAdmin)

class ventasAdmin(admin.ModelAdmin):
    fields = ["fecha", "hamburguesa", "lomo", "chorizo", "cono_fritas", "milanesa", "pizza", "agua_chica", "agua_grande",  "cerveza_lata", "cerveza_litro"]
    list_display = ["fecha"]
    
admin.site.register(ventas, ventasAdmin)



