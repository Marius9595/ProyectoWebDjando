from django.urls import path
from WebApp1 import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('Servicios/',views.Servicios, name="Servicios"),
    path('Tienda/',views.Tienda, name="Tienda"),
    path('Blog/',views.Blog, name="Blog"),
    path('contacto/',views.Contacto,name="Contacto" )
    
]