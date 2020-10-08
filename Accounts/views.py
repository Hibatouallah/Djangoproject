from django.shortcuts import render,redirect
from django.views import generic 
from .models import Comptegratuit,Comptepayant,Utilisateur
from .form import ComptegratuitInscriptionForm,ComptepayantInscriptionForm,ModifierUser,ModifiercompteGratuit,ModifiercomptePayant,Contact
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm
from django.contrib import messages
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token

from django.core.mail import EmailMessage,send_mail,BadHeaderError

from django.views.generic import UpdateView
from django.contrib.sessions.backends.db import SessionStore

def inscription(request):
    return render(request,'../templates/Accounts/inscription.html')
def login_view(request):
    return render(request,'../templates/Accounts/login.html') 

def checkingEmail(request):
    return render(request,'../templates/Accounts/checkingemail.html')  

def confirmationpage(request):
    return render(request,'../templates/Accounts/confirmationpage.html') 

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
                return redirect('checkingEmail')
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
                return redirect('checkingEmail')
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
            return redirect('confirmationpage')
        else:
            return HttpResponse('Activation link is invalid!')

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
                return redirect('index2')
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
    return redirect('inscription')

class CompteGratuiteditinfo(UpdateView):
    model = Utilisateur 
    template_name = 'Accounts/edit_profile_CG_infos.html'
    form_class = ModifierUser
    def get_success_url(self, **kwargs):
        return reverse('compteGratuitprofile', args=[self.request.user.username]) 
    
class CompteGratuiteditdetails(generic.UpdateView):
    model = Comptegratuit 
    template_name = 'Accounts/edit_profile_CG_details.html'
    form_class = ModifiercompteGratuit
    def get_success_url(self, **kwargs):
        return reverse('compteGratuitprofile', args=[self.request.user.username]) 

class Comptepayanteditinfo(UpdateView):
    model = Utilisateur 
    template_name = 'Accounts/edit_profile_CG_infos.html'
    form_class = ModifierUser
    def get_success_url(self, **kwargs):
        return reverse('comptepayantprofile', args=[self.request.user.username])   
        
class ComptePayanteditdetails(generic.UpdateView):
    model = Comptepayant 
    template_name = 'Accounts/edit_profile_CP_details.html'
    form_class = ModifiercomptePayant
    def get_success_url(self, **kwargs):
        return reverse('comptepayantprofile', args=[self.request.user.username])  
        

def comptepayantprofile(request,slug):
    profile = Comptepayant.objects.filter(slug=slug)
    return render(request,'../templates/Accounts/profile.html', {'profile': profile })
def confirmpagecontact(request):
    return render(request,'../templates/Accounts/confirmpagecontact.html')

def contact(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']
        send_mail(
           'Message from '+ message_name ,
           message,
           message_email,
           ['hibatouallah.1996@gmail.com'],
        )
        return redirect('confirmpagecontact')
    else:
        return  HttpResponseRedirect(url)
