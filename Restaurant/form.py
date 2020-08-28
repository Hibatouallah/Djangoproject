
from django.db import transaction
from .models import Post , Restaurant
from django import forms
from django.forms import ModelForm

class PostForm(forms.Form):
    #user = forms.IntegerField(widget=forms.HiddenInput()) 
    description = forms.CharField(widget=forms.Textarea)
    restau = forms.ModelChoiceField(queryset=Restaurant.objects.all(), empty_label=None)
    image = forms.ImageField()

    @transaction.atomic
    def save(self):
     
        post = Post.objects.create(user = 2)
        #post.user = self.cleaned_data.get('user')
        post.description = self.cleaned_data.get('description')
        post.restau = self.cleaned_data.get('restau')
        post.image = self.cleaned_data.get('image')

        Post.save()
        return Post