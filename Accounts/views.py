from django.shortcuts import render,redirect
from django.views import generic 
from .models import Comptegratuit,Comptepayant,Utilisateur
from .form import ComptegratuitInscriptionForm,ComptepayantInscriptionForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponse

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token

from django.core.mail import EmailMessage

from django.views.generic import UpdateView
from django.contrib.sessions.backends.db import SessionStore


"""
def profile(request):
    return render(request,'../templates/profile.html')
"""
def profile(request,username):
    profile= Profile.objects.filter(username=username)
    context = {
        'profile': profile,
    }
    return render(request,'../templates/Accounts/profile.html',context)

def inscription(request):
    return render(request,'../templates/Accounts/inscription.html')
def login_view(request):
    return render(request,'../templates/Accounts/login.html')   
"""
class comptegratuit_inscription(CreateView):
    model = Utilisateur
    form_class = ComptegratuitInscriptionForm
    template_name = '../templates/compteGrinscr.html'
   
    def form_valid(self,form):
        utilisateur = form.save()
        login(self.request,utilisateur)
        return redirect('AcceuilComptegratuit')
"""
def comptegratuit_inscription(request):
        if request.method == 'POST':
            form = ComptegratuitInscriptionForm(request.POST,request.FILES)
            if form.is_valid():
                user = form.save()
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your blog account.'
                message = render_to_string('Accounts/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                            mail_subject, message, to=[to_email]
                )
                email.send()
                return HttpResponse('Please confirm your email address to complete the registration')
        else:
            form = ComptegratuitInscriptionForm()
        return render(request, '../templates/Accounts/compteGrinscr.html', {'form': form})    

def comptepayant_inscription(request):
        if request.method == 'POST':
            form = ComptepayantInscriptionForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your blog account.'
                message = render_to_string('../templates/Accounts/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                            mail_subject, message, to=[to_email]
                )
                email.send()
                return HttpResponse('Please confirm your email address to complete the registration')
        else:
            form = ComptepayantInscriptionForm()
        return render(request, '../templates/Accounts/comptepayinscr.html', {'form': form})    
    
def activate(request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = Utilisateur.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, Utilisateur.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            # return redirect('home')
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        else:
            return HttpResponse('Activation link is invalid!')
"""
class comptepayant_inscription(CreateView):
    model = Utilisateur
    form_class = ComptepayantInscriptionForm
    template_name = '../templates/comptepayinscr.html'
    
    def form_valid(self,form):
        utilisateur = form.save()
        login(self.request,utilisateur)
        return redirect('AcceuilComptepayant')
"""
def AcceuilComptepayant(request):
    return render(request,'../templates/Accounts/AcceuilComptepayant.html')
def AcceuilComptegratuit(request):
    return render(request,'../templates/Accounts/AcceuilComptegratuit.html')

def comptepayant_login(request):
    if request.method == 'POST':
        form= AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            utilisateur = authenticate(username=username,password=password)
            if utilisateur is not None:
                login(request,utilisateur)
                return redirect('../templates/Accounts/AcceuilComptepayant')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    return render(request, '../templates/Accounts/comptepayantlogin.html',
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
                request.session['id'] = utilisateur.id
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    return render(request, '../templates/Accounts/comptegratuitlogin.html',
    context={'form':AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')

def compteGratuitprofile(request,slug):
    profileCG = Comptegratuit.objects.filter(slug=slug)
    return render(request,'../templates/Accounts/profile.html', {'profileCG': profileCG })
"""
class EditcompteGratuiteditprofile(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'Accounts/edit_profile_CG.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.Profile
"""
class compteGratuiteditinfo(UpdateView):
    model = Utilisateur 
    template_name = 'Accounts/edit_profile_CG_infos.html'
    fields = ['username','first_name','last_name','email']



class compteGratuiteditdetails(generic.UpdateView):
    model = Comptegratuit 
    template_name = 'Accounts/edit_profile_CG_details.html'
    fields = ['photoprofil','cin','description','ville','pays','numtel','website']

    