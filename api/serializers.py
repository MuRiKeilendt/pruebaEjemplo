from rest_framework import serializers
from .models import Persona,EstadoCivil

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Persona
        fields= ('id','nombre','edad','sexo','estadoCivil')

class EstadoCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model= EstadoCivil
        fields= ('id','nombre')
