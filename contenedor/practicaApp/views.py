from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from practicaApp.urls import IndexView, comprasViews, ventasViews, usuarioViews
from .models import usuario, productos, ventas
# Create your views here.


def IndexView(request):
    '''Esto es la pagina principal'''    
    return render(request, "index.html")

def ventasViews(request):
    venta = ventas.objects.all()# Trae todos los registros del modelo
    columnas = [field.name for field in ventas._meta.fields]  # Obtener nombres de columnas
    return render(request, "ventas.html", {"objeto":venta, "columnas": columnas})

def comprasViews(request):
    compra = productos.objects.all()# Trae todos los registros del modelo
    columnas = [field.name for field in productos._meta.fields]  # Obtener nombres de columnas
    return render(request, "compras.html", {"objeto":compra, "columnas": columnas})

def usuarioViews(request):
    usuarios = usuario.objects.all()# Trae todos los registros del modelo
    columnas = [field.name for field in usuario._meta.fields]  # Obtener nombres de columnas
    return render(request, "compras.html", {"objeto":usuarios, "columnas": columnas})

html_base = """
<h1>web mio</h1>
    <ul>
        <li><a href="">Inicio</a></li>
        <li><a href="/acercade">A Cerca de</a></li>
        <li><a href="/contacto">Contacto</a></li>       
        <li><a href="/usuarios">Usuarios</a></li>        
    </ul>    

"""

# Create your views here.


def acercade(request):
    '''Esto es la pagina A Cerca de'''    
    return render(request, "acercade.html")

def contacto(request):
    '''Esto es la pagina de contacto'''    
    return render(request, "contacto.html")

def usuarios(request):
    '''Esto es la pagina de usuarios'''    
    return render(request, "admin.html")
