from rest_framework import routers, serializers, viewsets

from Profile.models import Profile
from Profile.models import ModelCiudad
from Profile.models import ModelGenero
from Profile.models import ModelOcupacion
from Profile.models import ModelEstado
from Profile.models import ModelEstadoCivil

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')

class CiudadSerializers(serializers.ModelSerializer):
    class Meta:
        model = ModelCiudad
        fields = ('__all__')

class GeneroSerializers(serializers.ModelSerializer):
    class Meta:
        model = ModelGenero
        fields = ('__all__')
    
class OcupacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = ModelOcupacion
        fields = ('__all__')

class EstadoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ModelEstado
        fields = ('__all__')
    
class EstadoCivilSerializers(serializers.ModelSerializer):
    class Meta:
        model = ModelEstadoCivil
        fields = ('__all__')