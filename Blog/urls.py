from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Blog.views import Categorias,Blog

urlpatterns = [
    path('',Blog, name="Blog"),
    path('categoria/<int:categoria_id>/',Categorias, name="Categoria"),

    
]