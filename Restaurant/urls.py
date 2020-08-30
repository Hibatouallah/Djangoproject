from django.urls import path
from django.conf.urls import url
from .views import AjouterPost,Editpost,Supprimerpost,AjouterCommentaire
from .import views 

urlpatterns=[
    path('',views.index,name='index'),
    path('detailrestau/<str:intitule>/',views.detailrestau,name='detailrestau'),
    path('like/<int:pk>/',views.LikeView,name='like_restau'),
    path('likecom/<int:pk>/',views.LikeCommentaireView,name='like_comm'),
    path('mespostes/<int:id>/',views.mespostes,name='mespostes'),
    path('mespostes/ajouter_post/<int:pk>',AjouterPost.as_view(),name="ajouterpost"),
    path('mespostes/editpost/<int:pk>',Editpost.as_view(),name="editpost"),
    path('mespostes/<int:pk>/supprimer',Supprimerpost.as_view(),name="supprimerpost"),
    path('commentaire/<int:pk>/ajouter_commentaire/',AjouterCommentaire.as_view(),name="ajouter_commentaire"),
]