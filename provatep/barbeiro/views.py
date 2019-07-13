from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from barbeiro.serializer import ServicoSerializer, ProdutoSerializer


class ListServico(generics.ListCreateAPIView):
    serializer_class = ServicoSerializer
    authentication_classes = (JSONWebTokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(dono=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return user.servicos.all()


class ListProduto(generics.ListCreateAPIView):
    serializer_class = ProdutoSerializer
    authentication_classes = (JSONWebTokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(dono=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return user.produtos.all()
