from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static,serve
from django.conf import settings
from .import views
from .views import CompteGratuiteditinfo ,CompteGratuiteditdetails,ComptePayanteditdetails,Comptepayanteditinfo
from django.contrib.auth import views as auth_views
urlpatterns=[
    
    path('AcceuilComptepayant/',views.AcceuilComptepayant,name='AcceuilComptepayant'),
    path('AcceuilComptegratuit/',views.AcceuilComptegratuit,name='AcceuilComptegratuit'),
    path('inscription/',views.inscription,name='inscription'),
    path('comptegratuit_inscription/',views.comptegratuit_inscription,name='comptegratuit_inscription'),
    path('comptepayant_inscription/',views.comptepayant_inscription,name='comptepayant_inscription'),
    path('login/',views.login_view,name='login'),
    path('comptegratuit_login/',views.comptegratuit_login,name='comptegratuit_login'),
    path('comptepayant_login/',views.comptepayant_login,name='comptepayant_login'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('logout/',views.logout_view,name='logout'),
    path('checkingEmail/',views.checkingEmail,name='checkingEmail'),
    path('confirmationpage/',views.confirmationpage,name='confirmationpage'),
    
    path('compteGratuiteditinfo/<str:slug>',CompteGratuiteditinfo.as_view(),name="compteGratuiteditinfo"),
    path('compteGratuiteditdetails/<str:slug>',CompteGratuiteditdetails.as_view(),name="compteGratuiteditdetails"),

    path('profile/<str:slug>',views.comptepayantprofile,name="comptepayantprofile"),
    path('EditInfo/<str:slug>',Comptepayanteditinfo.as_view(),name="comptePayanteditinfo"),
    path('EditDetail/<str:slug>',ComptePayanteditdetails.as_view(),name="comptePayanteditdetails"),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='Accounts/password_reset.html'),name="password_reset"),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='Accounts/password_reset_done.html'),name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='Accounts/password_reset_confirm.html'),name="password_reset_confirm"),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='Accounts/password_reset_complete.html'),name="password_reset_complete"),
    path('contact/',views.contact,name="contact"),
    path('confirmpagecontact/',views.confirmpagecontact,name='confirmpagecontact'),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',
        serve,{'document_root':
                settings.MEDIA_ROOT, }),]