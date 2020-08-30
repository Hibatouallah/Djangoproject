from django.shortcuts import render,get_object_or_404
from .models import Restaurant,Post,Commentaire
from Accounts.models import Utilisateur,Comptegratuit
from django.views.generic import ListView,DetailView,CreateView ,UpdateView,DeleteView
from django.forms import modelformset_factory
from.form import CommentaireForm , AjouterPostForm ,ModifierPostForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
"""
def poster(request,intitule):
    

def restaurant_create(request):
    Imageformatset = modelformset_factory(Images, fields=('image',),extra=4)
    if request.method == 'POST':
        form = RestaurantCreateForm(request.POST)

        if form.is_valid():
            restaurant = form
class index(ListView):
    model = Restaurant
    template_name = 'Restaurant/index.html'

"""
def index(request):
    res = requests.get('https://ipinfo.io')
    data = res.json()
    city = data['city']
    restau = Restaurant.objects.filter(location=city)
    return render(request,'../templates/Restaurant/index.html', {'restau': restau })


def detailrestau(request,intitule):
    restau = Restaurant.objects.filter(intitule=intitule.replace('-',' '))
    likesres = get_object_or_404(Restaurant,intitule=intitule.replace('-',' '))
    total = likesres.total_likes()
    return render(request,'../templates/Restaurant/detailRestau.html', {'restau': restau ,'total':total})


def LikeView(request,pk):
    restau = get_object_or_404(Restaurant,id=request.POST.get('restaurant_id'))
    user = Comptegratuit.objects.get(utilisateur=request.user.id)
    restau.likes.add(user)
    return HttpResponseRedirect(reverse('index'))
def LikeCommentaireView(request,pk):
    comment = get_object_or_404(Commentaire,id=request.POST.get('commentaire_id'))
    user = Comptegratuit.objects.get(utilisateur=request.user.id)
    comment.likes.add(user)
    return HttpResponseRedirect(reverse('detailrestau',args=[comment.restaurant.intitule]))

def mespostes(request,id):
    usercg = Comptegratuit.objects.get(utilisateur=id)
    post = Post.objects.filter(user=usercg.id)
    return render(request,'../templates/Restaurant/listeposte.html', {'post': post })

class AjouterPost(CreateView):
    model = Post
    form_class = AjouterPostForm
    template_name = 'Restaurant/ajouter_post.html'
    #fields = ['description','restaurant','image']

    def form_valid(self, form):
        form.instance.user = Comptegratuit.objects.get(utilisateur=self.request.user)
        return super().form_valid(form)

class AjouterCommentaire(CreateView):
    model = Commentaire
    template_name = 'Restaurant/ajouter_commentaire.html'
    form_class = CommentaireForm

    def form_valid(self, form):
        form.instance.user = Comptegratuit.objects.get(utilisateur=self.request.user)
        form.instance.restaurant_id = self.kwargs['pk']
        return super().form_valid(form)  

class Editpost(UpdateView):
    model = Post 
    template_name = 'Restaurant/modifier_post.html'
    form_class = ModifierPostForm
    #fields = ['description','restaurant','image']

class Supprimerpost(DeleteView):
    model = Post 
    template_name = 'Restaurant/delete_post.html'
 
    def get_success_url(self, **kwargs):
        return reverse('mespostes', args=[self.request.user.id])
