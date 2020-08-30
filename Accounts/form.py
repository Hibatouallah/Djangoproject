from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Comptegratuit,Comptepayant,Utilisateur
from django import forms

class ComptegratuitInscriptionForm(UserCreationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    cin = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    website = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    ville = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    photoprofil = forms.ImageField(required = False,widget=forms.FileInput())
    photocouverture = forms.ImageField(required = False,widget=forms.FileInput())
    pays = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    codepostal = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    numtel =forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
   

    class Meta(UserCreationForm.Meta):
        model = Utilisateur
        fields = ('username','cin','last_name','first_name','password1','password2','website','description','email','ville','photoprofil','photocouverture','pays','codepostal','numtel')

    def __init__(self, *args,**kwargs):
        super(ComptegratuitInscriptionForm,self).__init__(*args,**kwargs)

        self.fields['password1'].widget.attrs['class']= 'form-control'
        self.fields['password2'].widget.attrs['class']= 'form-control'

    @transaction.atomic
    def save(self):
        utilisateur = super().save(commit=False)
        utilisateur.username = self.cleaned_data.get('username')
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
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    cin = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    photoprofil = forms.ImageField(required=False,widget=forms.FileInput())
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    pays = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    codepostal = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    numtel = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = Utilisateur
        fields = ('username','cin','last_name','first_name','password1','password2','email','photoprofil','pays','codepostal','numtel')

    def __init__(self, *args,**kwargs):
        super(ComptepayantInscriptionForm,self).__init__(*args,**kwargs)

        self.fields['password1'].widget.attrs['class']= 'form-control'
        self.fields['password2'].widget.attrs['class']= 'form-control'

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
        comptepayant.photoprofil = self.cleaned_data.get('photoprofil')
        comptepayant.numtel = self.cleaned_data.get('numtel')
        comptepayant.save()
        return utilisateur