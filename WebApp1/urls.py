from django.urls import path, include
from WebApp1 import views


urlpatterns = [
    path('', views.Home, name="Home"),
    path('Tienda/',views.Tienda, name="Tienda"),
    path('contacto/',views.Contacto,name="Contacto" )
    
]