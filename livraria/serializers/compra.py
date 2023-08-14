from rest_framework.serializers import ModelSerializer, CharField

from livraria.models import Compra

class CompraSerializer(ModelSerializer):
    usuario = CharField(source='usuario.email')
    class Meta:
        model = Compra
        fields = "__all__"


