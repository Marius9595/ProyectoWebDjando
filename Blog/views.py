from django.shortcuts import render
from Blog.models import Categoria, Post
# Create your views here.

def Blog(request):
    
    posts=Post.objects.all()
    
    return render(request,"Blog/blog.html",{"posts":posts})

def Categorias(request, categoria_id):
    
    categoria=Categoria.objects.get(id=categoria_id)
    
    posts=Post.objects.filter(categorias=categoria)
    
    return render(request, "Blog/categorias.html",{'categoria':categoria,"posts":posts})
    