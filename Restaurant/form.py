
from django.db import transaction
from .models import Post , Restaurant,Commentaire,PictureRestau
from django import forms
from django.forms import ModelForm


class PostForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput)
    class Meta:
        model = Post
        fields = ('restaurant','description','image')

        widgets = {
            'restaurant': forms.Select(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'image' : forms.ImageField(required=False),
        }




class ComentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('intitule','description')

        widgets = {
            'intitule': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),

        }

class RestaurantForm(forms.ModelForm):
    picture_default = forms.ImageField(required=False, widget=forms.FileInput)
    menu = forms.ImageField(required=False, widget=forms.FileInput)
    class Meta:
        model = Restaurant
        fields = ('cuisine','picture_default','meals','ville','intitule','website','email','horaire','adresse','numtele','price','menu')

        widgets = {
            'cuisine': forms.SelectMultiple(attrs={'class':'form-control'}),
            'meals': forms.SelectMultiple(attrs={'class':'form-control'}),
            'ville': forms.TextInput(attrs={'class':'form-control'}),
            'intitule': forms.TextInput(attrs={'class':'form-control'}),
            'website': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'horaire': forms.TextInput(attrs={'class':'form-control'}),
            'adresse': forms.Textarea(attrs={'class':'form-control'}),
            'numtele': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.Select(attrs={'class':'form-control'}),
            'picture_default': forms.ImageField(required=False),
            'menu': forms.ImageField(required=False),
        }


class PhotoForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput)
    class Meta:
        model = PictureRestau
        fields = ('restaurant','image')

        widgets = {
            'restaurant': forms.Select(attrs={'class':'form-control'}),
            'image': forms.ImageField(required=False),

        }

