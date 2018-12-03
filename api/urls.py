from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from . import views

urlpatterns = [    
    url(r'^PersonaLista/$',views.PersonaLista.as_view()),
    url(r'^PersonaLista/(?P<pk>[0-9]+)$',views.PersonaDetalle.as_view()),
    url(r'^EstadoCivilLista/$',views.EstadoCivilLista.as_view()),
    url(r'^EstadoCivilLista/(?P<pk>[0-9]+)$',views.EstadoCivilDetalle.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)