from django.urls import path
from django.conf.urls import url
from .views import index,AjouterPost,Editpost,Supprimerpost
from .import views 

urlpatterns=[
    path('',index.as_view(),name='index'),
    path('detailrestau/<str:intitule>/',views.detailrestau,name='detailrestau'),
    path('mespostes/<int:id>/',views.mespostes,name='mespostes'),
    path('mespostes/ajouter_post/<int:pk>',AjouterPost.as_view(),name="ajouterpost"),
    path('mespostes/editpost/<int:pk>',Editpost.as_view(),name="editpost"),
    path('mespostes/<int:pk>/supprimer',Supprimerpost.as_view(),name="supprimerpost"),
]