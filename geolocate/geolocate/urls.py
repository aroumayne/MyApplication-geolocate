#ici fichier de routage de geolocate pas du projet Mapschool


from django.conf.urls import url, include
from django.contrib import admin

#importation
from geolocate import views
from geolocate import models
from geolocate import serializers

#definition d'un namespace(petit nom de mon application)
app_name='geolocate'

urlpatterns=[

    #chargement des urls du site d'administration depuis mon appli geolocate
    url(r'^admin/' , admin.site.urls),

    #les routes des API
    #pour mieux comprendre la synthaxe des urls, il faut compreendre que la partie de gauche affichera
    #l'url que l'utilisateur verra sur son navigateur
    #la partie du milieu indique la vue de traitement correspondant dans le fichier View.py
    #la partie de droite s'il y en a indique juste le nom que l'on a choisit de donner à notre
    #url afin que l'on puisse pouvoir pointer dessus comme avec un lien exemple:
    #api/ets/1/ ou api/ets/101for
    url(r'^api/liste/etablissement/$', views.EtablissementDetailListe.as_view()),

    #?P<pk>\d+ cet expression reguliere permet d'afficher l'identifiant correspondant

    url(r'^api/etablissement/(?P<pk>\d+)/$', views.EtablissementDetailList.as_view()),



    #les routes de mon site
    url(r'^etablissement/$, views.EtablissementListView.as_view(), name='etablissement_list'),
    url(r'^etablissement-detail/(?P<pk>\d+/$', views.EtablissementDetailView.as_view(), name='etablissement-detail'),

]

