from django.db import models
from Accounts.models import Comptepayant,Comptegratuit
from django.urls import reverse
from django.contrib.sessions.backends.db import SessionStore
from Accounts.views import comptegratuit_login
from ckeditor.fields import RichTextField
import django.dispatch

class Cuisine(models.Model):
    intitule = models.CharField(max_length=20,primary_key=True)
    description = models.CharField(max_length=9000,null=True)
    def __str__(self):
        return f'{self.intitule}'
   

class Meals(models.Model):
    intitule = models.CharField(max_length=20,primary_key=True)
    description = models.CharField(max_length=9000,null=True)
    def __str__(self):
        return f'{self.intitule}'

class Restaurant(models.Model):
    PRICE = (
        ('cheap eats', 'cheap eats'),
        ('mide Rang', 'mide Rang'),
        ('Fine Dining', 'Fine Dining'),
    )
    directeur = models.ForeignKey(Comptepayant,on_delete=models.CASCADE) 
    cuisine = models.ManyToManyField(Cuisine, verbose_name='cuisine')
    meals = models.ManyToManyField(Meals, verbose_name='Meals')
    picture_default = models.ImageField(default='restau_pics/defaultrestau.png',upload_to='restau_pics')
    ville = models.CharField(max_length=20)
    intitule = models.CharField(max_length=200,unique=True)
    website = models.CharField(max_length=200,null=True,blank=True)
    menu = models.ImageField(default='menu_pics/defaultrestau.png',upload_to='restau_pics')
    email = models.EmailField(max_length=254)
    horaire = models.CharField(max_length=20)
    adresse = models.CharField(max_length=1000,unique=True)
    location = models.TextField(unique=True,null=True,blank=True)
    numtele = models.CharField(max_length=20)
    likes = models.ManyToManyField(Comptegratuit,related_name='restaurant',blank=True,null=True)
    price = models.CharField(max_length=50, choices=PRICE,null=True,blank=True)
    percentage = models.IntegerField("percentage", default=0)
    total_comme = 0
    total_rating = 0
    max_stars=5
    
  
    def get_percent(self,total,totalco):
        percent = 0
        add_comments = django.dispatch.Signal() 
        if self.total_comme > 0:
            self.total_rating = total
            self.total_comme = totalco
            percent = round(float(self.total_rating/self.total_votes) , 0)
        return percent
    
    def total_likes(self):
        return self.likes.count()
    
    def get_adress(self):
        return self.adresse
    def __str__(self):
        return f'{self.intitule}'
    def get_absolute_url(self):
        return reverse('index2')

class Post(models.Model):
    user = models.ForeignKey(Comptegratuit,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    description = RichTextField(null=True,blank=True)
    image = models.ImageField(default='restau_pics/defaultrestau.png',upload_to='restau_pics',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(Comptegratuit,related_name='posts')
    totallikes = models.IntegerField("total", default=0)
    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.user.utilisateur.username + 'post' + str(self.id)
    def get_absolute_url(self):
        return reverse('compteGratuitprofile', args=[self.user.utilisateur.username])



class Commentaire(models.Model):
    restaurant = models.ForeignKey(Restaurant,related_name="commentaire",on_delete=models.CASCADE)
    user = models.ForeignKey(Comptegratuit,on_delete=models.CASCADE)
    intitule = models.CharField(max_length=100)
    description = RichTextField(null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(default=1)
    
    def __str__(self):
        return '%s - %s' % (self.restaurant.intitule, self.user.utilisateur.username)

    def get_absolute_url(self):
        return reverse('detailrestau', args=[self.restaurant.intitule])

class PictureRestau(models.Model):
    restaurant = models.ForeignKey(Restaurant,related_name="restauimage",on_delete=models.CASCADE)
    image = models.ImageField(upload_to='restau_pics',blank=True,null=True)
    def __str__(self):
       return self.restaurant.intitule + "photo"
    def get_absolute_url(self):
        return reverse('index2')
