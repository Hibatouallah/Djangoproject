from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Comptegratuit,Comptepayant,Utilisateur
from django import forms

class ComptegratuitInscriptionForm(UserCreationForm):
    cin = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    website = forms.CharField(required=False)
    description = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    ville = forms.CharField(required=True)
    photoprofil = forms.FileField(required=False)
    photocouverture = forms.FileField(required=False)
    pays = forms.CharField(required=True)
    codepostal = forms.CharField(required=True)
    numtel =forms.CharField(required=True)
   

    class Meta(UserCreationForm.Meta):
        model = Utilisateur


    @transaction.atomic
    def save(self):
        utilisateur = super().save(commit=False)
        utilisateur.email = self.cleaned_data.get('email')
        utilisateur.last_name = self.cleaned_data.get('last_name')
        utilisateur.first_name = self.cleaned_data.get('first_name')
        utilisateur.uncomptegratuit = True

        utilisateur.save()
        comptegratuit = Comptegratuit.objects.create(utilisateur = utilisateur)
        comptegratuit.cin  = self.cleaned_data.get('cin')
 
    
        comptegratuit.website = self.cleaned_data.get('website')
        comptegratuit.description = self.cleaned_data.get('description')
        comptegratuit.ville = self.cleaned_data.get('ville')
        comptegratuit.photoprofil = self.cleaned_data.get('photoprofil')
        comptegratuit.photocouverture = self.cleaned_data.get('photocouverture')
        comptegratuit.pays = self.cleaned_data.get('pays')
        comptegratuit.codepostal = self.cleaned_data.get('codepostal')
        comptegratuit.numtel = self.cleaned_data.get('numtel')
        comptegratuit.location = self.cleaned_data.get('location')
        comptegratuit.save()
        return utilisateur


class ComptepayantInscriptionForm(UserCreationForm):
    cin = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    pays = forms.CharField(required=True)
    codepostal = forms.CharField(required=True)
    numtel = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = Utilisateur


    @transaction.atomic
    def save(self):
        utilisateur = super().save(commit=False)
        utilisateur.uncomptepayant = True
        utilisateur.is_staff = True

        utilisateur.email = self.cleaned_data.get('email')
        utilisateur.first_name = self.cleaned_data.get('first_name')
        utilisateur.last_name = self.cleaned_data.get('last_name')

        utilisateur.save()
        comptepayant = Comptepayant.objects.create(utilisateur = utilisateur)
        comptepayant.cin  = self.cleaned_data.get('cin')

        comptepayant.pays = self.cleaned_data.get('pays')
        comptepayant.codepostal = self.cleaned_data.get('codepostal')
        comptepayant.numtel = self.cleaned_data.get('numtel')
        comptepayant.save()
        return utilisateur