from django.urls import path

# el . indica que vamos a importar algo de la misma carpeta
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]