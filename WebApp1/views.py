from django.shortcuts import render, HttpResponse

from Servicios.models import Servicio
# Create your views here.



def Home(request):
    return render(request,"WebApp1/home.html")

def Servicios(request):
    
    servicios=Servicio.objects.all()
    
    return render(request,"WebApp1/servicios.html",{"servicios":servicios})

def Tienda(request):
    return render(request,"WebApp1/tienda.html")

def Blog(request):
    return render(request,"WebApp1/blog.html")

def Contacto(request):
    return render(request,"WebApp1/contacto.html")
    