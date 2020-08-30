from django.db import models
from Accounts.models import Comptepayant,Comptegratuit
from django.urls import reverse
from django.contrib.sessions.backends.db import SessionStore
from Accounts.views import comptegratuit_login
from ckeditor.fields import RichTextField


class Cuisine(models.Model):
    intitule = models.CharField(max_length=20,primary_key=True)
    description = models.CharField(max_length=9000,null=True)
    def __str__(self):
        return f'{self.intitule}'

class Restaurant(models.Model):
    directeur = models.ForeignKey(Comptepayant,on_delete=models.CASCADE) 
    cuisine = models.ManyToManyField(Cuisine, verbose_name='cuisine')
    location = models.CharField(max_length=20)
    intitule = models.CharField(max_length=200)
    intitule_tag =  models.CharField(max_length=200,default='tag')
    website = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    horaire = models.CharField(max_length=20)
    adresse = models.CharField(max_length=1000)
    numtele = models.CharField(max_length=20)
    likes = models.ManyToManyField(Comptegratuit,related_name='restaurant')
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return f'{self.intitule}'
    """
    def get_cuisines(self):
        return "\n".join([p.cuisines for p in self.cuisine.all()])
    """

class Post(models.Model):
    user = models.ForeignKey(Comptegratuit,on_delete=models.CASCADE)
    #description = models.CharField(max_length=2000,null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='restau_pics',blank=True,null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(Comptegratuit,related_name='posts')
    
    
    def __str__(self):
        return self.user.utilisateur.username + 'post' + str(self.id)
    def get_absolute_url(self):
        return reverse('mespostes', args=[self.user.utilisateur.id])
    """
    def sample_view(self,request):
        current_user = request.user
        return current_user.id
    
    def save(self, request=False,*args,**kwargs):
     
        if self.image:
            small=rescale_image(self.image,width=100,height=100)
            self.image_small=SimpleUploadedFile(name,small_pic)

        if request and not self.user:
            print(request.user.id) 
            self.user = request.user.id
        super(Post, self).save(*args,**kwargs)
    """

"""     
class Image(models.Model):
    #restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True,blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(default='default.jpg',upload_to='restau_pics',blank=True,null=True)

    def __str__(self):
       return self.Restaurant.intitule + "Image"

"""
class Menu(models.Model):
    restaurant = models.OneToOneField(Restaurant,on_delete=models.CASCADE,primary_key=True)
    intitule= models.CharField(max_length=24, unique=True, verbose_name='menu name')
    slug = models.SlugField(max_length=24,null=True, unique=True, help_text='The slug is the URL friendly version of the menu name, so that this can be accessed at a URL like mysite.com/menus/dinner/.')
    description = models.CharField(max_length=128, null=True, blank=True, help_text='Any additional text that the menu might need, i.e. Served between 11:00am and 4:00pm.')
    order = models.PositiveSmallIntegerField(default=0, help_text='The order of the menu determines where this menu appears alongside other menus.')

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.intitule)
        super(Menu, self).save(*args,**kwargs)
    def __str__(self):
        return f'{self.intitule}'
    class Meta:
        ordering = ['order']

class categoriemenu(models.Model):
	menu = models.ForeignKey(Menu,on_delete=models.CASCADE) 
	intitule = models.CharField(max_length=32, verbose_name='menu category name')
	additional_text = models.CharField(max_length=128, null=True, blank=True, help_text='The additional text is any bit of related information to go along with a menu category, i.e. the \'Pasta\' category might have details that say \'All entrees come with salad and bread\'.')
	order = models.IntegerField(default=0, help_text='The order is the order that this category should appear in when rendered on the templates.')
	
	class Meta:
		verbose_name='menu category'
		verbose_name_plural='menu categories'
		ordering = ['order', 'intitule']

	def __str__(self):
		return self.intitule


class MenuItem(models.Model):
    categoriemenu = models.ManyToManyField(categoriemenu)
    intitule = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    prix = models.IntegerField()
    image = models.ImageField(upload_to='menu',null=True,blank=True)
    epicee = models.BooleanField(default=False)
    sans_gluten = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.intitule}'


class Commentaire(models.Model):
    restaurant = models.ForeignKey(Restaurant,related_name="commentaire",on_delete=models.CASCADE)
    user = models.ForeignKey(Comptegratuit,on_delete=models.CASCADE)
    intitule = models.CharField(max_length=100)
    description = RichTextField(null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='restaucommentaire',null=True,blank=True)
    likes = models.ManyToManyField(Comptegratuit,related_name='commentairelike')
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return '%s - %s' % (self.restaurant.intitule, self.user.utilisateur.username)

    def get_absolute_url(self):
        return reverse('detailrestau', args=[self.restaurant.intitule])