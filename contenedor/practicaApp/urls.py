from django.urls import path
from practicaApp.views import IndexView, ventasViews, comprasViews, usuarioViews
from core import views


urlpatterns = [
   path('', IndexView),
   path('compras', comprasViews),
   path('ventas', ventasViews),
   path('usuarios', usuarioViews),
   path('home', views.home, name="home")  
]

