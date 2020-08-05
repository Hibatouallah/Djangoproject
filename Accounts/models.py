from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from location_field.models.plain import PlainLocationField

class Place(models.Model):
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
class Utilisateur(AbstractUser):
    uncomptegratuit = models.BooleanField(default=False)
    uncomptepayant = models.BooleanField(default=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)


class Comptegratuit(models.Model):
    utilisateur = models.OneToOneField(Utilisateur,on_delete=models.CASCADE,primary_key=True)
    cin = models.CharField(max_length=20)
    website = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    ville = models.CharField(max_length=20)
    photoprofil = models.FileField(null=True)
    photocouverture = models.FileField(null=True)
    pays = models.CharField(max_length=10)
    codepostal = models.CharField(max_length=20)
    numtel =models.CharField(max_length=20)



class Comptepayant(models.Model):
    utilisateur = models.OneToOneField(Utilisateur,on_delete=models.CASCADE,primary_key=True)
    cin = models.CharField(max_length=20)
    pays = models.CharField(max_length=10)
    codepostal = models.CharField(max_length=20)
    numtel =models.CharField(max_length=20)

