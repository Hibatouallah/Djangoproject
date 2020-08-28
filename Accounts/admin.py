from django.contrib import admin
from .models import Utilisateur,Comptegratuit,Comptepayant

admin.site.register(Utilisateur)
admin.site.register(Comptegratuit)
admin.site.register(Comptepayant)

