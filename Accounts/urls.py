from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static,serve
from django.conf import settings
from .import views
from .views import compteGratuiteditinfo ,compteGratuiteditdetails

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
    path('compteGratuitprofile/<str:slug>',views.compteGratuitprofile,name="compteGratuitprofile"),
    path('compteGratuiteditinfo/<str:slug>',compteGratuiteditinfo.as_view(),name="compteGratuiteditinfo"),
    path('compteGratuiteditdetails/<str:slug>',compteGratuiteditdetails.as_view(),name="compteGratuiteditdetails"),
]
"""
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
"""

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',
        serve,{'document_root':
                settings.MEDIA_ROOT, }),]