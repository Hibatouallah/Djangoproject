from django.contrib.auth.models import AbstractUser
from django.db import models
from location_field.models.plain import PlainLocationField
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.urls import reverse



class Utilisateur(AbstractUser):
    uncomptegratuit = models.BooleanField(default=False)
    uncomptepayant = models.BooleanField(default=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    slug = models.SlugField(null=True)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super(Utilisateur, self).save(*args,**kwargs)
    def __str__(self):
        return f'{self.username}'
    
    def get_absolute_url(self):
        return f"../compteGratuitprofile/{self.slug}"

class Comptegratuit(models.Model):
    utilisateur = models.OneToOneField(Utilisateur,on_delete=models.CASCADE)
    cin = models.CharField(max_length=20)
    website = models.CharField(max_length=50)
    description = models.CharField(max_length=9000,null=True)
    ville = models.CharField(max_length=20)
    photoprofil = models.ImageField(upload_to='profile_pics',null=True, blank=True)
    photocouverture = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    pays = models.CharField(max_length=10)
    codepostal = models.CharField(max_length=20)
    numtel =models.CharField(max_length=20)
    slug = models.SlugField(null=True)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.utilisateur.username)
        super(Comptegratuit, self).save(*args,**kwargs)
    
    def __str__(self):
        return f'{self.utilisateur.username}'

    def get_absolute_url(self):
        return f"../compteGratuitprofile/{self.slug}"

class Comptepayant(models.Model):
    utilisateur = models.OneToOneField(Utilisateur,on_delete=models.CASCADE)
    cin = models.CharField(max_length=20)
    photoprofil = models.ImageField(null=True,default='default.jpg',upload_to='media/')
    pays = models.CharField(max_length=10)
    codepostal = models.CharField(max_length=20)
    numtel =models.CharField(max_length=20)

    def __str__(self):
        return f'{self.utilisateur.username}'


"""
class ProfileCompteGratuit (models.Model):
    utilisateur = models.OneToOneField(Comptegratuit,null=True,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    bio = models.TextField()
    slug = models.SlugField(null=True)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.utilisateur)
        super(ProfileCompteGratuit, self).save(*args,**kwargs)
    def __str__(self):
        return f'{self.utilisateur}'

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = ProfileCompteGratuit.objects.create(utilisateur=kwargs['instance'])
post_save.connect(create_profile,sender=Comptegratuit)


"""