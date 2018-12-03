from .models import Persona,EstadoCivil
from .serializers import PersonaSerializer,EstadoCivilSerializer
from rest_framework import generics
# Create your views here.
class PersonaLista(generics.ListCreateAPIView):
    queryset = Persona
    serializer_class = PersonaSerializer

class PersonaDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Persona
    serializer_class = PersonaSerializer

class EstadoCivilLista(generics.ListCreateAPIView):
    queryset = EstadoCivil
    serializer_class = EstadoCivilSerializer

class EstadoCivilDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = EstadoCivil
    serializer_class = EstadoCivilSerializer

