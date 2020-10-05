from django.contrib import admin

from .models import Cuisine,Restaurant,Post,Commentaire,Meals,PictureRestau

admin.site.register(PictureRestau)
admin.site.register(Commentaire)
admin.site.register(Meals)
admin.site.register(Post)
admin.site.register(Cuisine)
admin.site.register(Restaurant)
