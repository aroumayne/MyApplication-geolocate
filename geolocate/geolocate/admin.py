from django.contrib import admin
from . import models
from django.conf import settings

# Register your models here.

#cette classe me permet de definir l'affichage de mes données dans la partie admin
#list_display permet de choisir les elements que je souhaite dans ma liste
#list-filter permet d'assigner des filtres
#search_fields me permettra dans le champ de rechercher d'effectuer une recherche sur les elements choisi
#fieldsets permettra d'inserer les champs de frmulaire de création ou modification

class EtablissementAdmin(admin.ModelAdmin):
    list_display   = ('nom', 'ville', 'quartier', 'repere', 'telephone', 'email', 'adresse_ets', 'longitude', 'latitude',)
    list_filter    = ('nom', 'ville', 'quartier', 'repere', 'telephone', 'email', 'adresse_ets', 'longitude', 'latitude', )
    search_fields  = ('nom', 'ville', 'quartier',)

    fieldsets = (
        (None, {
            'fields': ('nom', 'ville', 'quartier', 'repere', 'telephone', 'email', 'adresse_ets', 'longitude', 'latitude', )
        }),
    )

admin.site.register(models.Etablissement.EtablissementAdmin)