
from django.db import transaction
from .models import Post , Restaurant,Commentaire
from django import forms
from django.forms import ModelForm


class AjouterPostForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput)
    class Meta:
        model = Post
        fields = ('restaurant','description','image')

        widgets = {
            'restaurant': forms.Select(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'image' : forms.ImageField(required=False),
        }

class ModifierPostForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput)
    class Meta:
        model = Post
        fields = ('description','image')

        widgets = {
 
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'image' : forms.ImageField(required=False),
        }

class CommentaireForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput)
    class Meta:
        model = Commentaire
        fields = ('intitule','description','image')

        widgets = {
            'intitule': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'image' : forms.ImageField(required=False),
        }