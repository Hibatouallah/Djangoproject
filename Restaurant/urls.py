from django.urls import path
from django.conf.urls import url
from .views import AjouterPost,Editpost,Supprimerpost,Supprimercommentaire,EditCommentaire,Editrestau,Supprimerrestau,AjouterRestaurant,Ajouterphotos
from .import views 
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    path('',csrf_exempt(views.index),name='index'),
    path('detailrestau/<str:intitule>/',views.detailrestau,name='detailrestau'),
    path('like/<int:pk>/',views.LikeView,name='like_restau'),
    path('myposts/add_post/<int:pk>',AjouterPost.as_view(),name="ajouterpost"),
    path('myposts/<int:pk>/editpost',Editpost.as_view(),name="editpost"),
    path('myposts/<int:pk>/delete',Supprimerpost.as_view(),name="supprimerpost"),
    path('profile/<str:slug>',views.compteGratuitprofile,name="compteGratuitprofile"),
    path('comment/<int:pk>/ajouter_comment/',views.ajouterCommentaire,name="ajouter_commentaire"),
    path('comment/<int:pk>/delete_comment',Supprimercommentaire.as_view(),name="supprimercommentaire"),
    path('comment/editcomment/<int:pk>',EditCommentaire.as_view(),name="editcommentaire"),
    path('likepost/<int:pk>/',views.LikePostView,name='LikePostView'),

    path('homeownerrestau/',csrf_exempt(views.index2),name='index2'),
    path('detailrestauowner/<str:intitule>/',views.detailrestauowner,name='detailrestauowner'),
    path('restaurant/<int:pk>/editrestau',Editrestau.as_view(),name="editrestau"),
    path('restaurant/<int:pk>/delete',Supprimerrestau.as_view(),name="supprimerrestau"),
    path('restaurant/add_restau/<int:pk>',AjouterRestaurant.as_view(),name="ajouterrestau"),
    path('restaurant/add_photos/<int:pk>',Ajouterphotos.as_view(),name="ajouterphotos"),
]