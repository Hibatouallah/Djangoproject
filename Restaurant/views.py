from django.shortcuts import render,get_object_or_404
from .models import Restaurant,Post,Commentaire,Cuisine,PictureRestau
from Accounts.models import Utilisateur,Comptegratuit,Comptepayant
from django.views.generic import ListView,DetailView,CreateView ,UpdateView,DeleteView
from django.forms import modelformset_factory
from.form import PostForm , CommentaireForm , RestaurantForm ,PhotoForm,UpdateCommentaireForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
import json
from django.http import JsonResponse
from django.core.paginator import Paginator
from .filters import RestaurantFilter
from geopy.geocoders import Nominatim


def compteGratuitprofile(request,slug):
    profileCG = Comptegratuit.objects.filter(slug=slug)
    usercg = Comptegratuit.objects.get(slug=slug)
    post = Post.objects.filter(user=usercg)
    print(post)
    return render(request,'../templates/Restaurant/profile.html', {'profileCG': profileCG ,'post': post})

def index(request):
    res = requests.get('https://ipinfo.io')
    data = res.json()
    city = data['city']
    restau = Restaurant.objects.filter(ville=city)  
    """ Pagination """
    restau_filter = RestaurantFilter(request.GET,queryset=restau)
    paginator = Paginator(restau_filter.qs, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'../templates/Restaurant/index.html', {'page_obj': page_obj,'restau': restau ,'restau_filter':restau_filter,'city':city})




def detailrestau(request,intitule):
    restau = Restaurant.objects.filter(intitule=intitule.replace('-',' '))
    res = get_object_or_404(Restaurant,intitule=intitule.replace('-',' '))
    total = res.total_likes()
    Picture = PictureRestau.objects.filter(restaurant=res)
    """ Pagination """
    commentaire = Commentaire.objects.filter(restaurant=res) 
    paginator = Paginator(commentaire, 2) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    #return render(request,'../templates/Restaurant/detailRestau.html', {'restau': restau ,'total':total,'mapbox_access_token':mapbox_access_token,'longitude':loc.longitude,'latitude':loc.latitude,'picture':Picture,'page_obj':page_obj})
    return render(request,'../templates/Restaurant/detailRestau.html', {'restau': restau ,'total':total,'picture':Picture,'page_obj':page_obj})


def LikeView(request,pk):
    restau = get_object_or_404(Restaurant,id=pk)
    user = Comptegratuit.objects.get(utilisateur=request.user.id)
    restau.likes.add(user)
    return HttpResponseRedirect(reverse('index'))
 
def LikePostView(request,pk):
    url = request.META.get('HTTP_REFERER')
    post = get_object_or_404(Post,id=pk)
    user = Comptegratuit.objects.get(utilisateur=request.user.id)
    post.likes.add(user)
    total=post.total_likes()
    Post.objects.filter(id=pk).update(totallikes=total)
    return HttpResponseRedirect(url)

class AjouterPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'Restaurant/ajouter_post.html'
    def form_valid(self, form):
        form.instance.user = Comptegratuit.objects.get(utilisateur=self.request.user)
        return super().form_valid(form)

def ajouterCommentaire(request,pk):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            """ for adding comment """
            data = Commentaire()
            data.restaurant = Restaurant.objects.get(id=pk)
            data.user = Comptegratuit.objects.get(utilisateur=request.user)
            data.intitule = form.cleaned_data['intitule']
            data.description = form.cleaned_data['description']
            data.rate = form.cleaned_data['rate']
            data.save()
            """ for rating """
            res = get_object_or_404(Restaurant,id=pk)
            listecommanteire =  Commentaire.objects.filter(restaurant=res)
            totalrate = 0
            k=0
            for i in listecommanteire:
                k=k+1
                totalrate = totalrate+ i.rate
            t = Restaurant.objects.get(id=pk)
            result =  round(float(totalrate/k) , 0)
         
            Restaurant.objects.filter(id=pk).update(percentage=result)
         
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)
  

class Editpost(UpdateView):
    model = Post 
    template_name = 'Restaurant/modifier_post.html'
    form_class = PostForm

class Supprimerpost(DeleteView):
    model = Post 
    template_name = 'Restaurant/delete_post.html'
 
    def get_success_url(self, **kwargs):
        return reverse('compteGratuitprofile', args=[self.request.user.username])

class Supprimercommentaire(DeleteView):
    model = Commentaire 
    template_name = 'Restaurant/delete_commentaire.html'
 
    def get_success_url(self,**kwargs):
        return reverse('index')

class EditCommentaire(UpdateView):
    model = Commentaire 
    template_name = 'Restaurant/modifier_commentaire.html'
    form_class = UpdateCommentaireForm


"""Owner of Restaurant """

def index2(request):
    user = Comptepayant.objects.get(utilisateur=request.user)
    restau = Restaurant.objects.filter(directeur=user)  
    """ Pagination """
    restau_filter = RestaurantFilter(request.GET,queryset=restau)
    paginator = Paginator(restau_filter.qs, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'../templates/Restaurant/index2.html', {'page_obj': page_obj})

def detailrestauowner(request,intitule):
    restau = Restaurant.objects.filter(intitule=intitule.replace('-',' '))
    res = get_object_or_404(Restaurant,intitule=intitule.replace('-',' '))
    total = res.total_likes()
    Picture = PictureRestau.objects.filter(restaurant=res)

    return render(request,'../templates/Restaurant/detailRestauowner.html', {'restau': restau ,'total':total,'picture':Picture})

class Editrestau(UpdateView):
    model = Restaurant 
    template_name = 'Restaurant/modifier_restaurant.html'
    form_class = RestaurantForm
    def get_success_url(self,**kwargs):
        return reverse('index2')
    
class Supprimerrestau(DeleteView):
    model = Restaurant 
    template_name = 'Restaurant/delete_restau.html'
 
    def get_success_url(self,**kwargs):
        return reverse('index2')

class AjouterRestaurant(CreateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'Restaurant/ajouter_restau.html'

    def form_valid(self, form):
        form.instance.directeur = Comptepayant.objects.get(utilisateur=self.request.user)
        return super().form_valid(form)

class Ajouterphotos(CreateView):
    model = PictureRestau
    form_class = PhotoForm
    template_name = 'Restaurant/ajouter_photo.html'

    def form_valid(self, form):
        form.instance.directeur = Comptepayant.objects.get(utilisateur=self.request.user)
        return super().form_valid(form)


    