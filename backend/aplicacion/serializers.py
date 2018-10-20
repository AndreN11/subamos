from aplicacion.models import *
from django.contrib.auth.models import User
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    fecha_nacimiento = serializers.DateField(required=False,source="usuario.fecha_nacimiento")
    perfil = serializers.CharField(max_length=500, allow_blank=True,source="usuario.perfil")
 
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'perfil','fecha_nacimiento')
    def create(self, validated_data, instance=None):
        profile_data = validated_data.pop('usuario')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        Usuario.objects.update_or_create(user=user,**profile_data)
        return user

class CategoriaSerializer(serializers.ModelSerializer):
   class Meta:
       model = Categoria
       fields = ('id','nombrecategoria')

       