from rest_framework.serializers import ModelSerializer, CharField

from livraria.models import Compra

class CompraSerializer(ModelSerializer):
    usuario = CharField(source='usuario.email')
    status = CharField(source='get_status_display')
    class Meta:
        model = Compra
        fields = "__all__"


