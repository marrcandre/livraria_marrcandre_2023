from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from livraria.models import Livro
from livraria.serializers import (
    LivroDetailSerializer,
    LivroListSerializer,
    LivroSerializer,
)


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["categoria"]

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrieve":
            return LivroDetailSerializer
        else:
            return LivroSerializer
