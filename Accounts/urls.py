from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('AcceuilComptepayant/',views.AcceuilComptepayant,name='AcceuilComptepayant'),
    path('AcceuilComptegratuit/',views.AcceuilComptegratuit,name='AcceuilComptegratuit'),
    path('inscription/',views.inscription,name='inscription'),
    path('comptegratuit_inscription/',views.comptegratuit_inscription.as_view(),name='comptegratuit_inscription'),
    path('comptepayant_inscription/',views.comptepayant_inscription.as_view(),name='comptepayant_inscription'),
    path('login/',views.login_view,name='login'),
    path('comptegratuit_login/',views.comptegratuit_login,name='comptegratuit_login'),
    path('comptepayant_login/',views.comptepayant_login,name='comptepayant_login'),
    #path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
]