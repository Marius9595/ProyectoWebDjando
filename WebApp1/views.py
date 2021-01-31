from django.shortcuts import render, HttpResponse


# Create your views here.



def Home(request):
    return render(request,"WebApp1/home.html")



def Tienda(request):
    return render(request,"WebApp1/tienda.html")

def Blog(request):
    return render(request,"WebApp1/blog.html")

def Contacto(request):
    return render(request,"WebApp1/contacto.html")
    