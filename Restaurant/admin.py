from django.contrib import admin

from .models import Cuisine,Restaurant,Menu,categoriemenu,MenuItem,Post,Commentaire

admin.site.register(Commentaire)
admin.site.register(Post)
admin.site.register(Cuisine)
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(categoriemenu)
admin.site.register(MenuItem)