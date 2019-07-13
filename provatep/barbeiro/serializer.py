from rest_framework import serializers

from barbeiro.models import Servico, Produto


class ServicoSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Servico
        fields = ('id', 'nome', 'valor')


class ProdutoSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Produto
        fields = ('id', 'nome', 'valor','quantidade')

