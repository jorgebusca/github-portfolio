
from django.contrib import admin
from django.urls import path, include 
from practicaApp.views import views, IndexView,comprasViews, ventasViews, usuarioViews
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/token', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name ='password_reset_complete'), 
    path('', include("practicaApp.urls")),
    path('', IndexView),
    path('', IndexView),
   path('compras', comprasViews),
   path('ventas', ventasViews),
   path('usuarios', usuarioViews),
   path('home', views.home, name="home")  
    
]
