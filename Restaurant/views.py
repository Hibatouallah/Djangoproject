from django.shortcuts import render
from .models import Restaurant,Post
from Accounts.models import Utilisateur,Comptegratuit
from django.views.generic import ListView,DetailView,CreateView ,UpdateView,DeleteView
from django.forms import modelformset_factory
from.form import PostForm
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
"""
def poster(request,intitule):
    

def restaurant_create(request):
    Imageformatset = modelformset_factory(Images, fields=('image',),extra=4)
    if request.method == 'POST':
        form = RestaurantCreateForm(request.POST)

        if form.is_valid():
            restaurant = form


def index(request):
    #return render(request,'../templates/index.html')
    restau = Restaurant.objects.all()
    return render(request,'../templates/Accounts/index.html', {'restau': restau })

"""

class index(ListView):
    model = Restaurant
    template_name = 'Restaurant/index.html'

def detailrestau(request,intitule):
    restau = Restaurant.objects.filter(intitule=intitule.replace('-',' '))
    return render(request,'../templates/Restaurant/detailRestau.html', {'restau': restau })
def mespostes(request,id):
    usercg = Comptegratuit.objects.get(utilisateur=id)
    post = Post.objects.filter(user=usercg.id)
    return render(request,'../templates/Restaurant/listeposte.html', {'post': post })
class AjouterPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'Restaurant/ajouter_post.html'
    fields = ['description','restaurant','image']

    def form_valid(self, form):
        form.instance.user = Comptegratuit.objects.get(utilisateur=self.request.user)
        return super().form_valid(form)
    
class Editpost(UpdateView):
    model = Post 
    template_name = 'Restaurant/modifier_post.html'
    fields = ['description','restaurant','image']

class Supprimerpost(DeleteView):
    model = Post 
    template_name = 'Restaurant/delete_post.html'
 
    def get_success_url(self, **kwargs):
        return reverse('mespostes', args=[self.request.user.id])
