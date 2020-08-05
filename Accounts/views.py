from django.shortcuts import render,redirect
from django.views.generic import CreateView
from .models import Comptegratuit,Comptepayant,Utilisateur
from .form import ComptegratuitInscriptionForm,ComptepayantInscriptionForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def index(request):
    return render(request,'../templates/index.html')
def inscription(request):
    return render(request,'../templates/inscription.html')
def login_view(request):
    return render(request,'../templates/login.html')   

class comptegratuit_inscription(CreateView):
    model = Utilisateur
    form_class = ComptegratuitInscriptionForm
    template_name = '../templates/compteGrinscr.html'

    def form_valid(self,form):
        utilisateur = form.save()
        login(self.request,utilisateur)
        return redirect('AcceuilComptegratuit')

class comptepayant_inscription(CreateView):
    model = Utilisateur
    form_class = ComptepayantInscriptionForm
    template_name = '../templates/comptepayinscr.html'
    
    def form_valid(self,form):
        utilisateur = form.save()
        login(self.request,utilisateur)
        return redirect('AcceuilComptepayant')

def AcceuilComptepayant(request):
    return render(request,'../templates/AcceuilComptepayant.html')
def AcceuilComptegratuit(request):
    return render(request,'../templates/AcceuilComptegratuit.html')

def comptepayant_login(request):
    if request.method == 'POST':
        form= AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            utilisateur = authenticate(username=username,password=password)
            if utilisateur is not None:
                login(request,utilisateur)
                return redirect('AcceuilComptepayant')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    return render(request, '../templates/comptepayantlogin.html',
    context={'form':AuthenticationForm()})

def comptegratuit_login(request):
    if request.method == 'POST':
        form= AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            utilisateur = authenticate(username=username,password=password)
            if utilisateur is not None:
                login(request,utilisateur)
                return redirect('AcceuilComptegratuit')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    return render(request, '../templates/comptegratuitlogin.html',
    context={'form':AuthenticationForm()})
"""
def login_view(request):
    if request.method == 'POST':
        form= AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            utilisateur = authenticate(username=username,password=password)
            if utilisateur is not None:
                login(request,utilisateur)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})
"""

def logout_view(request):
    logout(request)
    return redirect('/')