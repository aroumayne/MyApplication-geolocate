#ici fichier de routage de geolocate pas de projet Mapschool
#lors de la creation d'une application django ne cree pas ce fichier
#donc c'est au programmeur de le faire y compris tous les autres fichiers
#telsque serializers.py, forms.py, fichiers.py ....etc.

from rest_framework.serializers import ModelSerializer
from .models import Etablissement

class EtablissementSerializer(ModelSerializer):

    class Meta:
        model=Etablissement
        fields=['nom', 'ville', 'quartier', 'repere', 'telephone', 'email', 'adresse', 'longitude', 'latitude']