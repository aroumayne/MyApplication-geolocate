from django.db import models

# Create your models here.
# création de notre BD

class Etablissement(models.Model):
    nom = models.CharField(max_length=255, null=True, blank=True, verbose_name="Nom de l'Etablissement")
    ville = models.CharField(max_length=255, null=True, blank=True, verbose_name="Ville")
    quartier = models.CharField(max_length=255, null= True, blank=True,verbose_name="Nom du Quartier")
    repere = models.TextField(max_length=255, null= True, blank=True,  verbose_name="Répère")
    telephone = models.CharField(max_length=30, null= True, blank=True, verbose_name="Telephone(s)")
    email = models.CharField(max_length=255, null= True, blank=True, verbose_name="Email(s)")
    adresse_ets = models.CharField(max_length=255, null= True, blank=True, verbose_name="Adresse")
    latitude = models.CharField(max_length=255,  verbose_name="Latitude")
    longitude = models.CharField(max_length=255, verbose_name="Longitude")

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = "Etablissements"