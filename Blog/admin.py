from django.contrib import admin

from .models import Catergoria,Post

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    
    readonly_fields=('created','updated')
    
class PostAdmin(admin.ModelAdmin):
    
    readonly_fields=('created','updated')
    
admin.site.register(Catergoria,CategoriaAdmin)

admin.site.register(Post,PostAdmin)
    

