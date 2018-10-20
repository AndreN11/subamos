from django.shortcuts import render
from rest_framework.decorators import permission_classes
from aplicacion.models import *
from aplicacion.serializers import *
from aplicacion.permissions import IsPostOrIsAuthenticated
from rest_framework import generics

@permission_classes((IsPostOrIsAuthenticated, ))
class UsuarioList(generics.ListCreateAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

class CategoriaList(generics.ListCreateAPIView):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()
